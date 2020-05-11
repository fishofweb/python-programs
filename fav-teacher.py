print("This is a favourite teacher app")
print()
fav = []
teacher = input("who's your first favourite teacher: ")
fav.append(teacher)
teacher = input("who's your second favourite teacher: ")
fav.append(teacher)
teacher = input("who's your third favourite teacher: ")
fav.append(teacher)
teacher = input("who's your fourth favourite teacher: ")
fav.append(teacher)

print("Your favourite teachers ranked: ", fav)

print("Your favourite teachers alphabetically are:",sorted(fav))

print("Your favourite teachers in reverse alphabetical order are: ",sorted(fav,reverse=True))

print("Your top two teachers are:", fav[0], "and", fav[1])

print("Your next two teachers are: ", fav[2], "and", fav[3])

print("Your last favourite is :", fav[-1])

print("You have a total of", len(fav),"favourite teachers")

new_fav=input("Oops,"+fav[0]+" is no longer your first favourite teacher."+"Who is your new favourite teacher: ")

fav.insert(0,new_fav)

print("Your favourite teachers ranked: ", fav)

print("Your favourite teachers alphabetically are:",sorted(fav))

print("Your favourite teachers in reverse alphabetical order are: ",sorted(fav,reverse=True))

print("Your top two teachers are:", fav[0], "and", fav[1])

print("Your next two teachers are: ", fav[2], "and", fav[3])

print("Your last favourite is :", fav[-1])

print("You have a total of", len(fav),"favourite teachers")


rm_teacher = input("You've decided you no longer like a teacher. Which teacher would you like to remove from your list: ")

fav.remove(rm_teacher)

print("Your favourite teachers ranked: ", fav)

print("Your favourite teachers alphabetically are:",sorted(fav))

print("Your favourite teachers in reverse alphabetical order are: ",sorted(fav,reverse=True))

print("Your top two teachers are:", fav[0], "and", fav[1])

print("Your next two teachers are: ", fav[2], "and", fav[3])

print("Your last favourite is :", fav[-1])

print("You have a total of", len(fav),"favourite teachers")











