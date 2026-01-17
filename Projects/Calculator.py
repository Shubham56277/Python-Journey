def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multi(a,b):
    return a * b
def div(a,b):
    if b ==0:
        return "Error1" \
        "! Division by zero."
    return a / b
while True:
    print("Select Operation :\n")
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Exit")
    choice = input(" Enter Choice btw 1-5 : ")
    if choice == '5':
        print("Calculator is closed.")
        break

    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter First Number : "))
        b = float(input("Enter Second Number : "))
        if choice == '1':
            print("Result =", add(a, b))
        elif choice == '2':
            print("Result =", sub(a, b))
        elif choice == '3':
            print("Result =", multi(a, b))
        elif choice == '4':
            print("Result =", div(a, b))
    else:
        print("Invalid choice, Type 1-5 ")
