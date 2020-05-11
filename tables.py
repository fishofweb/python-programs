welcome = input("Hi.. what's your name buddy: ")
number = float(input(welcome + " enter your number :"))


for n in range(1,10):
    # product = n*number
    print(n, "*", number,"=",round(n*number,2),"\n\n\n" )
    print(f"{number}**{n} = {round(number**n, 2)}")

print(welcome + ", Hey Math is cool !!!!!!! \n ")

print(welcome, "you are awesome buddy!!!!!!!!!!!!!!!")