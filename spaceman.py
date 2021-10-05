
import random

def load_word():

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

#FUNCTION that checks if all the letters guessed are the the letters in the secret word (Victory condition)
def is_word_guessed(secret_word, letters_guessed):
#FOR each individual letter in the secret word 
    for character in secret_word:
    #IF any letter from the secret word are still in the letter left to be guessed THEN
    #RETURN False (Meaning you haven't won yet so keep guessing) 
        if character not in letters_guessed:
            
            return False
    #ELSE Return True (Meaning you guessed all the letter so you won!)
    return True
    

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

#FUNCTION that controls the game of spaceman and brings in all the functions into one.
def spaceman(secret_word):

    print(secret_word)

    #SET and empty list for the letters that the user will guess
    letters_guessed = ['']
    #SET the number of guesses allowed by the user to 7
    guess_times = 7

    #in this code any '\n' is a line break
    print('\n')
    #DISPLAY instructions for the user to understand the game 
    print('Welcome to Spaceman, the object of the game is to guess the secret word, doing so one letter at a time.')
    print('You have 7 guesses to figure out what word I am thinking of. Good luck!')
    print('\n')

    word_is_x_letters_long = len(secret_word)
    #DISPLAY the number corresponding to the length of the word. i.e "Apple" is 5 letters long
    print(f'The word in question is {word_is_x_letters_long} letters long')
    print('\n')
    
    #SET a variable to true. This variable determines if the player wants to play again, if it is false, then the player has said "n". 
    play_repeat = True
    #DOWHILE True = play the game again
    while play_repeat:
    
        #DOWHILE False if the letters guessed do not match the secret word, Keep playing. AND if the guess is not equal to 0, Keep playing
        while is_word_guessed(secret_word, letters_guessed) is False and guess_times != 0:
            #DISPLAY the amount of guesses left to find the secret word.
            print(f'You have {guess_times} guesses left to get the secret word.')
            #DISPLAY the letters that are left for the player to use.
            print(f'Letters left to guess are: {letters_not_guessed_yet(letters_guessed)}')
            print('\n')
            #PROMPT the user to guess a letter
            guess_input = input('Please guess a letter: ')
            #GET user input and save it in a variable
            #SAVE / TRANSFORM user input regardless of upper or lowercase to a lowercase. 
            guess = guess_input.lower()

            #IF the letter guessed by user is already one of the letters previously guessed THEN
            if guess in letters_guessed:
                #DISPLAY a message letting user know that they already used the letter.
                print(f'Choose a different letter, you already used this one {get_guessed_words(secret_word, letters_guessed)}')
                print('\n')

            #ELSE IF the guess is not a letter of the alphabet THEN
            elif guess not in "abcdefghijklmnopqrstuvwxyz":
                #DISPLAY a message informing them to chose a letter
                print('Please choose a letter, that is not a letter')
                print('\n')

            #ELSE IF the letter is in the secret word and hasn't been used yet THEN
            elif is_guess_in_word(guess, secret_word):
                #ADD the letter guessed into the list of letters that have been guessed so far
                letters_guessed += guess
                #DISPLAY a well done for guessing the right letter message
                print(f'Good guess this is what you have: {get_guessed_words(secret_word, letters_guessed)}')
                print('\n')

            #ELSE the letter is not in the secret word THEN
            else:
                #ADD the letter guessed into the list of letters that have been guessed so far
                letters_guessed += guess
                #DISPLAY a message that this is not a letter in the word and to guess again
                print (f'That letter is not in the word, try again : {get_guessed_words(secret_word, letters_guessed)}')
                print('\n')
                #SUBSTRACT 1 from the total number of guesses left
                guess_times -= 1

        #IF the number of guesses reaches 0 THEN
        if guess_times == 0:
            #DISPLAY that the user lost, and OUTPUT the secret word THEN
            print (f'OH NO, you have no more guesses, the word was: {secret_word}')
            print ('\n')
            #BREAK out of the loop
            break
        #ELSE the number of guesses was above 0 and we found the word
        else:
            #DISPLAY a celebratory message for the use and OUTPUT the secret word again THEN
            print (f'Congratulations! You WIN! The secret word was "{secret_word}"!')
            print ('\n')
            break
        #ENDIF
    
    #PROMPT the user to enter 'y' to play again or 'n' to stop playing
    user_answer = input('would you like to play spaceman again? (y/n) ')
    #GET user's answer
    #IF user answered 'y' THEN
    if user_answer == 'y':
        #RETURN True
        play_repeat = True
        #INITIALIZE the spaceman game once again
        spaceman(load_word())
    #ELSE the answer was 'n'
    else:
        #DISPLAY a thank you for playing message
        print('Thanks for playing, bye now!')
        print ('\n')
        #RETURN False breaking us out of the WHILE loop and exiting
        play_repeat = False

#CALLS / RUNS the spaceman game and includes the secret word.
spaceman(load_word())
        
    #DONE-TODO: show the player information about the game according to the project spec - DONE
    #DONE-TODO: Ask the player to guess one letter per round and check that it is only one letter - DONE
    #DONE-TODO: Check if the guessed letter is in the secret or not and give the player feedback - DONE
    #DONE-TODO: show the guessed word so far - DONE
    #DONE-TODO: check if the game has been won or lost - DONE

""" 
TESTING THE FUNCTIONS TO CONFIRM THE OUTPUT WAS AS EXPECTED
print ('\n')
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
print(lettersfortest) 

secret_word = load_word()
print (secret_word)

"""

