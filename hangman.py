import random
import string
from flask import flash

def loadWords(infile):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    flash("Loading word list from file...")
    # inFile: file
    file = open(infile, 'r', 0)
    # line: string
    line = file.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    flash("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for c in secretWord:
        if not c in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    printstr = ''
    for c in secretWord:
        if c in lettersGuessed:
            printstr = printstr + c + ' '
        else:
            printstr = printstr + '_ '
    return printstr


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alstr = ''
    for c in string.ascii_lowercase:
        if not c in lettersGuessed:
            alstr = alstr + c
    return alstr


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 0
    guessesAllowed = 8
    guessesLeft = guessesAllowed - mistakesMade
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessedWord = getGuessedWord(secretWord,lettersGuessed)
    flash("Welcome to the game Hangman!")
    flash("I am thinking of a word that is " + str(len(secretWord)) + " letters long")

    while guessesLeft > 1:
        guessesLeft = guessesAllowed - mistakesMade
        flash("You have " + str(guessesLeft) + " guesses left")
        flash("Available Letters: " + availableLetters)
        
        #this will have to change in the web version
        guess = raw_input("Please guess a letter:")
        
        guess = guess.lower()
        if (not guess in availableLetters) and (guess in lettersGuessed):
            flash("Oops! You've already guessed that letter: " + guessedWord)
        else:
            lettersGuessed.append(guess)
            availableLetters = getAvailableLetters(lettersGuessed)

            if guess in secretWord:
                guessedWord = getGuessedWord(secretWord,lettersGuessed)
                flash("Good guess: " + guessedWord)
            else:
                flash("Oops! That letter is not in my word: " + guessedWord)
                mistakesMade += 1


        if isWordGuessed(secretWord,lettersGuessed):
            flash("Congratulations, you won!")
            return None

    flash("Sorry, you ran out of guesses. The word was " + secretWord + '.')