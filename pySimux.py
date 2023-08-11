'''
  (c) BudgieWare 2023. Made by DAVETHEBABY
  Modified by Strawpoem
  pySimux is open-source, meaning you are free to modify the .py file if you want to share it around!
  See the MODIFYING.txt for more info.
'''


import time
import turtle
import colorama
from colorama import Fore, Back, Style
import os
from tqdm import tqdm 
from webbrowser import open as show_me

'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
def main():
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Welcome to the pySimux Launcher") # Launcher message
  time.sleep(2)
  # Loading Screen
  for i in tqdm (range (127),  
                desc=Fore.GREEN + "Loading pySimux",  
                ascii=False, ncols=75): 
      time.sleep(0.01)       
  # Print "complete"
  print(Fore.GREEN + "Complete. . .")
  time.sleep(1) 
  # This will start the Simu
  os.system('cls' if os.name == 'nt' else 'clear')
  time.sleep(.500)
  # Welcome Text
  welcomemessage()
  # This runs the commands
  while True:
    command = input('TYPE ANYTHING: ')
    if command == 'joe':
        joe()
    elif command == 'help':
      help()
    elif command == 'echo':
      echo()
    elif command == 'wait':
      wait()
    elif command == 'clear':
      clear()
    elif command == 'info':
      info()
    elif command == 'shutdown':
      shutdown()
    elif command == 'ascii cat':
      ascii_cat()
    elif command == 'ascii Rainbow':
      ascii_rainbow()
    elif command == 'debug':
      debug()
    elif command == 'math':
      math()
    elif command == 'turtle rainbow':
      turtle_rainbow()
    elif command == 'web':
      web()
    elif command == 'help turtle':
      help_turtle()
    elif command == 'help web':
      help_web()
    elif command == 'help ascii':
      help_ascii()
    elif command == 'help math':
      help_math()
    else:
      unknown_command(command)

'''
  From here, these are all the programs in pySimux
  All Programs, from top to bottom: unknown_command(), welcomemessage(), joe(), echo(), wait(), clear(), info(), shutdown(), ascii_cat(), ascii_rainbow(), debug(), math(), turtle_rainbow(), web(), 
'''

# If command not in list above is typed in. variable command is the command, that the user typed in wrong
def unknown_command(command):
  print(f"{Style.BRIGHT}{Fore.RED}UNKNOWN COMMAND: ", command)
  print(f"{Fore.WHITE}{Style.NORMAL}For a list of commands type {Style.BRIGHT}help{Style.NORMAL} in the terminal")

# To show welcome text
def welcomemessage():
  print(f"{Fore.WHITE}Welcome to {Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux")
  print(f"{Fore.WHITE}{Style.NORMAL}Version 0.0.0.06\n")
  print(f"{Fore.WHITE}{Style.NORMAL}Type a command, for a list of commands type {Style.BRIGHT}help{Style.NORMAL} in the terminal")

# Program to print "Joe Mama"
def joe():
  print('Joe Mama')

# Program to repeat, what you typed
def echo():
  whattosay = input('Type anything:')
  print(whattosay)

# Program, that lets you wait for a specific amount of time
def wait():
  waiter = input('Time to wait (in seconds)')
  time.sleep(waiter)

# Clears the screen and shows welcome message again
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  welcomemessage()

# Prints out information about system and copyright
def info():
  print(f"{Fore.WHITE}{Style.NORMAL}Simu: {Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux")
  print(f"{Fore.WHITE}{Style.NORMAL}Version: 0.0.0.06")
  print(f"{Fore.WHITE}{Style.NORMAL}Language: {Style.BRIGHT}English{Style.NORMAL} - - - {Style.DIM}You can translate pySimux into your language by modifying the {Style.BRIGHT}.py{Style.NORMAL} file", '\n' * 4)
  print(f"{Fore.WHITE}{Style.NORMAL}(C) {Fore.GREEN}Budgie{Fore.YELLOW}{Style.BRIGHT}Ware{Fore.WHITE}{Style.NORMAL} 2023. Made by {Fore.BLUE}DAVETHEBABY")
  print(f"{Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux{Fore.WHITE} is {Style.BRIGHT}open-source{Style.NORMAL}, meaning you are free to modify the .py file if you want to and share it around!")
  print(f"{Fore.WHITE} See the {Style.BRIGHT}MODIFYING.TXT{Style.NORMAL} file for more info.")

