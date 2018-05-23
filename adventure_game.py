# Braden Wade
# 2018-05-16

import time
import random
import os
import sys
import textwrap
import cmd

##### GLOBAL VARIABLES #####
option = ""

class player:
    '''Sets up a player'''
    def __init__(self):
        self.name = ""
        self.weapon = ""
        self.player_hp = 100
        self.player_type = ""
        self.type_attributes = []
        self.has_ring = False
        self.damage = 0
player = player()

def player_stats():
    print("\n###########################################")
    print("#            - PLAYER MENU -              #")
    print("###########################################")
    print("Your name is:", player.name)
    print("Your weapon is:", player.weapon)
    print("Your are a:", player.player_type)
    print("Your HP is at", player.player_hp,"out of 100")
    print("Your attributes are:", player.type_attributes[0, 1, 2])
    if player.has_ring == True:
        print("# You have the goblin's ring!")
    print("###########################################\n")

class goblin:
    '''Sets up a Goblin'''
    def __init__(self):
        self.damage = 0
        self.hp = 80
goblin = goblin()

##### CHECK TITLE SCREEN INPUT #####
def title_screen_check():
    option = input("> ")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
        
##### TITLE SCREEN #####
def title_screen_options():
    title_screen_check()
    while option.lower() != ['play', 'help', 'quit']:
        title_screen_check()
        
##### DISPLAY TITLE MENU #####
def title_screen():
    print('##################################')
    print('# Welcome to the Text Based RPG! #')
    print('##################################')
    print('#            - PLAY -            #')
    print('#            - HELP -            #')
    print('#            - QUIT -            #')
    print('##################################')
    title_screen_options()

##### DISPLAY TITLE MENU #####
def help_menu():
    print('##################################')
    print('#          - HELP MENU -         #')
    print('##################################')
    print('# - Use numbers to select options#')
    print('# - Explore everywhere!          #')
    print('##################################')
    enter()
    title_screen()
    
##### STARTS THE GAME BY GOING TO PLAYER SETUP #####
def start_game():
    player_setup()

##### TAKES INPUT TO SET UP PLAYER #####
def player_setup():
    print("What is your name?")
    player_name = input("> ")
    player.name = player_name
    player.weapon = "Knife"
    print("What is your species? ")
    player_type = input("> ")
    player.player_type = player_type
    if player_type.lower() == "human":
        player.type_attributes = ["Fast", "Cunning", "Weak"]
    else:
        player.type_attributes = ["Strong", "Dumb", "Brave"]
    player.player_hp = 100
    town_gate()

##### LOCATION ONE #####
def town_gate(): 
    print("\n----------------------------------------\n")
    print("You are at the town gate...")
    print("There is a guard standing before you...")
    print("\n1) Talk to the guard")
    print("2) Attack the guard")
    print("3) Leave the town gate")
    print("\n----------------------------------------\n")
    print("What do you want to do?")
    choice = input("> ")
    
    ##### CHECK INPUT AND CALL NEXT #####
    if choice == '1':
        if player.has_ring == True:
            ending()
        else:
            print("----------------------------------------")
            print("\nGuard: Hello Stranger. So your name is ", player.name, "? \nGuard: Sorry but we can not let a stranger into our town.\n")
            print("----------------------------------------")
            enter()
            town_gate()
    elif choice == '2':
        player.player_hp -= 10
        print("\n----------------------------------------\n")
        print("Guard: Hey, don't be stupid!\n\nThe guard hits you too hard and you give up\n(You receive ten damage)")
        print("Your HP is: ", player.player_hp)
        print("\n----------------------------------------\n")
        if player.player_hp <= 0:
            dead()
        enter()
        town_gate()
    elif choice == '3':
        cross_road()
    else:
        error()
        town_gate()

##### SECOND LOCATION #####
def cross_road():
    print()
    print("----------------------------------------")
    print()
    print("You come to a cross roads")
    print("The town is to the south...")
    print()
    print("1) Go north")
    print("2) Go east")
    print("3) Go south")
    print("4) Go west")
    print() 
    print("----------------------------------------")
    print("What do you want to do?")
    option = input("> ")
    
    ##### CHECK INPUT AND CALL NEXT #####
    if option == "1":
        north()
    elif option == "2":
        east()
    elif option == "3":
        town_gate()
    elif option == "4":
        west()
    else:
        error()
        enter()
        cross_road()

