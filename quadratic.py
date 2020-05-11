import cmath
print("Welcome to the Quadratic Solver App.")
print("\n")
print("A quadratic equation is of the form ax^2 + bx + c = 0")

print("Your solutions can be real or complex numbers.")

print("A complex number has two parts: a + bj")

print("Where a is the real portion and bj is the imaginary portion.")
print("\n")
num_ = int(input("How many equations would you like to solve today: "))

# number_of_equations = []
# number_of_equations.append(num_)
print("\n\n")
for i in range(1,num_+1):
    print("Solving equation#",i)
    print("------------------------------------------------------------------")
    print("\n")
    a = int(input("Please Enter your value of a (coefficient of x^2): "))
    b = int(input("Please Enter your value of b (coefficient of x): "))
    c = int(input("Please Enter your value of c (coefficient): "))

    print("\n")

    print("The solutions to",str(a)+"x^2 +",str(b)+"x +",str(c))
    print("\n")
    math_ = cmath.sqrt((b**2)-(4*a*c))
    positive= (-b + math_)/2*a
    negative= (-b - math_)/2*a

    print("x1:",positive)
    print("x2:",negative)

    print("\n\n")
print("Thank you for using this app :)")
