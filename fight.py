class character():
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves
        self.life = 10
    def speed(self, s):
        s += 5

    def life(self, move):
        if punch == True:
            self.life -= 1
            print("JIN's LIFE:", self.life)
        if kick == True:
            self.life -= 2
            print("PAUL's LIFE", self.life)

class jin(character):
    def __init__(self, name , moves):
        super().__init__(name, moves)
        self.speed = 10
        self.life = 20
    def kick(self):
        kick = True
        print("Jin is on fire... kick... another kick.....another kick .....The damage is done...")
        # paul.life(kick)
    def life(self):
        self.life -= 1
        print("JIN's LIFE:", self.life)
class paul(character):
    def __init__(self, name, moves):
        super().__init__(name, moves)
        self.speed = 10
        self.life = 20

    def punch(self):
        punch = True
        print("Power Punch.......")
        # jin.life(punch)

    def life(self):
        self.life -= 2
        print("PAUL's LIFE", self.life)


jin = jin("JIN", 1)
paul = paul("PAUL", 1)


import random
number = 1
while True:
    print("Round : ", number)

    turn = random.randint(0,2)
    if turn == 0:
        kick = True
        jin.kick()
        paul.life()

    elif turn == 1:
        punch = True
        paul.punch()
        jin.life()
    else:
        print("Blocked.....!!!!")

    number +=1
    if jin.life==0 or paul.life==0:
        break