print("Welcome to blackjack game")
import random
player = []
c1 = []
c2 = []
c3 = []
c4 = []
cards = ['king', 'queen', 'joker', 'ace']
def players_values():
    player.append(random.randint(1, 9))
    player.append(random.choice(cards))

    c1.append(random.randint(1, 9))
    c1.append(random.choice(cards))

    c2.append(random.randint(1, 9))
    c2.append(random.choice(cards))

    c3.append(random.randint(1, 9))
    c3.append(random.choice(cards))

    c4.append(random.randint(1, 9))
    c4.append(random.choice(cards))
    return player,c1,c2,c3,c4
class blackjack():
    def __init__(self, player, c1,c2,c3,c4):
        self.player = player
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        print(self.player)
        print(self.c1)
        print(self.c2)
        print(self.c3)
        print(self.c4)

        if player[1] == 'ace':
            player.pop()
            player.append(11)
        elif player[1] != 'ace':
            player.pop()
            player.append(10)

        else:
            print("player error")

        if c1[1] == 'ace':
            c1.pop()
            c1.append(11)
        elif c1[1] != 'ace':
            c1.pop()
            c1.append(10)

        else:
            print("c1 error")

        if c2[1] == 'ace':
            c2.pop()
            c2.append(11)
        elif c2[1] != 'ace':
            c2.pop()
            c2.append(10)

        else:
            print("c2 error")

        if c3[1] == 'ace':
            c3.pop()
            c3.append(11)
        elif c3[1] != 'ace':
            c3.pop()
            c3.append(10)

        else:
            print("c3 error")

        if c4[1] == 'ace':
            c4.pop()
            c4.append(11)
        elif c4[1] != 'ace':
            c4.pop()
            c4.append(10)

        else:
            print("c4 error")

        if player[0] + player[1] == 20:
            print("player wins")
        elif c1[0] + c1[1] == 20:
            print("C1 wins")

        elif c2[0] + c2[1] == 20:
            print("C2 wins")

        elif c3[0] + c3[1] == 20:
            print("c3 wins")

        elif c4[0] + c4[1] == 20:
            print("c4 wins")

        else:
            print("Nobody won")


players_values()

blackj = blackjack(player,c1,c2,c3,c4)