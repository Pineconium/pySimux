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
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the pySimux Launcher")
time.sleep(2)
for i in tqdm (range (127),  
               desc=Fore.GREEN + "Loading pySimux",  
               ascii=False, ncols=75): 
    time.sleep(0.01)       

print(Fore.GREEN + "Complete. . .")
time.sleep(1) 
#This will start the Simu
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(.500)
print(f"{Fore.WHITE}Welcome to {Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux")
print(f"{Fore.WHITE}{Style.NORMAL}Version 0.0.0.06")
print()
print(f"{Fore.WHITE}{Style.NORMAL}Type a command, for a list of commands type {Style.BRIGHT}help{Style.NORMAL} in the terminal")
while True:
 command = input('TYPE ANYTHING: ')
 if command == 'joe':
    print('Joe Mama')
 elif command == 'help':
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
  print(f"{Style.NORMAL}debugtest{Style.DIM} - - - -{Fore.GREEN}For debugging purposing only")
  print(f"{Style.NORMAL}{Fore.WHITE}shutdown")
  print(f"{Style.NORMAL}web {Style.DIM}(url){Style.NORMAL}")
  print(f"{Style.NORMAL}turtle [pattern] - - - Type help turtle for a list of patterns.")
 elif command == 'echo':
   whattosay = input('Type anything:')
   print(whattosay)
 elif command == 'wait':
   waiter = input('Time to wait (in seconds)')
   time.sleep(waiter)
 elif command == 'clear':
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"{Fore.WHITE}Welcome to {Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux")
   print(f"{Fore.WHITE}{Style.NORMAL}Version 0.0.0.06")
   print()
   print(f"{Fore.WHITE}{Style.NORMAL}Type a command, for a list of commands type {Style.BRIGHT}help{Style.NORMAL} in the terminal")
 elif command == 'info':
   print(f"{Fore.WHITE}{Style.NORMAL}Simu: {Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux")
   print(f"{Fore.WHITE}{Style.NORMAL}Version: 0.0.0.06")
   print(f"{Fore.WHITE}{Style.NORMAL}Language: {Style.BRIGHT}English{Style.NORMAL} - - - {Style.DIM}You can translate pySimux into your language by modifying the {Style.BRIGHT}.py{Style.NORMAL} file")
   print()
   print()
   print()
   print()
   print(f"{Fore.WHITE}{Style.NORMAL}(C) {Fore.GREEN}Budgie{Fore.YELLOW}{Style.BRIGHT}Ware{Fore.WHITE}{Style.NORMAL} 2023. Made by {Fore.BLUE}DAVETHEBABY")
   print(f"{Fore.YELLOW}py{Fore.BLUE}{Style.BRIGHT}Simux{Fore.WHITE} is {Style.BRIGHT}open-source{Style.NORMAL}, meaning you are free to modify the .py file if you want to and share it around!")
   print(f"{Fore.WHITE} See the {Style.BRIGHT}MODIFYING.TXT{Style.NORMAL} file for more info.")
 elif command == 'shutdown':
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
 elif command == 'ascii cat':
   print(f"{Fore.GREEN}|\      _,,,---,,_")
   print("/,`.-'`'    -.  ;-;;,_")
   print("|,4-   )-,_..;\ (  `'-'")
   print("'---''(_/--'  `-'\_) )")
   print(f"{Fore.WHITE}")
 elif command == 'ascii Rainbow':
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
 elif command == 'debugtest':
   print(f"{Fore.RED}WARNING! {Fore.WHITE}You are about to use a tool that should ONLY be used for testing purposes")
   input("Press Enter to Continue...")
   os.system('cls' if os.name == 'nt' else 'clear')
   print("Colour Test")
   time.sleep(2)
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"{Fore.RED}██████████████████████████████████████")
   print(f"{Fore.RED}██████████████████████████████████████")
   print(f"{Fore.RED}██████████████████████████████████████")
   print(f"{Fore.RED}██████████████████████████████████████")
   print(f"{Fore.RED}██████████████████████████████████████")
   print(f"{Fore.RED}██████████████████████████████████████")
   print(f"{Fore.RED}██████████████████████████████████████")
   print(f"{Fore.RED}██████████████████████████████████████")
   time.sleep(5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   print(f"{Fore.YELLOW}██████████████████████████████████████")
   time.sleep(5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"{Fore.GREEN}██████████████████████████████████████")
   print(f"{Fore.GREEN}██████████████████████████████████████")
   print(f"{Fore.GREEN}██████████████████████████████████████")
   print(f"{Fore.GREEN}██████████████████████████████████████")
   print(f"{Fore.GREEN}██████████████████████████████████████")
   print(f"{Fore.GREEN}██████████████████████████████████████")
   print(f"{Fore.GREEN}██████████████████████████████████████")
   print(f"{Fore.GREEN}██████████████████████████████████████")
   time.sleep(5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"{Fore.BLUE}██████████████████████████████████████")
   print(f"{Fore.BLUE}██████████████████████████████████████")
   print(f"{Fore.BLUE}██████████████████████████████████████")
   print(f"{Fore.BLUE}██████████████████████████████████████")
   print(f"{Fore.BLUE}██████████████████████████████████████")
   print(f"{Fore.BLUE}██████████████████████████████████████")
   print(f"{Fore.BLUE}██████████████████████████████████████")
   print(f"{Fore.BLUE}██████████████████████████████████████")
   time.sleep(5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   print(f"{Fore.MAGENTA}██████████████████████████████████████")
   time.sleep(5)
   os.system('cls' if os.name == 'nt' else 'clear')
   print(f"{Fore.WHITE}██████████████████████████████████████")
   print(f"{Fore.WHITE}██████████████████████████████████████")
   print(f"{Fore.WHITE}██████████████████████████████████████")
   print(f"{Fore.WHITE}██████████████████████████████████████")
   print(f"{Fore.WHITE}██████████████████████████████████████")
   print(f"{Fore.WHITE}██████████████████████████████████████")
   print(f"{Fore.WHITE}██████████████████████████████████████")
   print(f"{Fore.WHITE}██████████████████████████████████████")
   time.sleep(5)
   print("Test OK!")
   time.sleep(2)
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
 elif command == 'math':
  number1 = int(input('What is your first number? '))
  operator = input('What is your operator? ')
  number2 = int(input('What is your second number? '))
  if operator == '+':
    res = number1 + number2
  elif operator == '-':
    res = number1 - number2
  elif operator == '*':
    res = number1 * number2
  elif operator == '/':
    res = number1 / number2
  print("Your answer is: ")
  print(res)
  
 elif command == 'turtle rainbow':
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
 elif command == 'web':
   url = input("Enter a URL: ")
   show_me(url)
 elif command == 'help turtle':
  print('Opens a turtle window and draws a pattern')
  print("")
  print("Patterns are: rainbow, circle, tiktok, square, loop")
 elif command == 'help web':
  print('Opens the provided URL in the users default web browser')
  print("")
  print("Format: web -> Input a vaild url (such as google.com) -> Opens the URL in the default browser")
 elif command == 'help ascii':
  print('Draws a pattern in ASCII ART')
  print("")
  print("Patterns are: cat, Rainbow")
 elif command == 'help math':
  print('Solves an equation using print and if + elif statements')
  print("")
  print("Format: math -> number 1 -> operator (+, -, *, /) -> number two = answer")
 else:
   print(f"{Style.BRIGHT}{Fore.RED}UNKNOWN COMMAND: ", command)
   print(f"{Fore.WHITE}{Style.NORMAL}For a list of commands type {Style.BRIGHT}help{Style.NORMAL} in the terminal")
