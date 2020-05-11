print("Welcome to the even and odd app.")

while True:
    even = []
    odd = []
    numbers = input("Enter numbers: ")
    number_list = numbers.split(",")
    for c in number_list:
        if int(c)%2 == 0:
            even.append(c)
        else:
            odd.append(c)

    print("Even: ",even)
    print("Odd: ", odd)


    choice = input("Do you want to continue: ")

    if choice != 'y':
        break


print("Thank you for using this app.")