##### HEALING RIVER LOCATION #####
def north():
    ##### CHECK IF HP IS FULL #####
    if player.player_hp == 100:
        print()
        print("----------------------------------------")
        print()
        print("You come arrive at a healing river...")
        print("But you HP is already full!")
        print()
        print("1) Go back")
        print() 
        print("----------------------------------------")
        print("What do you want to do?")
    else:
        player.player_hp += 10
        print()
        print("----------------------------------------")
        print()
        print("You come arrive at a healing river...")
        print("You gain 10 HP!")
        print("Your HP is now: ", player.player_hp)
        print()
        print("1) Go back")
        print() 
        print("----------------------------------------")
        print("What do you want to do?")
    option = input("> ")
    
    ##### CHECK INPUT AND CALL NEXT #####
    if option == "1":
        cross_road()
    else:
        error()
        print("You are automatically being sent to the cross road!")
        enter()
        cross_road()

##### SWORD LOCATION #####
def east():
    player.weapon = "Sword"
    print()
    print("----------------------------------------")
    print()
    print("You find a sword in the forest!")
    print("Your weapon is now: ", player.weapon)
    print()
    print("1) Go back")
    print() 
    print("----------------------------------------")
    print("What do you want to do?")
    option = input("> ")
    
    ##### CHECK INPUT AND CALL NEXT #####
    if option == "1":
        cross_road()
    else:
        error()
        print("You are automatically being sent to the cross road!")
        enter()
        cross_road()

##### GOBLIN FIGHT LOCATION #####
def west():
    print()
    print("----------------------------------------")
    print()
    print("You encountered a Goblin!\n")
    print("1) Fight")
    print("2) Run\n")
    print("----------------------------------------")
    print("What do you want to do?")
    option = input("> ")
    
    ##### CHECK INPUT AND CALL NEXT #####
    if option == "1":
        fight()
    elif option == "2":
        cross_road()
    else:
        error()
        print("You are automatically being sent to the cross road!")
        enter()
        cross_road()

def attack():
    if player.weapon == "Knife":
            player.damage = random.randint(1, 6)
    elif player.weapon == "Sword":
        player.damage = random.randint(1, 9)
        
    print("You attacked the goblin and gave", player.damage, "damage.")
    goblin.hp = goblin.hp - player.damage
    print("The goblin's HP is: ", goblin.hp)
        
    if goblin.hp <= 0:
        win()
    elif goblin.hp >= 1:
        goblin.damage = random.randint(1, 11)
        print("The goblin counter-attacks and deals", goblin.damage, "damage")
        player.player_hp = player.player_hp - goblin.damage
        print("Your HP is: ", player.player_hp)
        
    if player.player_hp <= 0:
        dead()
    else:
        fight()
    enter()

def win():
    print("\n----------------------------------------\n")
    print("You kilSDZXZDSled the Goblin!\nThe Goblin dropped a ring...\nYou obtained a silver ring!")
    print("\nGo east")
    print("\n----------------------------------------\n")
    print("What do you want to do?")
    choice = input("> ")
    player.has_ring = True
    
    if choice == 1:
        cross_road()
    else:
        error()
        enter()
        win()

def fight():
    print("\n----------------------------------------\n")
    print("Your HP is: ", player.player_hp, "\nThe goblins HP is: ", goblin.hp)
    print("\n1) Attack")
    print("2) Run")
    print("\n----------------------------------------\n")
    print("What do you want to do?")
    choice = input("> ")
    
    if choice == "1":
        attack()
    elif choice == "2":
        cross_road()
    else:
        error()
        enter()
        fight()

def error():
    print("ERROR: INVALID INPUT")
    enter()

def enter():
    enter = input("Enter to continue...")

def ending():
    print("Guard: You killed the goblin? Thank you!")
    print("You seem very trustworthy! Welcome to the town!")
    print("\n----------------------------------------\n")
    print("              # THE END #                   ")
    print("\n----------------------------------------\n")
    sys.exit()
   
def dead():
    print("\n----------------------------------------\n")
    print("                YOU DIED                    ")
    print("\n----------------------------------------\n")
    sys.exit()

title_screen()
start_game()









    

