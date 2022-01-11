import msvcrt
import sys
import random
import os

player_score = 0

computer_score = 0

def rps(keypressed):
     if keypressed == b'1':
          return "ROCK"
     elif keypressed == b'2':
          return "PAPER"
     elif keypressed == b'3':
          return "SCISSORS"
     elif keypressed == b'q':
          sys.exit()

while True:


     print("\nType 1 for ROCK, 2 for PAPER, 3 for SCISSORS and q to quit")

     inputval = rps(msvcrt.getch())

     if inputval == None:
          print("Invalid option, try again")
          print("\nPress any key to continue...")
          msvcrt.getch()
          os.system('CLS')
          continue


     computeropt = random.randint(1,3)

     if computeropt == 1: computerval = "ROCK"
     elif computeropt == 2: computerval = "PAPER"
     else: computerval = "SCISSORS"

     print("\nYou selected {} and Computer selected {}".format(inputval,computerval))

     print("\n==========================================================")

     if computerval == inputval: print("\nNoone gets a point, Current Score: You {} and Computer {}".format(player_score,computer_score))

     elif (inputval == "ROCK" and computerval == "SCISSORS") or (inputval == "SCISSORS" and computerval == "PAPER") or (inputval == "PAPER" and computerval == "ROCK"):
          player_score += 1
          print("You get 1 point, your score is {0}  and computer score is {1}".format(player_score,computer_score))
     else:
          computer_score += 1
          print("Computer gets 1 point, your score is {}  and computer score is {}".format(player_score,computer_score))

     print("==========================================================")

     print("\nPress any key to continue...")

     msvcrt.getch()
     os.system('CLS')









