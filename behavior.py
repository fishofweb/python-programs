import random

class mashun():
    def __init__(self, name):
        self.name = name
        print("Hello I am ", self.name, "Let's see how's my mood today...!\n")
        self.hunger1 = random.randint(1,10)
        self.boredom1 = random.randint(1, 10)
        self.happy1 = random.randint(1, 10)
        self.excitement1 = random.randint(1, 10)



    def hungry(self):
        # hunger = random.randint(1,10)
        print("Henger level: ", self.hunger1)
        if self.hunger1 == 10:
            print("I am too much hungry .... make me something pleeeeeeeezzzzzzzz")



    def boredom(self):
        # boredom = random.randint(1,10)
        print("Boredom level: ",self.boredom1)
        if self.boredom1 == 10:
            print("I am too much bored .... i dont know what to do......uuugghghhghghhghghh")


    def happy(self):
        # happy = random.randint(1,10)
        print("Happiness level: ",self.happy1)
        if self.happy1 == 10:
            print(" HAHAHAHAHAHHAH.... I AM tooo muuuuch haaapappapappyyyyyy")

    def excitement(self):
        # excitement = random.randint(1,10)
        print("Excitement level: ",self.excitement1)
        if self.excitement1 == 10:
            print("EXCITED TODAY ...... I am going for a hike ..... hahahahahahhahahaahhahahahahahahahh Yayyyyyyyyyyyyy")



while True:
    print("\n\nHey !!! its a new Day")

    Mashun = mashun("Roshaan")
    Mashun.hungry()
    Mashun.excitement()
    Mashun.boredom()
    Mashun.happy()
    input("Press enter for next day...!")