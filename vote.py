print("Welcome to the Voter Registration App.\n\n")
name = input("Please enter your name: ")

age = int(input("Please enter your age: "))
parties =["Republican","Democratic", "Independent", "Libertarian","Green"]
print("\n")

if age>=18:
    print("Congratulations",name,"You are old enough to register to vote")

    print("Here is a list of political parties to join.")
    for x in parties:
        print("-",x)

    print("\n")

    choice = input("Which party would you like to join: ").title().strip()

    if choice == 'Republican':
        print("Hey are you sure you want o join trump...!")

    elif choice == "Democratic":
        print("Obama is a nice man!")

    elif choice == "Independent":
        print("Independent needs to be confident....!")

    elif choice == "Green":
        print("Green....what a name...!")

    elif choice == "Libertarian":
        print("Green....what a name...!")
    else:
        print("Type correct name")

    if choice in parties:
        print("\n You have joined",choice,"Congrats! i hope you have made the right choice.... haha....just kidding ...enjoy!!!")

else:
    print("hey, You are too young buddy")