"""
Build a text-based role-playing game that has at least 2 classes:

a Hero() class
an Opponent() class

The Hero should encounter multiple Opponents of different strengths (or levels)
and be able to perform different actions in regards to them - at a minimum:

- attack
- run away

If the Hero chooses to attack, the program decides through a simulated dice
throw that takes the current level into account, whether the Hero or the
Opponent wins this round.

Implement consequences for winning and losing, e.g. forcing the Hero to wait a
few seconds before continuing the game in case they lose, or removing the
Opponent from the Opponent pool in case the Hero wins.
"""

import random


class Hero:
    """Represents the role of a hero.

        ...

    Attributes
    ----------
    name : str
        name of the hero
    level : int
        current level of the hero
    health : int
        health score (0 - 100)

    Methods
    -------
    attack(opponent)
        If the Hero chooses to attack, the program decides through a simulated dice throw that takes the current level into account, whether the Hero or the Opponent wins this round
    run_away(direction)
        If the Hero runs away, nothing happens
    """

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100

    def attack(self, opponent):
        print(
            f"An enemy {attacker.name} (level {attacker.level}) is attacking you!")
        while self.health > 0 and opponent.health > 0:
            entry = input("Stay and fight (f) or run away (r)? ")
            if entry == "f":
                dice_roll_1 = random.randint(1, 6)
                dice_roll_2 = random.randint(1, 6)
                dice_roll = dice_roll_1 + dice_roll_2
                attack_score = dice_roll + self.level
                defend_score = 6 + opponent.level  # attacker has slight advantage
                if attack_score >= defend_score:
                    print('The hero lands a blow!')
                    opponent.health -= 25
                if attack_score < defend_score:
                    print('The monster strikes!')
                    self.health -= 25
                print(
                    f'{self.name} health: {self.health} | {opponent.name} health: {opponent.health}\n')
            if entry == "r":
                self.run_away()
                break
        # Fighting ends
        if opponent.health <= 0:
            print('The hero wins and levels up! Your health is restored.')
            self.level += 1
            self.health = 100
            print(f'{self.name} level: {self.level}\n')
            monsters.remove(attacker)
        if self.health <= 0:
            print('The monster wins!')

    def run_away(self):
        dice_roll = random.randint(1, 6)
        if dice_roll > 3:
            print('The monster hits you in the back as you ran away, ouch!\n')
            self.health -= 5
        print('You ran away - phew!\n')


class Opponent(Hero):
    """Represents the role of an opponent.

        ...

    Attributes
    ----------
    name : str
        name of the opponent
    level : int
        current level of the opponent
    health : int
        health score (0 - 100)

    Methods
    -------


    """

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 100


# GAMEPLAY
game_on = True
print('WELCOME TO HEROS VS MONSTERS\n')
while game_on:
    # Hero setup
    name = input("What is the name of your character? ")
    hero = Hero(name)

    # Monster setup
    goblin = Opponent("Goblin", 1)
    ogre = Opponent("Ogre", 2)
    troll = Opponent("Troll", 3)
    minotaur = Opponent("Minotaur", 4)
    giant_squid = Opponent("Giant Squid", 5)
    monsters = [goblin, ogre, troll, minotaur, giant_squid]

    # Encounters
    while hero.health > 0:
        try:
            attacker = random.choice(monsters)
            hero.attack(attacker)
        except IndexError:
            print("You have won HEROS VS MONSTERS - CONGRATULATIONS!\n")
            game_on = False
            break
    if hero.health <= 0:
        entry = input(
            "You have died and the game has ended. Play again? (Y/N)? ")
        if entry == 'N':
            game_on = False
