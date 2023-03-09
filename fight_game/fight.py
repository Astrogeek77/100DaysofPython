import random
import math


class Warrior:
    __attack_power = 0
    __block_power = 0
    health = 0
    name = ""

    def __init__(self, name, health, attack_power, block_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.block_power = block_power

    def handleAttack(self):
        # return random.randint(1, 1000) % self.attack_power
        return random.randint(1, self.attack_power)

    def handleBlock(self):
        # return random.randint(1, 1000) % self.block_power
        return random.randint(1, self.block_power)

    def __del__(self):
        print(f"Warrior {self.name} has been destroyed")


class Battle:
    def __init__(self, warrior1, warrior2):
        self.start_fight(warrior1, warrior2)

    @staticmethod
    def start_fight(warrior1, warrior2):
        while True:
            if (Battle.getAttackResult(warrior1, warrior2) == "Game Over"):
                print("Game Over\n")
                break

            if (Battle.getAttackResult(warrior2, warrior1) == "Game Over"):
                print("Game Over\n")
                break

    @staticmethod
    def getAttackResult(warrior1, warrior2):
        warrior1AttackAmt = warrior1.handleAttack()
        warrior2BlockAmt = warrior2.handleBlock()

        damagetoWarrior2 = math.ceil(warrior1AttackAmt - warrior2BlockAmt)
        if (damagetoWarrior2 < 0):
            damagetoWarrior2 = 0
        # damagetoWarrior2 = 0 if damagetoWarrior2 < 0 else damagetoWarrior2
        warrior2.health = warrior2.health - damagetoWarrior2

        print(
            f"{warrior1.name} attacks {warrior2.name} and deals {damagetoWarrior2} damage.")
        print(f"{warrior2.name} is down to {warrior2.health} health.")

        if (warrior2.health <= 0):
            print(
                f"\nResult: {warrior2.name} has Died and {warrior1.name} is Victorious\n")
            return "Game Over"
        else:
            return "Fight Again"


batman = Warrior("Batman", 180, 35, 35)
superman = Warrior("Superman", 185, 30, 40)

Battle.start_fight(batman, superman)
