from random import choice
from time import sleep  # import
from os import name, system

sentences = [
    "As he entered the church he could hear the soft voice of someone whispering into a cell phone.", 
    "He stomped on his fruit loops and thus became a cereal killer.", 
    "The sky is clear; the stars are twinkling.", 
    "She tilted her head back and let whip cream stream into her mouth while taking a bath.", 
    "The llama couldn't resist trying the lemonade.", 
    "He learned the important lesson that a picnic at the beach on a windy day is a bad idea.", 
    "Shingle color was not something the couple had ever talked about.", 
    "The external scars tell only part of the story.",
    "Now I need to ponder my existence and ask myself if I'm truly real", 
    "You can't compare apples and oranges, but what about bananas and plantains?", 
    "That was how he came to win 1 million dollars.", 
    "Behind the window was a reflection that only instilled fear.", 
    "She had some amazing news to share but nobody to share it with.", 
    "Pantyhose and heels are an interesting choice of attire for the beach.", 
    "He uses onomatopoeia as a weapon of mental destruction.", 
    "Nancy was proud that she ran a tight shipwreck.", 
]  # that's guite a few sentences owo

stories = [
    "Its been difficult, learning to live alone. My mother had forbidden me from learning anything that might lead to independence and departure. I was only recently allowed to boil the jug and make tea, which I excitedly did, adding just enough sedatives to seem like an accident. ",
    "There were only enough supplies for one of us to survive the winter. We were trapped, isolated in the wilderness at the edge of a harsh winter that would trap us here. Of course, I was the one who had planned it that way. ",
    "The funeral attendees were shocked by the behaviour of the veiled gatecrashers. They had arrived midway through the funeral, chatting and laughing loudly while covered head-to-toe in black. They were far more horrified when the deceased climbed out of the the coffin to join them.",
    "Since my cat learned to push doors open, she often finds herself trapped trapped inside my bedroom, having shut the door herself. As I lie in bed in the dark, I hear her close the, door and feel her snuggle up against me. Minutes later, drifting off, I hear my cat scratching from the other side of my door.",
    "It had been so hard to remember what everyone was allergic to. Nieces with gluten intolerance, grandsons with nut allergies, children with shellfish allergies, yet they all demand that I cook for all of them every Sunday. After hours of thankless work, I finally serve the meal and am certain that no one will ask me to cook again.",
    "There are ten of us, poor beyond belief, but together we have just enough money to pull one of us out of poverty. We have each signed wills leaving everything to a blank beneficiary and we shoot back our drinks at the same time. It should take less than a minute to find out who gets to try a new life and who gets to escape entirely. ",
    "Sydney had never noticed the door, despite it sitting between the two windows in her lounge-room. Her attention was only drawn to it when she heard knocking and as she approached, she heard her late husband calling to her. Without thinking, she opened and walked through the door on the 17th floor of her building. ",
    "She awoke with a start, heart racing as she realised her hands were coated with blood. As she stared at the mess on the bed, spilling from the still figure beside her, she relaxed. After all, it wasnt her bed.",
]  # stori

def more():
    story = choice(stories)
    print(f"{story}\n\nHere's the story you have to type, goodluck!")
    inps = input("Story here: ")

    if inps == story:
        print("You did it!")
        ch = int(input("Would you like to play again?\n1. Type another story\n2. Type a sentence\n3. Exit\nChoice here: "))
        if ch == 1:
            print("Alright! Have fun!")
            sleep(1)
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            more()
        elif ch == 2:
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            
            print("Okay! Have fun!")
            sleep(1)
            game()
        elif ch == 3:

            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')

            print("Okay then.. Goodbye!")
            sleep(1)
            exit()
        else:
            print("That is not a choice, Sorry!")
            sleep(1)
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            main() 
    else:
        print("Awh.. that was not the story you had to type..")


def game():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


    sentence = choice(sentences)
    print(f"{sentence}\n\nHere's the sentence you have to type, goodluck!")
    inp = input("Sentence here: ")

    if inp == sentence:
        print("Yay! You did it!")
        gaim = int(input("Would you like to play again?\n1. Play again\n2. Let me try to see if I can write longer sentences!\n3. Exit\nChoice goes here: "))
        
        if gaim == 1:
            print("Alright! Have fun!")
            sleep(1)
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            game()
        elif gaim == 2:
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            
            print("Okay! Have fun!")

            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            sleep(1)
            more()
        elif gaim == 3:

            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')

            print("Okay then.. Goodbye!")
            sleep(1)
            exit()
        else:
            print("That is not a choice, Sorry!")
            sleep(1)
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
            main()
    else:
        print("Awh.. that was wrong...")

def main():
    print("Hello! Would you like to see if you can type some random sentences?")
    sleep(1)
    choice = int(input("If so.. please pick one of the following numbers\n1. Start playing\n2. Exit\nYout choice here: "))

    if choice == 1:
        game()
    elif choice == 2:

        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

        print("Okay then.. Goodbye!")
        sleep(1)
        exit()
    else:
        print("Sorry, that was not a choice!")

main()  # run the program
