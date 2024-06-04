import pyfiglet

ascii_banner = pyfiglet.figlet_format("Taschen\nRechner")
print(ascii_banner)

def get_operator(action):
    if action == '1':
        operator = "*"
        return operator
    elif action == '2':
        operator = "/"
        return operator
    elif action == '3':
        operator = "-"
        return operator
    elif action == '4':
        operator = "+"
        return operator
    else:
        print("Invalid action! Exiting...")
        quit()

def calculation(operator, num1, num2):
    operator_dict = {'*': lambda x, y: x * y,
                     '/': lambda x, y: x / y if y != 0 else "Error: Division by zero",
                     '-': lambda x, y: x - y,
                     '+': lambda x, y: x + y}

    return operator_dict.get(operator, lambda x, y: "Error: Invalid operator")(num1, num2)

print("Choose your action")
print("Multiplication       [1]")
print("Division             [2]")
print("Subtraction          [3]")
print("Addition             [4]")

action = input("Action: ")

num1 = float(input("Erste Nummer: "))
num2 = float(input("Zweite Nummer: "))

operator = get_operator(action)
result = calculation(operator, num1, num2)

print(f"The result of {num1} {operator} {num2} is: {result}")
