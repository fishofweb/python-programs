import random
print("Welcome to a game of Rock-Paper-Scissors")

rounds = int(input("How many rounds would you like to play: "))
player = 0
computer =0
comp_list= ['Rock','Paper','Scissors']
for c in range(rounds):
    print("\n")
    print("Round",c+1)
    print("Player:", player,"\t\tComputer: ", computer)
    choice=input("Time to pick...Rock-paper-scissors: ").title().strip()


    list_number = random.randint(0, 2)
    print("\n")
    comp_choice = comp_list[list_number]
    print("Computer:",comp_choice)

    print("Player:",choice)
    if choice in comp_list:
        if choice == comp_choice:
            print("It's a tie, how boring!\nthis round was a tie.")

        elif comp_list.index(choice) >comp_list.index(comp_choice):
            print("You win ")
            player += 1

        elif comp_list.index(choice) < comp_list.index(comp_choice):
            print("Lost")
            computer += 1

    elif choice not in comp_list:
        print("Unexpected choice\n")
        print("that's not a valid option. Computer gets a point")
        computer += 1

    else:
        print("some thing went wrong")

