import tkinter as tk
from tkinter import ttk

# Function to display output
def display_output():
    user_input = entry.get()
    output_label.config(text=f"You Entered: {user_input}")

# Create main window
root = tk.Tk()
root.title("Simple Input-Output")

# Create and place widgets
frame = ttk.Frame(root, padding="20")
frame.grid()

label = ttk.Label(frame, text="Enter Something:")
label.grid(column=0, row=0, padx=5, pady=5)

entry = ttk.Entry(frame, width=30)
entry.grid(column=1, row=0, padx=5, pady=5)

button = ttk.Button(frame, text="Submit", command=display_output)
button.grid(column=0, row=1, columnspan=2, pady=10)

output_label = ttk.Label(frame, text="", font=("Arial", 12))
output_label.grid(column=0, row=2, columnspan=2, pady=5)

# Start the GUI event loop
root.mainloop()
