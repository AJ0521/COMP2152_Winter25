#
# Student ID: 101505643
# Name: Abrar Junaid,Mohammed
# GitHub: @AJ0521

import random

# Define the weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Function to roll the dice and select a weapon
def roll_weapon():
    try:
        # Roll the dice (1 to 6)
        weaponRoll = random.randint(1, 6)
        print(f"You rolled a {weaponRoll}.")

        # Get the weapon based on the roll
        weapon = weapons[weaponRoll - 1]
        print(f"Your weapon is gonnna be: {weapon}")


        if weaponRoll <= 2:
            print("unfortunately You rolled a weak weapon, My friend.")
        elif weaponRoll <= 4:
            print("Your weapon is meh, but dont worry about it.")
        else:
            print("Impressive weapon, friend!")

        # This gonna Check if the weapon is not a Fist
        if weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except ValueError:
        print("Error: Please enter a valid integer.")
    except IndexError:
        print("Error: Index out of range. Please check the weapon list.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Calling the function to execute the weapon roll
roll_weapon()