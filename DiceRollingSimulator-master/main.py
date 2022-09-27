import random as rand
import time as t

print("Welcome to dice rolling!")
print("Would you like to roll one die at a time, or would you like to roll 2 dice at a time?")
print("Answer \"1\" for the first option.\nAnswer \"2\" for the second option.")
choice = int(input("Your choice: "))


def singledie():
    print("How many dice would you like to roll?\n")
    dicenum = int(input("Your choice: "))
    die = 0

    print(f"Alright.. {dicenum} it is.")
    t.sleep(0.7)
    print("Rolling...")

    for i in range(dicenum):
        die += 1
        t.sleep(1)
        print(f"die number {die}: {rand.randint(1, 6)}")


def doubledice():
    print("How many pairs of dice would you like to roll?")
    dicenumb = int(input("Your choice: "))
    dice = 0

    print(f"Alright.. {dicenumb} it is.")
    t.sleep(0.7)
    print("Rolling...")

    for j in range(dicenumb):
        dice += 1
        t.sleep(1)
        print(f"dice number {dice}: {rand.randint(1, 6)} and {rand.randint(1, 6)}")


if choice == 1:
    singledie()
elif choice == 2:
    doubledice()
else:
    print("That isn't a choice!")
