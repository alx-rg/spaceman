#Below are aspects of the program that will be required

#The game needs to explain what's going to happen with the player.
#How to play, how many guesses

#Randomness that will require us to import the random module

#Take in a list of words from a text document 
#Function to return a word from the word list
#Function to hide the secret word and replace the length with underscores

#Function to print the underscores to the screen
#Return the secret word

import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    #IMPORT a list of words from text file and READ list
    f = open('words.txt', 'r')
    #SAVE the list of words into a variable (words_list)
    words_list = f.readlines()
    #CLOSE the list of words text file.
    f.close()
    #
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    #SELECT a word at random in the variable (words_list) 
    secret_word = random.choice(words_list)
    #STORE the secret_word in the function
    return secret_word

#Test that we are getting a random word

#print(load_word())

#FUNCTION that checks if all the letters guessed are the letters in the secret word
def is_word_guessed(secret_word, letters_guessed):
    #VERIFY if the all the letters guessed by user are in the secret word (Victory condition)
    if letters_guessed in secret_word:
    #IF all the letters used are in the secret word THEN 
        #Return TRUE
        return True
    #ELSE if the letters are not all in the secret work THEN
        #Return FALSE
    else:
        return False
    #ENDIF


    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
 #   pass

#FUNCTION used to show string of letters guessed so far and underscores for letters yet to be guessed
def get_guessed_words(secret_word, letters_guessed):
    #SAVE string of letters and _ in a variable called "guess"
    guess=''
    #DO for each letter in the secret word 
    for i in range(len(secret_word)):
    #IF the letter guessed is in the secret word THEN
        #Add the letter to the guess character string
        if secret_word[i] in letters_guessed:
            guess += secret_word[i]
    #ELSE
        #add an underscore "_" to the character string
        else:
            guess += '_'
    #DISPLAY the resulting character string with the letters and underscores 
    return guess    



'''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    # secret_word = 'apple'
    # letters_guessed = ['a', 'l', 'e']
    # get_guessed_words(secret_word, letters_guessed)
    # print(secret_word)
    # print(letters_guessed)
    # print(get_guessed_words)
#    pass

#FUNCTION that checks if the letter guessed by user is in the secret word
def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
    #CHECK if the letter guessed by user is in the secret word
        return True
    #IF yes THEN 
        #Return TRUE
    else:
    #ELSE if the letter guessed is not in the secret work THEN
        #Return FALSE
        return False
    #ENDIF


'''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

#    pass

#FUNCTION that checks the alphabet against letters already guessed and returns the letters that are still available to be used

def letters_not_guessed_yet(letters_guessed):
    #INITIALIZE an empty variable that will be used to accept the letters that have not been used
    letters_left = ''
    #FOR the letters in the alphabet
    for letter in 'abcdefghijklmnopqrstuv':
        #IF the letters of the alphabet are not already used THEN
            #STORE the letters that have not been used in a the empty variable above containing so that it now contains the string of letters
        if  letter not in letters_guessed:
            letters_left += letter
    #RETURN the string the string of letters that have not been guessed yet out of the function
    return letters_left

def game_win_condition(secret_word, letters_guessed):
    count = 0
    for letter in letters_guessed:
        if letter in secret_word:
            count += 1
            if count == len(secret_word):
                return True
            else:
                return False

#def spaceman(secret_word):
'''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
#   




def spaceman(secret_word):
    letters_guessed = ['']
    guess_times = 7

    print('Welcome to Spaceman, you have 7 guesses to figure out what word I am thinking of. Good luck')
    print('\n')

    word_is_x_letters_long = len(secret_word)

    print(f'The word in question is {word_is_x_letters_long} letters long')
    print('\n')

    while not (game_win_condition(secret_word, letters_not_guessed_yet(letters_guessed))) and guess_times != 0:
        print(f'You have {guess_times} guesses left to get the full word.')
        print(f'Letters left to guess are: {letters_not_guessed_yet(letters_guessed)}')
        print('\n')
        guess_input = input('Please guess a letter: ')
        guess = guess_input.lower()

        if guess in letters_guessed:
            print(f'Choose a different letter, you already used this one {get_guessed_words(secret_word, letters_guessed)}')
            print('\n')

        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print('Please choose a letter, that is not a letter')
            print('\n')

        elif is_guess_in_word(guess, secret_word):
            letters_guessed += guess
            print(f'Good guess this is what you have: {get_guessed_words(secret_word, letters_guessed)}')
            print('\n')

        else:
            letters_guessed += guess
            print (f'That letter is not in the word, try again : {get_guessed_words(secret_word, letters_guessed)}')
            print('\n')
            guess_times -= 1

    if guess_times == 0:
        print (f'No more guesses, the word was: {secret_word}')
        print ('\n')
    else:
        print ("Congratulations!")
        print ('\n')
    


        

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost




    #These function calls that will start the game


""" print ('\n')
print(load_word())
testwordtoguess=load_word

iswordguessedtest = is_word_guessed ('testwordtoguess', 'abcdefghijklmnopqrstuvwxyz') #TRUE
print(iswordguessedtest)
print ('above should be true')

iswordguessedtest = is_word_guessed ('orange', 'apple') #FALSE
print(iswordguessedtest)
print('above should be false')

isguessinwordtest = is_guess_in_word('a', 'apple')
print(isguessinwordtest)

#apple
getguesswordstest = get_guessed_words('apple', 'abcdefg')
print(getguesswordstest)

lettersfortest = letters_not_guessed_yet('abcdedf')
print(lettersfortest) """

#secret_word = load_word()
#print (secret_word)
spaceman(load_word())