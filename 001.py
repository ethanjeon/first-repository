""" to-do:
next function: cards?
"""

import random

def main_menu():
    print()
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('|Welcome to the Probability Simulator! What would you like to do?|')
    print('|                        1: Dice Rolls                           |')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print()
    x = input()
    if x == '1':
        dice_roll()

def stats(current_rolls):
    roll_display = [0,0,0,0,0,0]
    for i in current_rolls:
        roll_display[i-1] += 1
    print()
    for i in range(6):
        print('Rolled a ' + str(i+1) + ': ' + str(roll_display[i]) + ' times (' + str(100 * (roll_display[i] / len(current_rolls))) + '%)')
    print()
    running_sum = 0
    for i in current_rolls:
        running_sum += i
    running_sum /= len(current_rolls)
    print('Average roll: ' + str(running_sum))
    print()
    x = input('Press 1 to add rolls: ')
    if x == '1':
        dice_reroll(current_rolls)
    else:
        print()
        print('Here were all of your rolls:')
        print(current_rolls)
        print()
        print()
        print()
        main_menu()

def dice_reroll(current_rolls):
    number_of_additional_rolls = 0
    print()
    print('How many rolls would you like to add?')
    number_of_additional_rolls = int(input('Number of additional rolls: '))
    print()
    for i in range(number_of_additional_rolls):
        x = random.randint(1,6)
        current_rolls.append(x)
    for i in range(len(current_rolls)):
        print('Roll ' + str(i+1) + ': ' + str(current_rolls[i]))
    print()
    x = input('Press 1 to add rolls: ')
    if x == '1':
        dice_reroll(current_rolls)
    else:
        stats(current_rolls)

def dice_roll():
    number_of_rolls = 0
    current_rolls = []
    print()
    print('How many times would you like to roll?')
    print()
    number_of_rolls = int(input('Number of rolls: '))
    print()
    for i in range(number_of_rolls):
        x = random.randint(1,6)
        print('Roll ' + str(i+1) + ': ' + str(x))
        current_rolls.append(x)
    print()
    x = input('Press 1 to add rolls: ')
    if x == '1':
        dice_reroll(current_rolls)
    else:
        stats(current_rolls)

main_menu()
