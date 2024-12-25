#Calculator Project

# 1. Using Arithmatic Operators
no1 = input("Enter the 1st number : ")
op = input("Enter the operator (+,-,*,/,//,%,**) : ")
no2 = input("Enter the 2nd number : ")
no1 = int(no1)
no2 = int(no2)
if op == '+':
    print("Result = " + str(no1+no2))
elif op == '-':
    print("Result = " + str(no1-no2))
elif op == '*':
    print("Result = " + str(no1*no2))
elif op == '/':
    print("Result = " + str(no1/no2))
elif op == '//':
    print("Result = " + str(no1//no2))
elif op == '%':
    print("Result = " + str(no1%no2))
elif op == '**':
    print("Result = " + str(no1**no2))
else:
    print("Invalid Choice.")


# 1. Menu Driven Calculation
i =0
while i==0 :
    no1 = input("Enter the 1st number : ")
    op = input("Enter the operator (+,-): ")
    no2 = input("Enter the 2nd number : ")
    no1 = int(no1)
    no2 = int(no2)
    if op == '+':
        print("Result = " + str(no1 + no2))
    elif op == '-':
        print("Result = " + str(no1 - no2))
    else:
        print("invalid")
    i = int(input("If you want to calculate press 0."))


# 1. Menu Driven Calculation using user-defined function
def calculator(first, second):
    op = input("Enter the operator (+,-,*,/,//,%,^) : ")
    if op == '+':
        print("Result = " + str(first + second))
    elif op == '-':
        print("Result = " + str(first - second))
    elif op == '*':
        print("Result = " + str(first * second))
    elif op == '/':
        print("Result = " + str(first / second))
    elif op == '//':
        print("Result = " + str(first // second))
    elif op == '%':
        print("Result = " + str(first % second))
    elif op == '^':
        print("Result = " + str(first ** second))
    else:
        print("Invalid Choice.")
i = 0
while i == 0:
    f = input("Enter the 1st number : ")
    s = input("Enter the 2nd number : ")
    f = int(f)
    s = int(s)
    calculator(f, s)
    i = int(input("If you want to calculate more press 0 else press 1."))

