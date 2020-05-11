import time
print("Welcome prime number calculator App.")

while True:
    number1 = input("If you want to see  just one number, press 1 if you see prime numbers in range , press 2:")

    while True:
        if number1 == '1':
            num1 = int(input("enter the number: \n"))
            if num1 % 2 == 0:
                print(" it's not prime.")
                break
            elif num1 % 3 == 0 and num1 != 3 and num1 != 1:
                print("It's not prime.")
                break
            elif num1 == 1 or num1 == 3 or num1 % 3 != 0:
                print("it is prime")
                break

        elif number1 == '2':
            start_time = time.time()
            start = int(input("Starting range: "))
            stop = int(input("Ending range: "))
            numberList = list(range(start,stop+1))
            prime=[]
            # print(numberList)
            for c in range(len(numberList)+1):
                # print(c)
                if c % 2 == 0:
                    continue
                if int(c) == 1 or int(c) == 3 or int(c) % 3 != 0:
                    prime.append(c)
                    #break
                else:
                    continue
            end_time = time.time()
            total_time = end_time - start_time
            print("start time:",start_time)
            print("end time: ", end_time)
            print("Time taken: ",total_time)
            print(prime)
        else:
            print("unexpected behavior")


        more = input("do you want to continue.(y/n)\n")
        if more != 'y':
            print("thank you for using this app.")
            quit()



