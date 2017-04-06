# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Volumes/My Passport/New folder (2)/_nfsmvpatch1.3/my study/python/p_set 3/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    # Write your Python code here
# Write your Python code here
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    l=len(secretWord)
    i=0
    n=len(lettersGuessed)
    o=0
    if n==0:
     return False
   
   
    while o < len(lettersGuessed):
        cd = lettersGuessed[o]
        ch=secretWord[i]
        if (ch == cd):
          i=i+1
          o=0
        if ch != cd:  
          o=o+1
          if o>=n:
            return False
            break
        if i>=len(secretWord):
          return True
          break
       


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    l=len(secretWord)
    i=0
    n=len(lettersGuessed)
    o=0
    str=''
    if n==0:
      while i<l:
        str=str+'_'
        i=i+1
      return str
   
   
    while o < len(lettersGuessed):
        cd = lettersGuessed[o]
        ch=secretWord[i]
        if (ch == cd):
          i=i+1
          o=0
          str=str+ch
        if ch != cd:  
          o=o+1
          if o>=n:
            i=i+1
            str=str+'_'
            o=0
          if(i==l):
            return str
            break
            
        if i>=len(secretWord):
          return str
          break
   



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    l=len(lst)
    i=0
    n=len(lettersGuessed)
    o=0
    str=''
    if n==0:
      while i<l:
        str=str+lst[i]
        i=i+1
      return str  
   
   
    while o < len(lettersGuessed):
        cd = lettersGuessed[o]
        ch=lst[i]
        if (ch == cd):
          i=i+1
          o=0
          str=str+''
        if ch != cd:  
          o=o+1
          if o>=n:
            i=i+1
            str=str+ch
            o=0
          if(i==l):
            return str
            break
            
        if i>=len(lst):
          return str
          break


    

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
    # FILL IN YOUR CODE HERE..
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
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    l=len(secretWord)
    print('I am thinking of a word that is'+str(l)+'letters long')
    
    i=8
    lettersGuessed=[]
    get=''
    while i>0:
        
        print('-----------')
        print('You have'+str(i)+'guesses left.')
        print('Available letters:'+getAvailableLetters(lettersGuessed))
        ln=input('Please guess a letter:')
        ln=ln.lower()
       
        #print('Please guess a letter:'+str(ln))
        lettersGuessed.append(ln)
        get=getGuessedWord(secretWord, lettersGuessed)
        lettersGuessed.remove(ln)
        
        if ln in lettersGuessed:
            print("Oops! You've already guessed that letter:"+get)
        else:   
          if ln in get:
            print('Good guess:'+get)
            lettersGuessed.append(ln)
            
          else:
            print('Oops! That letter is not in my word:'+get)
            lettersGuessed.append(ln)
            
            i=i-1
        if(isWordGuessed(secretWord,lettersGuessed)):
             print('------------')
             print('Congratulations, you won!')
             break

        else :
            if i==0:
                
             print('------------')
             print('Sorry, you ran out of guesses. The word was  --' + secretWord)
             break

             
               
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
