import requests
import tkinter as tk
from tkinter import filedialog, messagebox
import re

def convert_to_latex_text(text):
    # Convert inline equations
    def replace_inline_equations(match):
        equation = match.group(1)
        # Replace common notations with LaTeX equivalents
        equation = re.sub(r'\^(\w+)', r'^{\1}', equation)  # Superscripts
        equation = re.sub(r'_(\w+)', r'_{\1}', equation)  # Subscripts
        
        # Replace common symbols
        symbol_map = {
            '!=': r'\neq',
            '>=': r'\geq',
            '<=': r'\leq',
            '->': r'\rightarrow',
            'sqrt': r'\sqrt',
            'integral': r'\int',
            'sum': r'\sum',
            'pi': r'\pi',
            'theta': r'\theta',
            'delta': r'\delta',
            'sigma': r'\sigma',
            'infinity': r'\infty'
        }
        
        for symbol, latex_symbol in symbol_map.items():
            equation = equation.replace(symbol, latex_symbol)
        
        return f'${equation}$'
    
    # Replace inline equations (text between single $ signs)
    text = re.sub(r'\$([^$]+)\$', replace_inline_equations, text)
    
    return text

def upload_pdf(file_path, api_key):
    url = "https://api.chatpdf.com/v1/sources/add-file"
    headers = {'x-api-key': api_key}
    files = {'file': open(file_path, 'rb')}

    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        return response.json().get('sourceId')
    else:
        messagebox.showerror("Error", f"Error uploading PDF: {response.text}")
        return None

def ask_question(source_id, question, api_key):
    url = "https://api.chatpdf.com/v1/chats/message"
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
    }
    data = {
        "sourceId": source_id,
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        # Convert mathematical expressions to LaTeX text format
        answer = response.json().get('content')
        return convert_to_latex_text(answer)
    else:
        messagebox.showerror("Error", f"Error asking question: {response.text}")
        return None

def delete_pdf(source_id, api_key):
    url = "https://api.chatpdf.com/v1/sources/delete"
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
    }
    data = {"sources": [source_id]}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        messagebox.showinfo("Success", "PDF deleted successfully.")
    else:
        messagebox.showerror("Error", f"Error deleting PDF: {response.text}")

def configure_api_key(root):
    def save_api_key():
        api_key = api_key_entry.get()
        if api_key:
            root.api_key = api_key
            key_window.destroy()
        else:
            messagebox.showerror("Error", "API Key is required.")

    key_window = tk.Toplevel(root)
    key_window.title("Enter API Key") # Key: sec_eVIHB22XB8XNSm7o9qqKIKQv4JLZrash
    key_window.geometry("300x150")
    key_window.grab_set()

    tk.Label(key_window, text="Enter your ChatPDF API Key:").pack(pady=5)
    api_key_entry = tk.Entry(key_window, width=40, show="*")
    api_key_entry.pack(pady=5)
    tk.Button(key_window, text="Save", command=save_api_key).pack(pady=10)

def upload_and_interact(root):
    if not hasattr(root, 'api_key'):
        messagebox.showerror("Error", "Please set the API key first.")
        return

    file_path = filedialog.askopenfilename(title="Select a PDF File", filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return

    source_id = upload_pdf(file_path, root.api_key)
    if not source_id:
        return

    messagebox.showinfo("Success", f"PDF uploaded successfully. Source ID: {source_id}")

    while True:
        question_window = tk.Toplevel(root)
        question_window.title("Ask a Question")
        question_window.geometry("300x150")
        question_window.grab_set()

        tk.Label(question_window, text="Ask a question about the PDF:").pack(pady=5)
        question_entry = tk.Entry(question_window, width=40)
        question_entry.pack(pady=5)

        question_asked = tk.BooleanVar(value=False)

        def submit_question():
            question = question_entry.get()
            question_window.destroy()
            if question:
                answer = ask_question(source_id, question, root.api_key)
                if answer:
                    messagebox.showinfo("Answer", answer)
            question_asked.set(True)

        def cancel_interaction():
            question_window.destroy()
            question_asked.set(False)

        tk.Button(question_window, text="Submit", command=submit_question).pack(pady=5)
        tk.Button(question_window, text="Cancel", command=cancel_interaction).pack(pady=5)

        question_window.wait_window()

        if not question_asked.get():
            break

    if messagebox.askyesno("Delete PDF", "Do you want to delete the PDF source?"):
        delete_pdf(source_id, root.api_key)

def main():
    root = tk.Tk()
    root.title("ChatPDF Interaction")
    root.geometry("400x200")

    tk.Label(root, text="ChatPDF Interaction", font=("Helvetica", 16)).pack(pady=10)

    def set_api_key():
        configure_api_key(root)

    def start_interaction():
        if not hasattr(root, 'api_key'):
            messagebox.showerror("Error", "Please set the API key first.")
        else:
            upload_and_interact(root)

    tk.Button(root, text="Set API Key", command=set_api_key, width=20).pack(pady=5)
    tk.Button(root, text="Upload PDF and Interact", command=start_interaction, width=20).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()