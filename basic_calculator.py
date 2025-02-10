def subtract(x, y):
    return x - y

def add(x,y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Can't by divided by zero"
    return x / y

def get_input():
    while True:
        try:
            num1= float(input("Enter num1: "))
            num2= float(input("Enter num2: "))
        except ValueError:
            print("Invalid Number!")
            continue

        operation = input("Enter the operation(+, -, /, *): ")

        if operation == "-":
            result = subtract(num1, num2)
        elif operation == "+":
            result = add(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid Operation")
            continue

        return result



def main():
    while True:
        answer = get_input()
        print(answer)

        cont = input("Do you want to contine? (y/n)").lower().strip()
        
        if cont == "n":
            print("Goodbye!")
            break
main()