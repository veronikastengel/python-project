#!/usr/bin/env python
# coding: utf-8

import random

def coin_flip(first_r):
    if first_r:
        shake_yesno = input("You want to shake it? 'yes' or 'no'")
        shake_yesno = shake_yesno.strip().lower()
    else:
        shake_yesno = "yes"

    # Validate the player's input
    if shake_yesno != "yes" and shake_yesno != "no":
        print("Invalid input. Should have entered 'yes' or 'no'.")

    # Simulate the coin flip
    if shake_yesno == "yes":
        coin = random.choice(["yes", "no"])
        # Check if the player wins or loses
        if shake_yesno == coin:
            print("A paper clip falls out!")
            clip = True
        else:
            print("Nothing happened.")
            clip = False
    else:
        clip = False
    return clip

def shake_it():
    first_round = True
    while True:
        clip = coin_flip(first_round)
        first_round = False
        if clip == False:
            play_again = input("Do you want to try shaking it again? Please enter 'yes' or 'no'.").strip().lower()
            if play_again != "yes":
                break
        else:
            break
    return clip

#to call it:
#shake_it()
