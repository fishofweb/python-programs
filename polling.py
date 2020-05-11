print("Welcome to the Yes or No Issue Polling App.")

issue = input("What is the YES or NO issue you will be voting: ")

no_of_votes = int(input("What is the number of voters you will allow on the issue: "))

password = input("Enter a password for polling results: ")

voters = []
votes = []
# my_dict={issue:voters}
for c in range(no_of_votes):
    name = input("What is your name: ").title().strip()
    if name in voters:
        print("Someone with the same name has already casted the vote")
        continue
    print("here is the issue: ", issue)
    opinion = input("What do you think...yes or no: ")
    if (opinion != 'yes') and (opinion != 'no'):
        print("Type either yes or no",opinion+" is not an option, anyways your opinion is recorded but it won't count")
    voters.append(name)
    votes.append(opinion)
    print("\nThank you",name+"!","Your vote has been recorded")

print("\n")

print("The following",len(voters),"people voted:")

for z in voters:
    print("\t\t",z)


print("On the following issue: ",issue)

yes = votes.count('yes')
no = votes.count('no')

if yes > no :
    print("yes wins!",yes,"votes to",no)

if no > yes:
    print("no wins!",no,"votes to",yes)

if yes == no:
    print("it was a tie! both are",yes)
my_dict={}
for x,y in zip(voters,votes):
    my_dict.update({x : y})

for i in range(2):
    result_pwd = input("To see the results enter the admin password: ")
    if result_pwd == password:
        for k,v in my_dict.items():
            print("Voter:",k,"\t\tVote:",v)
        break

    else:
        print("incorrect password")
