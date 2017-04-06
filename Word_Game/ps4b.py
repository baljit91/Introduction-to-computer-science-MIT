from ps4a import *
import time
def isWordInHand(word, hand):
      wordFreq = getFrequencyDict(word)
      for key in wordFreq:
        if wordFreq[key] > hand.get(key, 0):
          return False
      return True

#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    """score=0

    # Create a new variable to store the best word seen so far (initially None)
    bword=''
    i=0
    st=''
    j=0
    for letter in hand.keys():
      for j in range(hand[letter]):
        st=st+' '+letter
    n=len(st)            

    # For each word in the wordList
    while i<len(wordList):
        bword=wordList[i]
        st=''
        for letter in hand.keys():
          for j in range(hand[letter]):
            st=st+' '+letter
                

        while j<len(bword):
            if bword[j] in st:
                j=j+1
                if j==len(bword):
                    sc=getWordScore(bword, n)
                    if sc>score:
                      score=sc
                    
            else:
                j=len(bword)+1
        


    return score    
            
    

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found."""

    
    # Create a new variable to store the maximum score seen so far (initially 0)
    """
Given a hand and a wordList, find the word that gives
the maximum value score, and return it.

This word should be calculated by considering all the words
in the wordList.

If no words in the wordList can be made from the hand, return None.

hand: dictionary (string -> int)
wordList: list (string)
returns: string or None
"""
    def isWordInHand(word, hand):
        wordFreq = getFrequencyDict(word)
        for key in wordFreq:
            if wordFreq[key] > hand.get(key, 0):
                return False
        return True
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    score = 0
    # Create a new variable to store the best word seen so far (initially None)
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isWordInHand (word, hand):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    score=0
    while True:
    
        # Display the hand
        #dish=displayHand(hand)
        
        #print('Current Hand:'+ dish)
        strn=''
        for letter in hand.keys():
          for j in range(hand[letter]):
            strn=strn+' '+letter
                           # print all on the same line
        print('Current Hand:'+strn)
        

        word=compChooseWord(hand, wordList, n)
        if word == None:
            print ("Total score: "+str(score)+ "points.")
            break       
        if isValidWord(word, hand, wordList)==False:
            break
        sco=getWordScore(word, n)
        score=score+sco
        hand=updateHand(hand, word)
        
                
        print('"'+word+'"' +'   earned'+ str(sco)+ 'points. Total:'+str(score)+ 'points.')
        st=''
        for letter in hand.keys():
          for j in range(hand[letter]):
            st=st+' '+letter
                           
        
           
        if len(st)==0:
            return print('Total score:'+str(score)+'points')
            
            break
            
     
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print ("playGame not yet implemented.") # <-- Remove this when you code this function
    g=0
   
    flag=True
    while flag:
        foo=input('Enter n to deal a new hand, r to replay the last hand, or e to end game')
        if foo=='r' and g==0:
            print('You have not played a hand yet. Please play a new hand first!')
        if foo=='r' and g==1:
            fo1=input('Enter u to have yourself play, c to have the computer play:')
            if fo1=='u':
                
              playHand(hand, wordList, HAND_SIZE)
              
            if fo1=='c':
                
              compPlayHand(hand, wordList, HAND_SIZE)
          
            
        if foo=='n'  or foo=='e':
          if foo=='n':
            fo=input('Enter u to have yourself play, c to have the computer play:')
            if fo=='u':
              hand=dealHand(HAND_SIZE)  
              playHand(hand, wordList, HAND_SIZE)
              g=1
            if fo=='c':
                hand=dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
                g=1

            if  fo!='u' and fo!='c' :
              print('Invalid command.')    
                
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


