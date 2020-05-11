import time

localtime = time.asctime( time.localtime(time.time()) )

print("Welcome to grocery list App\nCurrent Date and Time: ",localtime)
grocery= ['meat','chease']
print("you have meat and chease currently in your list")

item1= input("Type of food to add to the grocery list: ").lower().strip()
item2= input("Type of food to add to the grocery list: ").lower().strip()
item3= input("Type of food to add to the grocery list: ").lower().strip()

grocery.append(item1)
grocery.append(item2)
grocery.append(item3)
print("here is your grocery list:", str(len(grocery))+ " items")
print("\n", grocery)
grocery.sort()
print("\nhere is your grocery list sorted\n",grocery)

print("simulating grocery shopping...\n")

print("current grocery list", len(grocery), "items")

buy1 = input("what did you just buy: ").lower().strip()
grocery.remove(buy1)

print(f"Removing {buy1} from list....")

print("\nCurrent grocery list:", len(grocery))
print("\n",grocery)

buy2 = input("what you bought now: ").lower().strip()
print("Removing ", buy2, "from list....\n")
grocery.remove(buy2)


buy3 = input("did you just buy something  : ").lower().strip()
print("Removing ", buy3, "from list....\n")
grocery.remove(buy3)


print("current grocery list:", len(grocery))

print("\n", grocery)
out_of_stock = grocery.pop()
print("Sorry, the store is out of", out_of_stock)

buy4 = input("what would you buy intead: ")
grocery.insert(1,buy4)

print("here is what remains on your grocery list: \n")
print(grocery)


