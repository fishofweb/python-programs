

while True:
    number = int(input("Enter number: "))
    number_list = list(range(1, number))
    factors = []
    print("Factors of",number,"are:")

    for n in number_list:
        if number%n == 0:
            print(n)
            factors.append(n)

    print("in summary: ")
    # for b in range(int(len(factors))):
    #     print(factors[b])

    for c in range(int(len(factors)/2)):
        print(factors[c],"*",factors[-c-1],"=",factors[c]*factors[-c-1])

    choice = input("do you want to quit(y/n): ")

    if choice == 'y':
        quit()

    for b in range(int(len(factors))):
        print(factors[-b-1])