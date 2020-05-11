print("Welcome to the Basketball Roster Program")

point_guard = input("Who is your point guard: ").title().strip()
shooting_guard = input("Who is your shooting guard: ").title().strip()
small_forward = input("Who is your small forward: ").title().strip()
power_forward = input("Who is your power forward: ").title().strip()
center = input("Who is your center: ").title().strip()

players = [point_guard,shooting_guard,small_forward,power_forward,center]
print("\t\t\tYour starting 5 for the upcoming basketball season\n")
print("\t\t\t\t\t\tPoint Guard:","\t\t\t",point_guard)
print("\t\t\t\t\t\tShooting Guard:","\t\t\t",shooting_guard)
print("\t\t\t\t\t\tSmall Forward:","\t\t\t",small_forward)
print("\t\t\t\t\t\tPower Forward:","\t\t\t",power_forward)
print("\t\t\t\t\t\tCenter:","\t\t\t",center)

players.remove(small_forward)
print("Oh no, wait....",small_forward,"is not a good player , you will lose because of him, kindly replace him as soon as possible.  Thank you!")
print("Your roster has",len(players),"players.")
new_player= input(f"who will take {small_forward} spot: ")
players.append(new_player)

print("\t\t\tYour new 5 players for the upcoming basketball season\n")
print("\t\t\t\t\t\tPoint Guard:","\t\t\t",point_guard)
print("\t\t\t\t\t\tShooting Guard:","\t\t\t",shooting_guard)
print("\t\t\t\t\t\tSmall Forward:","\t\t\t",new_player)
print("\t\t\t\t\t\tPower Forward:","\t\t\t",power_forward)
print("\t\t\t\t\t\tCenter:","\t\t\t",center)


print("Good Luck", new_player,"you will do great!")
print("your new roster has", len(players),"players.")


