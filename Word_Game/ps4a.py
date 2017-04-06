# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "/Users/Singh/Desktop/singh/resumee/p_set 4/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print ("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    l=len(word)
    if l==0:
        return 0
    i=0
    score=0
    while i<l:
        temp=word[i]
        sc=SCRABBLE_LETTER_VALUES[temp]
        score=score+sc
        i=i+1

    score=score*l    

    if l==n:
        score=score+50

    return score   



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    strn=''
    for letter in hand.keys():
        for j in range(hand[letter]):
            strn=strn+' '+letter
                           # print all on the same line
    return strn                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = int(n / 3)
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    i=0
    l=len(word)
    han=hand.copy()
    while i<l:
        c=word[i]
        han[c] = han.get(c, 0)-1
        i=i+1
    return han    



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    l=len(word)
    if l==0:
        return False
    i=0
    
    han=hand.copy()
    while i<l:
        c=word[i]
        if c in han:
            han[c] = han.get(c, 0)-1
            val=han.get(c)
            if val==0:
              del han[c]
                     
              
            
            i=i+1
        else:
            return False
    if i==l and word in wordList:
        return True
    else:
      return False


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    k=0
    for letter in hand.keys():
        n=hand[letter]
        k=k+n
             
    return k





def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    flag1=True
    score=0
    sco=0
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    while flag1:
    
        # Display the hand
        #dish=displayHand(hand)
        
        #print('Current Hand:'+ dish)
        strn=''
        for letter in hand.keys():
          for j in range(hand[letter]):
            strn=strn+' '+letter
                           # print all on the same line
        print('Current Hand:'+strn)
        
        
        
        # Ask user for input
        word=input('Enter word, or a "." to indicate that you are finished:')
        
        # If the input is a single period:
        if word =='.':
            print('Goodbye! Total score:'+str(score)+'points.')
            flag1=False
            break
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        flag2=isValidWord(word, hand, wordList)
        
            # If the word is not valid:
        if flag2==False:
            print('Invalid word, please try again')
            print('__________________________________')
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):
                  
        if isValidWord(word, hand, wordList)==True: 
            sco=getWordScore(word, n)
            score=score+sco      
        
                
            print( word +'earned'+ str(sco)+ 'points. Total:'+str(score)+ 'points.')
            print('__________________________________')

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand
            hand=updateHand(hand, word)
            st=''
            for letter in hand.keys():
              for j in range(hand[letter]):
                st=st+' '+letter
                           
        
           
            if st=='':
                print('Run out of letters. Total score:'+str(score)+'points')
                break
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    print ("playGame not yet implemented.") # <-- Remove this line when you code the function
    g=0
   
    flag=True
    while flag:
        foo=input('Enter n to deal a new hand, r to replay the last hand, or e to end game')
        if foo=='r' and g==0:
            print('You have not played a hand yet. Please play a new hand first!')
        if foo=='r' and g==1:
            playHand(hand, wordList, HAND_SIZE)
            
        if foo=='n'  or foo=='e':
          if foo=='n':
            hand=dealHand(HAND_SIZE)  
            playHand(hand, wordList, HAND_SIZE)
            g=1
          if foo=='e':
            flag=False
            break
        if foo!='n' and foo!='r' and foo!='e':
            print('Invalid command.')
        
        
    
            
   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
