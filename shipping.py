print("Welcome to the shipping accpounts Program")

name = input("Hello, what is your username: ").title().strip()

print("\nHello",name,". Welcome back to your account.\n")
print("Current Shipping Prices are as follows:\n")

z_to_100 = 5.10
h_to_500 = 5.00

f_to_1000 = 4.95

over_1000= 4.80

print("Shipping orders 0 to 100:\t\t","$"+str(z_to_100),"each")
print("Shipping orders 100 to 500:\t\t","$"+str(h_to_500),"each")
print("Shipping orders 500 to 1000:\t\t","$"+str(f_to_1000),"each")
print("Shipping orders over 1000:\t\t","$"+str(over_1000),"each")

order = int(input("How many items would you like to ship: "))

print("\n")

if order > 0 and order <= 100:
    print(f"To ship {order} items it will cost you ${round(order*z_to_100,2)} at ${z_to_100} per item.")

elif order > 100 and order <= 500:
    print(f"To ship {order} items it will cost you ${round(order*h_to_500,2)} at ${h_to_500} per item.")

elif order > 500 and order <= 1000:
    print(f"To ship {order} items it will cost you ${round(order*f_to_1000,2)} at ${f_to_1000} per item.")

elif order > 1000:
    print(f"To ship {order} items it will cost you ${round(order*over_1000,2)} at ${over_1000} per item.")

else:
    print("type appropriate entry")
    quit()
print("\n")

confirm = input("would you like to place this order (y/n):\t").lower().strip()

if confirm == 'y':
    print("Okay.\tShipping your",order,"items.\n")

elif confirm == 'n':
    print("Okay.\tno order is being placed at this time.\n")

else:
    print("Whats wrong with you.. i said type either y or n. \n")

