#HangMan

import os
import random


with open("wordlist.txt")as words:          #converting the txt file to a list
    wordList = words.read().split()

word = random.choice(wordList)              #picking a random word from the list
reveal = list(len(word) * "_")
lenWord = len(word)                         #a variable containing the value of the length of the randomly chosen word

gameWon = False                             #setting the gameWon variable to false at the start of the game

print("Welcome to Hangman!")
gameDifficulty = input("Set your difficulty level by typing 'easy', 'medium', or 'hard': ")

#-----------------------------
if gameDifficulty == "easy":
    diffValue = 12
if gameDifficulty == "medium":              #Game difficulty script
    diffValue = 8
if gameDifficulty == "hard":
    diffValue = 4
#-----------------------------

lives = lenWord + diffValue                 #simple addition to calculate the amount of lives to give you depending on the length of the word and the chosen difficulty

print("You have ", lives, " lives")         #tells you how many lives you have at the start of the game

while gameWon == False and lives > 0:
    print(reveal)
    guess = input("What is your guess? ")
    if guess == word:
        gameWon == True
    if len(guess) == 1 and guess in word:
        for i in range(0, len(word)):
            letter = word[i]
            if guess == letter:
                reveal[i] = guess
    if "_" not in reveal:
        gameWon = True
        if gameWon == True:
            print(reveal)
            print("You won")
    else:
        lives = lives - 1
        if lives < 1:
            print("Game over, you lose :( ")
            
        

       
       
   

                
             

          



        
    

