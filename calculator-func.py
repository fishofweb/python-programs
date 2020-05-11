print("Welcome to calculator app.")
history = []
def addition(num1,num2):
    add = num1 + num2

    history.append(f"{num1} + {num2}= {add}")
    return add

def subtraction(num1,num2):
    sub = num1 - num2
    history.append(f"{num1} - {num2}= {sub}")
    return sub

def multiply(num1,num2):
    mul = num1 * num2
    history.append(f"{num1} x {num2}= {mul}")
    return mul

def divide(num1,num2):
    d = num1 / num2
    # history.append(d)
    history.append(f"{num1} / {num2}= {d}")
    return d

def exp(num1,num2):
    e = num1 ** num2
    # history.append(e)
    history.append(f"{num1} ** {num2}= {e}")
    return e

while True:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operation = input("Enter operation: ")[0].lower()
    result = 0
    if operation == 's':
        result = subtraction(num1,num2)
    elif operation == 'm':
        result = multiply(num1,num2)
    elif operation == 'd':
        result = divide(num1,num2)
    elif operation == 'a':
        result = addition(num1,num2)
    elif operation == 'e':
        result = exp(num1,num2)

    else:
        print(" something went wrong!")


    print ("The result is : ", result)

    choice = input("do you want to continue: ")[0].lower()
    if choice == 'n':
        print("Thank you for using this app.")
        print("History: ", history)
        break


