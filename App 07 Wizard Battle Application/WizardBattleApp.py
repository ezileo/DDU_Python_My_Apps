# Author: Rohit Gupta
# Date: January 31, 2017
# Version: 1.0

import datetime
import random
import actors



def main():
    print_the_header()
    print("\n" + "!!!!!!!!!!!!!!Hello from the Main!!!!!!!!!!!!!!!!!!!!!!!" + "\n")
    game_loop()


def print_the_header():
    print("----------------------------------------")
    print("          THE WIZARD APPLICATION        ")
    print("----------------------------------------")
    print("")
    user_name = input("Player please input your name: ")
    print("Welcome to the game {}".format(user_name))
    now = datetime.datetime.now()
    print("Current Time is " + (now.strftime("%A, %d  %B  %Y")))


def game_loop():
    creatures = [
        Creature("Toad", 1),
        Creature("Tiger", 12),
        Creature("Bat", 3),
        Creature("Dragon", 50),
        Creature("Evil Wizard", 1000),
    ]

    print(creatures)

    hero = Wizards("Gandalf", 75)
    print(hero)

    while True:
        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared from the Dark Forest".format(active_creature.name, active_creature.level))
        print()

        cmd = input("Do you want to [a]ttack, [r]un away or [l]ook around: ")
        if cmd == "a":
            print("Attack")
        elif cmd == "r":
            print("Running Away!!")
        elif cmd == "l":
            print("Look Around!!")
        else:
            print("OK, Exiting the game. Have a nice day ahead!!!")
            break


if __name__ == '__main__':
    main()