# Creates fake shutdown screen
def shutdown():
  print(f"{Fore.WHITE}Shutting down {Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux")
  time.sleep(2)
  print(f"{Fore.WHITE}{Style.NORMAL}Disabling a terminal element")
  print("TERMINAL HAS SUCCESSFULLY STOPPED")
  print("Disabling a terminal element")
  print("TERMINAL HAS SUCCESSFULLY STOPPED")
  print("Killing all simu tasks")
  print("1 task(s) has been killed")
  time.sleep(0.07)
  print("3 task(s) has been killed")
  time.sleep(0.1)
  print("8 task(s) has been killed")
  time.sleep(0.06)
  print("10 task(s) has been killed")
  time.sleep(0.05)
  print("11 task(s) has been killed")
  time.sleep(0.12)
  print("28 task(s) has been killed")
  time.sleep(0.03)
  print("Stopping pySimux")
  time.sleep(1.25)
  print("PYSIMUX HAS SUCCESSFULLY STOPPED")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  while True:
    print("To restart pySimux, relaunch the .py file, to exit strike Ctrl+C")
    os.system('cls' if os.name == 'nt' else 'clear')

# Prints out a cat
def ascii_cat():
  print(f"{Fore.GREEN}|\      _,,,---,,_")
  print("/,`.-'`'    -.  ;-;;,_")
  print("|,4-   )-,_..;\ (  `'-'")
  print("'---''(_/--'  `-'\_) )")
  print(f"{Fore.WHITE}")

# Prints out a rainbow
def ascii_rainbow():
  print(f"{Fore.RED}{Style.DIM}██████████████████████████████████████")
  print(f"{Fore.RED}{Style.NORMAL}██████████████████████████████████████")
  print(f"{Fore.RED}{Style.BRIGHT}██████████████████████████████████████")
  print(f"{Fore.YELLOW}{Style.DIM}██████████████████████████████████████")
  print(f"{Fore.YELLOW}{Style.NORMAL}██████████████████████████████████████")
  print(f"{Fore.YELLOW}{Style.BRIGHT}██████████████████████████████████████")
  print(f"{Fore.GREEN}{Style.DIM}██████████████████████████████████████")
  print(f"{Fore.GREEN}{Style.NORMAL}██████████████████████████████████████")
  print(f"{Fore.GREEN}{Style.BRIGHT}██████████████████████████████████████")
  print(f"{Fore.CYAN}{Style.DIM}██████████████████████████████████████")
  print(f"{Fore.CYAN}{Style.NORMAL}██████████████████████████████████████")
  print(f"{Fore.CYAN}{Style.BRIGHT}██████████████████████████████████████")
  print(f"{Fore.BLUE}{Style.DIM}██████████████████████████████████████")
  print(f"{Fore.BLUE}{Style.NORMAL}██████████████████████████████████████")
  print(f"{Fore.BLUE}{Style.BRIGHT}██████████████████████████████████████")
  print(f"{Fore.MAGENTA}{Style.DIM}██████████████████████████████████████")
  print(f"{Fore.MAGENTA}{Style.NORMAL}██████████████████████████████████████")
  print(f"{Fore.MAGENTA}{Style.BRIGHT}██████████████████████████████████████")
  
  print(f"{Fore.WHITE}{Style.NORMAL}")

# Program for debugging
def debug():
  print(f"{Fore.RED}WARNING! {Fore.WHITE}You are about to use a tool that should ONLY be used for testing purposes")
  input("Press Enter to Continue...")
  os.system('cls' if os.name == 'nt' else 'clear')
  #Prints out Red, Yellow, Green, Blue, Magenta and white for 5 seconds each
  print("Colour Test")
  time.sleep(2)
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(8):
    print(f"{Fore.RED}██████████████████████████████████████")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(8):
    print(f"{Fore.YELLOW}██████████████████████████████████████")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(8):
    print(f"{Fore.GREEN}██████████████████████████████████████")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(8):
    print(f"{Fore.BLUE}██████████████████████████████████████")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(8):
    print(f"{Fore.MAGENTA}██████████████████████████████████████")
  time.sleep(5)
  os.system('cls' if os.name == 'nt' else 'clear')
  for i in range(8):
    print(f"{Fore.WHITE}██████████████████████████████████████")
  time.sleep(5)
  print("Test OK!")
  time.sleep(2)
  # opens a windows with a turtle
  print("Turtle Test")
  time.sleep(2)
  print("To exit this test, close the Turtle Window")
  mypen= turtle.Turtle()
  mypen.shape('turtle')
  mypen.speed(10)
  
  window= turtle.Screen()
  window.bgcolor('white')
  rainbow= ['red','orange','yellow','green','blue','indigo','violet']
  size= 180
  mypen.penup()
  mypen.goto(0,-180)
  for color in rainbow:
    mypen.color(color)
    mypen.fillcolor(color)
    mypen.begin_fill()
    mypen.circle(size)
    mypen.end_fill()
    size-=20

    turtle.done()
  
