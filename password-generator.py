import string
import random

if __name__ == "__main__":
    print("This is a password generator app\n")
    input("\n\nPress enter to continue....")
    string1 = string.ascii_lowercase
    

    string2 = string.ascii_uppercase
    

    string3 = string.digits

    string4 = string.punctuation

    

    passwordLength = input("Enter password's length: ")
    
    
    passwordLength = int(passwordLength)

    join_str = string1+string2+string3+string4
    list_ = []
    for i in range(len(join_str)):
        list_.append(join_str[i])



    random.shuffle(list_)
    your_password = ""
    for r in range(passwordLength):
        your_password += str(list_[r])

    print("Your system generated password is ===>>> ",your_password)

