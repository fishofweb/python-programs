import math
print("Welcome to the Factorial Calculator App.")
print("\n")
number_=int(input("What number would you like to comput the factorial of? "))
lst=[]
for i in range(0,number_+1):
    lst.append(i)
    lst.append("*")
lst.pop()
# lst.pop(0)
# lst.pop(0)
# print(lst)


print(str(number_)+"! = ", end="")
for i in lst[2:]:
    print(i,end="")
print("\n")
print("Here is the result from math library: ",math.factorial(number_))


fact =1
for c in range(1,number_+1):
    fact = fact * c
print("Here is the result from my own algorithm: ", fact)

print("\n")

print("it is shown twice that",str(number_)+"! = ", str(fact), "(with excitement)")

