print("Welcome to the bank app.")
amt =0

def name(n):
    if n == 'david':
        return True
    else:
        return False

def savings(other=0,opr='add', present=500):
    if opr == 'add':
        total = present + other
    else:
        total = present - other
    if total<0:
        return "Your acount is going negative"
    else:
        return total


def current(other=0,opr='add',present=500):
    print(opr)
    if opr == 'add':
        total = present + other
    else:
        total = present - other
    if total<0:
        return "Your acount is going negative"
    else:

        return total

while True:
    name_ = input("What is your name: ").lower().strip()
    authorized = name(name_)
    while authorized:
        print("Account summary: \n")
        print("Current Account Balance: ", current())
        print("Savings Account Balance: ", savings())

        input("press enter to continue...")

        account = input(f"Hi {name_}! Which account you want to work with today:").lower().strip()
        if account == 'current':
            update = input("Do you want to deposit or withdraw an amount: ")
            if update == 'deposit':
                amt = int(input("Enter amount : "))
                total_amt = current(amt)
                break
            if update == 'withdraw':
                amt = int(input("Enter amount : "))
                total_amt = current(amt,'subtract')
                break

        if account == 'savings':
            update = input("Do you want to deposit or withdraw an amount: ")
            if update == 'deposit':
                amt = int(input("Enter amount : "))
                total_amt = current(amt)
                break
            if update == 'withdraw':
                amt = int(input("Enter amount : "))
                total_amt = current(amt,'subtract')
                break


    cont = input("Do you want to continue: ")
    if cont[0]=='n':
        print("Summary: ")
        print("Savings : ",savings(amt))
        print("Current : ", current(amt))
        break