


#Below are aspects of the program that will be required

#The game needs to explain what's going to happen with the player.
#How to play, how many guesses

#Randomness that will require us to import the random module

import random

#Take in a list of words from a text document 
#Function to return a word from the word list
#Function to hide the secret word and replace the length with underscores

#Function to print the underscores to the screen
#Return the secret word

def import_word():
   #import a list of words from text file and READ list
   #place the list of words into a variable
   #close the list of words text file.
   #in the variable, select at random a word
   word_list = open('words.txt', 'r')
   secret_word_list = word_list
   secret_word = random.choice(secret_word_list)
   #word_list.close('words.txt')
   return secret_word

print(import_word())

