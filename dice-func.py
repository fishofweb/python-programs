print("Welcome to dice app.")
import random
def dice(number, times):
    lst = []
    for c in range(0, times):
        p = random.randint(0, number)
        lst.append(p)

    return lst



while True:
    number = int(input("higest number:"))
    times = int(input("Times:"))

    deck = dice(number, times)

    for v in deck:
        print(v)


    cont= input("Do you want to continue: ")
    if cont == 'n':
        break


print("Thank you for using this app.!")