# Simple Calculator Program
def math():
  # Asks for first number
  number1 = int(input('What is your first number? '))
  # Asks for operator
  operator = input('What is your operator? ')
  # Asks for second number
  number2 = int(input('What is your second number? '))
  # Calculate equation
  if operator == '+':
    res = number1 + number2
  elif operator == '-':
    res = number1 - number2
  elif operator == '*':
    res = number1 * number2
  elif operator == '/':
    res = number1 / number2
  # Prints out answer
  print("Your answer is: ")
  print(res)

# Program, that creates a window with a turtle drawing circles
def turtle_rainbow():
  mypen= turtle.Turtle()
  mypen.shape('turtle')
  mypen.speed(10)
  
  window= turtle.Screen()
  window.bgcolor('white')
  rainbow= ['red','orange','yellow','green','blue','indigo','violet']
  size= 180
  mypen.penup()
  mypen.goto(0,-180)
  for color in rainbow:
    mypen.color(color)
    mypen.fillcolor(color)
    mypen.begin_fill()
    mypen.circle(size)
    mypen.end_fill()
    size-=20

  turtle.done()
  print("Test OK!")
  time.sleep(2)
  
  print("Test went OK! Returning to terminal in 5 seconds")
  time.sleep(5)

# Opens webbrowser (in real OS) with the URL you input
def web():
  url = input("Enter a URL: ")
  show_me(url)

'''

Help messages

'''

# Help program
def help():
  print('GUIDE: Commands with dim text are arguments that happen AFTER a command is typed. These are in brackets')
  print('GUIDE: Commands with bracketed text but are NOT dimmed are choices, these can be entered in ONE whole command')
  print('* If a arg. has a pound sign ("#"), its a number input')
  print('* If a arg. has NO SIGN, it accepts any input in text (string arg)')
  print('* If a arg. has a set of symbols in a double brackets (for example: (+, -), it accepts ONLY the allowed symbols ')
  print('* If a arg. has a star (*) this arg. is optional')
  print("")
  print(f"{Style.NORMAL}help {Style.DIM}(*command)")
  print(f"{Style.NORMAL}wait {Style.DIM}(#secs)")
  print(f"{Style.NORMAL}echo {Style.DIM}(text or number)")
  print(f"{Style.NORMAL}clear")
  print(f"{Style.NORMAL}info")
  print(f"{Style.NORMAL}math {Style.DIM}(#number 1) ((+, -, /, *)), (#number 2)v{Style.NORMAL}")
  print("ascii (cat, dog, Hello, rainbow)")
  print(f"{Style.NORMAL}debug{Style.DIM} - - - -{Fore.GREEN}For debugging purposing only")
  print(f"{Style.NORMAL}{Fore.WHITE}shutdown")
  print(f"{Style.NORMAL}web {Style.DIM}(url){Style.NORMAL}")
  print(f"{Style.NORMAL}turtle [pattern] - - - Type help turtle for a list of patterns.")

# Help page for turtle_rainbow() program
def help_turtle():
  print('Opens a turtle window and draws a pattern', end="\n\n")
  print("Patterns are: rainbow, circle, tiktok, square, loop")
# Help page for web() program
def help_web():
  print('Opens the provided URL in the users default web browser', end="\n\n")
  print("Format: web -> Input a vaild url (such as google.com) -> Opens the URL in the default browser")

# Help page for ascii-art programs
def help_ascii():
  print('Draws a pattern in ASCII ART', end="\n\n")
  print("Patterns are: cat, Rainbow")

# Help page for calculator
def help_math():
  print('Solves an equation using print and if + elif statements', end="\n\n")
  print("Format: math -> number 1 -> operator (+, -, *, /) -> number two = answer")

# Run main
main()
