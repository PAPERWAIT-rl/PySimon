from random import *
from colorama import Fore, Back, Style, init
import time
import os
# Initialize colorama (needed for Windows)
init(autoreset=True)

Color_list = []
start = 0
next_color = 0
color = ""
Formatted_array = ""

def Array_formatter():
    global Color_list, Formatted_array
    Formatted_array = ''.join(str(x) for x in Color_list)
    
def color_lexer():
    global color, next_color
    if next_color == 1:
        color = Fore.RED 
    elif next_color == 2:
        color = Fore.GREEN
    elif next_color == 3:
        color = Fore.BLUE
    elif next_color == 4:
        color = Fore.YELLOW

# The Main Game Loop
def game_loop():
    # Define globals
    global start,next_color,color
    
    # Pick random color
    error = 0
    while True:
        if start == 0:
            print("Type 'S' to start!")
            if input().upper() == 'S':
                start = 1
                error = 0
                
            else:
                print("Invalid, try again.")
                error = 1
            continue
        if start == 1 and error == 0: 
            next_color = randrange(1,5)
            Color_list.append(next_color)
        color_lexer()
        print(f"{color}" + "######################")
        time.sleep(1)
        if os.name == 'nt': # Windows
            os.system('cls')
        else: # Linux / macOS
            os.system('clear')
        Array_formatter()
        
        
        # Ask user color pattern
        user_input = input("Type pattern: 1 for Red, 2 for Green, 3 for Blue, 4 for Yellow.\n")
        if user_input == Formatted_array:
            print("Correct! Adding color...")
        else:
            print("Wrong! Game Over.")
            break
game_loop()