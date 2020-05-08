# Author Khalid
import time
import random


# printing and pausing for second!
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)  # or you can pass it as parameter to the function!
    # as (message_to_print, time_delay) for example if you want!, but I
    #  made it the same!


# printing the introduction!
def intro(enemy):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) dagger.")


# Entering the house!
def house(game_stauts, enemy):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                f"out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")

    if "cave" not in game_stauts:  # we can put this in new def if we want!
        print_pause("You feel a bit under-prepared for this, what "
                    "with only having a tiny dagger.")
    status = input("Would you like to (1) fight or (2) run away?")
    if status == "1":
        fight(game_stauts, enemy)
    elif status == "2":
        run_away(game_stauts, enemy)
    else:
        # house(game_stauts, enemy)
        end_game()  # quit to end_game() based on the game!


# Entering the cave!
def cave(game_stauts, enemy):
    # Things that happen to the player goes in the cave
    print_pause("You peer cautiously into the cave.")
    # print(game_stauts, "!!!")  # Debugging!

    if "cave" not in game_stauts:  # we can put this in another def if we want!
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    "sword with you.")
        game_stauts.append("cave")  # we have the magical Sword ^_^ now!
    else:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")

    print_pause("You walk back out to the field.")
    selection(game_stauts, enemy)


def fight(game_stauts, enemy):
    # Things that happen when the player fights. we can define a {weapon} also!
    if "cave" not in game_stauts:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {enemy}.")
        print_pause("You have been defeated!")
    else:
        print_pause(f"As the {enemy} moves to attack, you unsheath your "
                    "new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                    "brace yourself for the attack.")
        print_pause("But the pirate takes one look at your shiny new toy and "
                    "runs away!")
        print_pause("You have rid the town of the pirate. You are victorious!")

    end_game()


# selection process thru the field!
def selection(game_stauts, enemy):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    field(game_stauts, enemy)


def field(game_stauts, enemy):
    choice = input("(Please enter 1 or 2.)\n ")
    if choice == "1":  # or "1" in choice:
        house(game_stauts, enemy)
    elif choice == "2":  # or "2" in choice:
        cave(game_stauts, enemy)
    else:
        field(game_stauts, enemy)  # or while repeat not in/in ['1', '2']


def run_away(game_stauts, enemy):
    print_pause("You run back into the field. Luckily, you don't seem "
                "to have been followed.")
    selection(game_stauts, enemy)


# Main function
def play_game():
    enemy = random.choice(["pirate", "troll", "wicked fairie", "dragon",
                           "gorgon"])
    game_stauts = []
    intro(enemy)
    # print(game_stauts, "!")  # Debugging!
    # print("enemy = ", enemy)  # Debugging!
    selection(game_stauts, enemy)


def repeat_game():
    print_pause("Excellent! Restarting the game ...")
    play_game()
    #  return


def end_game():
    # print_pause("GAME OVER")
    repeat = input("Would you like to play again? (y/n)")
    if repeat == "y":
        repeat_game()

    elif repeat == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        end_game()  # repeat! or while repeat not in/in ['y', 'n']:


# run the initial game!
play_game()


# pycodestyle adventure_game.py 100% done!
#  End! clone on April 28, 2020
