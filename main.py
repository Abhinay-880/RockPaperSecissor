# ROCK PAPER SCISSOR

import random

a = 'rock'
b = 'paper'
c = 'scissor'
computer = [a,b,c]
score = 0
computer_score = 0
start = True
while start:
    computer_choice = random.choice(computer)
    user_choice = input("enter your choice ? ROCK , PAPER , SCISSOR :").lower()
    if user_choice == 'rock' and computer_choice == 'scissor':
        print("computer : scissor")
        print("YOU WIN")
        score +=1
    elif user_choice == 'scissor' and computer_choice == 'paper':
        print("computer : paper")
        print("YOU WON")
        score +=1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("computer : rock")
        print("YOU WON")
        score +=1
    elif user_choice == 'rock' and computer_choice == 'paper':
        print("computer : paper")
        print("YOU LOOSE")
        computer_score += 1
    elif user_choice == 'scissor' and computer_choice == 'rock':
        print("computer : rock")
        print("YOU LOOSE")
        computer_score += 1
    elif user_choice == 'paper' and computer_choice == 'scissor':
        print("computer : scissor")
        print("YOU LOOSE")
        computer_score += 1
    elif user_choice == 'rock' and computer_choice == 'rock':
        print("TIE")
    elif user_choice == 'paper' and computer_choice == 'paper':
        print("TIE")
    elif user_choice == 'scissor' and computer_choice == 'scissor':
        print("TIE")
    play_again = input("Do you want to play again ? yes or no : ").lower()
    if play_again == 'yes':
        start = True
    else:
        print(f"FINAL SCORE ")
        print(f"USER SCORE : {score}")
        print(f"COMPUTER SCORE : {computer_score}")
        start = False