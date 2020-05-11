import math
print("Welcome , i'm computing hypotenueus and area of the right triagle")
a = float(input("enter first leg: "))
b = float(input("enter second leg: "))

hypotenuous = round(math.sqrt((a*a) + (b * b)),3)

area = (a*b)/2
area = round(area,3)
print("Hypotenuese is :", hypotenuous)

print(f"Area of a right triagle is {area}")