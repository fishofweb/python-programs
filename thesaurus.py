print("Welcome to the Thesaurus App!\n")

print("Choose a word from the thesaurus and I will give you the synonym.\n")

my_dict = {"hot": ["warm", "fire"],
           "cold": ["chilly","cool"],
           "happy": ["content","glad"],
           "sad": ["gloomy","bad mood"],
            }

print("Here are the words in the thesaurus:")
for key in my_dict:
    print("\t\t- "+key)

word = input("What word would you like a synonym for: ").lower().strip()
if word not in my_dict.keys():
    print(word,"is not in thesaurus")
    quit()

for key,value in my_dict.items():
    if word == key:
        print("Synonym of", key, "is",value[0])


choice = input("Would you like to see the whole thesaurus (yes/no): ").lower().strip()

if choice == "yes":
    for k , v in my_dict.items():
        print("Synonyms of",k,"are:")
        for val in v:
            print("\t\t-"+val)

else:
    print("Thank you for using this app , Good Bye")
    quit()

print("Thank you for using this app , Good Bye")
