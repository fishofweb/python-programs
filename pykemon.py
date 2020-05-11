import random
class Pykemon():
    def __init__(self ,name, element, health, speed):
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health

        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        damage = random.randint(15,25)
        print("Pykemon "+ self.name + " used "+ self.moves[0]+ ".")
        print("it dealt "+ str(damage)+ " damage.")
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        damage = random.randint(0, 50)
        print("Pykemon " + self.name + " used " + self.moves[1] + ".")

        if damage < 10:
            print("The attack missed")
        else:
            print("it dealt " + str(damage) + " damage.")

        enemy.current_health -= damage

    def restore(self):
        heal = random.randint(15, 25)
        print("Pykemon "+ self.name+ " used "+ self.moves[2]+ ".")
        self.current_health += heal

        if self.current_health > self.max_health:
            self.current_health = self.max_health
    def faint(self):
        if self.current_health <=0:
            self.is_alive = False
            print("Pykemon "+ self.name + " has fainted!")
            input("press enter to continue....")
    def show_stats(self):
        print("\nName: ", self.name)
        print("Element Type: ", str(self.current_health), " / ", str(self.max_health))
        print("Speed: "+ str(self.speed))
