print("Welcomr to the frequency analysis App.\n")

for times in range(2):
    phrase = input("Enter a word or phrase: "+ str(times+1)+" ")
    my_list = list(phrase)
    # print(my_list)
    words = {}
    a=ord('a')
    for i in range(a,a+26):
        if my_list.count(chr(i)) != 0:
            words[chr(i)]= my_list.count(chr(i))



    occurence = list(words.values())
    keys = list(words.keys())
    # print(keys)

    occurence.sort(reverse=True)
    letter_set = []
    print("\tLetter\t\tOccurrence\t\tPercentage")
    for k,v in words.items():
        print("\t"+ k+  "\t\t"  +    str(v)  +"\t\t\t" + str(round((v/len(my_list))*100)) + "%")

    print("letters ordered from highest to lowest: ", end="")
    for i in occurence:
        for k,v in words.items():
            if i == v:
                if k not in letter_set:
                    letter_set.append(k)

    for c in range(len(letter_set)):
        print(str(letter_set[c]), end="")


    print("\n\n")