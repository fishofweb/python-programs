print("Welcome to tick cross game.")

def blue_print():
    print("\t\t------------------")
    print("\t\t|1|\t2|\t3|")
    print("\t\t------------------")
    print("\t\t|4|\t5|\t6|")
    print("\t\t------------------")
    print("\t\t|7|\t8|\t9|")
    print("\t\t------------------")

def game(row1,turn, mark):


    for item in range(len(row1)):
        if item == int(turn)-1:
            row1.pop(item)
            row1.insert(int(turn)-1, mark)

    print(row1)
    print("\t\t------------------")

    print(f"\t\t|{row1[0]}|\t {row1[1]}|\t{row1[2]}|")
    print("\t\t------------------")

    print(f"\t\t|{row1[3]}|\t {row1[4]}|\t{row1[5]}|")
    print("\t\t------------------")

    print(f"\t\t|{row1[6]}|\t {row1[7]}|\t{row1[8]}|")
    print("\t\t------------------")

def result(row1):
    if row1[0] == 'X' and row1[1]== 'X' and row1[2]=='X':
        return "player 1 wins!"
    elif row1[3] == 'X' and row1[4]== 'X' and row1[5]=='X':
        return "player 1 wins!"

    elif row1[6] == 'X' and row1[7]== 'X' and row1[8]=='X':
        return "player 1 wins!"
    elif row1[0] == 'X' and row1[3] == 'X' and row1[6] == 'X':
        return "player 1 wins!"

    elif row1[1] == 'X' and row1[4] == 'X' and row1[7] == 'X':
        return "player 1 wins!"
    elif row1[2] == 'X' and row1[5] == 'X' and row1[8] == 'X':
        return "player 1 wins!"
    elif row1[0] == 'X' and row1[4] == 'X' and row1[8] == 'X':
        return "player 1 wins!"

    elif row1[2] == 'X' and row1[4] == 'X' and row1[6] == 'X':
        return "player 1 wins!"

    elif row1[0] == 'O' and row1[1]== 'O' and row1[2]=='O':
        return "player 2 wins!"
    elif row1[3] == 'O' and row1[4]== 'O' and row1[5]=='O':
        return "player 2 wins!"

    elif row1[6] == 'O' and row1[7]== 'O' and row1[8]=='O':
        return "player 2 wins!"
    elif row1[0] == 'O' and row1[3] == 'O' and row1[6] == 'O':
        return "player 2 wins!"

    elif row1[1] == 'O' and row1[4] == 'O' and row1[7] == 'O':
        return "player 2 wins!"
    elif row1[2] == 'O' and row1[5] == 'O' and row1[8] == 'O':
        return "player 2 wins!"
    elif row1[0] == 'O' and row1[4] == 'O' and row1[8] == 'O':
        return "player 2 wins!"

    elif row1[2] == 'O' and row1[4] == 'O' and row1[6] == 'O':
        return "player 2 wins!"

    else:
        return "DRAW"

again = True
while again:
    blue_print()

    row1 = [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]
    start = 1
    while start < 9:
        mark = 'X'
        while True:
            player1 = int(input(" X : your turn: "))
            # check = row1.index(player1 - 1)
            # if row1[check] == "X" or row1[check] == "O":
            #     print("This place is already filled")
            #     continue
            if row1[player1-1] != " ":
                print("Entry is already filled")
                continue
            game(row1,player1, mark)
            if game == "foul":
                continue
            else:
                break
        outcome = result(row1)

        if outcome == "player 1 wins!":
            print(outcome)
            break
        if outcome == "player 2 wins!":
            print(outcome)
            break

        mark = 'O'
        while True:
            player2 = int(input("O : your turn: "))
            if row1[player2-1] != " ":
                print("Entry is already filled")
                continue
            game(row1,player2, mark)
            if game == "foul":
                continue
            else:
                break

        outcome = result(row1)

        if outcome == "player 1 wins!":
            print(outcome)
            break
        if outcome == "player 2 wins!":
            print(outcome)
            break

        start += 1


    if outcome == "DRAW":
        print(outcome)

    choice = input("Do you want to continue?")
    if choice == 'n':
        again = False



