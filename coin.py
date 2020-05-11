import random

print("Welcome to coin flipping app.")
print(random.randint(1, 2))

print("I will flip a coin a set number of times.\n")

number = int(input("How many times would you like me to flip the coin: "))

print("\n")

head = []
tail = []

for c in range(number):
    coin = random.randint(1, 2)
    if coin == 1:
        head.append(coin)
        print("Head")

        if len(head)%10 == 0:
            print("At "+ str(c) + " flips. Number of ","tail is ",len(tail), "and head is",len(head))
        # elif number%2 !=0:
        #     if len(head)==len(head)-1:
        #         print("head is ", len(head))


    else:
        tail.append(coin)
        print("tail")

        if len(tail)% 10 ==0 :
            print("At "+ str(c) + " flips. Number of ","tail is ",len(tail), "and head is",len(head))


print("Results of flipping a coin 500 times:\n")

print("Side\t\tCount\t\tPercentage")
print("Heads\t\t"+str(head.count(1))+"/"+str(number)+"\t\t"+str((head.count(1)/number) * 100))

print("Tail\t\t"+str(tail.count(2))+"/"+str(number)+"\t\t"+str((tail.count(2)/number) * 100))