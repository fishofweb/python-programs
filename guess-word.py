print("Welcome to word guessing App.")

import random

# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)
#
# print(mylist)

my_dict = {
    "Commodities" : ['oil', 'coal', 'Gold'],
    "countries": ['Pakistan', " Turkey", "Malaysia"],
    "OS": ['Windows','Linux','Android'],
}

key_list = []
value_list = []

for k,v in my_dict.items():
    key_list.append(k)
    value_list.append(v)

# print(key_list)
# print("\n")
# print(value_list)
while True:
    random_ = random.randint(0,len(key_list)-1)

    current_key = key_list[random_]
        # print(current_key)

    current_value_list = value_list[random_]

        # print(current_value_list)

    random_word_value = random.randint(0,len(current_value_list)-1)

    word = current_value_list[random_word_value]
    hint_list = []

    print("Guess",len(word),"Charactors word from category:",current_key)

    for n in range(len(word)):

        # for c in range(len(word)):
        hint_list.append('-')
        print("-", end="")

    print("\n\n")
    while True:

        guess_count =0
        guess = input("Enter your Guess: ").title().strip()
        if guess == word:
            guess_count += 1
            print("Correct! You Guessed the word in",guess_count,"Number of guess")
            break
        else:
            guess_count += 1
            print("Thats incorrect :( \n")
            hint_ = random.randint(0,len(word)-1)
            hint_list[hint_]=word[hint_]
            for m in hint_list:
                print(m,end="")
            print("\n")


    choice=input("Do you want to continue?")
    if choice == 'no':
        break

