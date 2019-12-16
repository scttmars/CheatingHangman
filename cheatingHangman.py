#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:41:49 2019

@author: scottmarsden
"""

def main():
    wordLength = 0
    numGuesses = 0
    showWordCount = False
    #wordList = ["ALLY", "BETA", "COOL",  "DEAL",  "ELSE", "FLEW",  "GOOD", "HOPE", "IBEX", "A"]
    mainWordList = []
    gameEnd = False
    displayWord = ""
    userGuess = ""
    guessedLetters = ""
    
    wordList = []
    file = open("/Users/scottmarsden/Desktop/dictionary.txt", "r")
    for line in file:
        line = line.strip()
        wordList.append(line)
        
    
    wordLength = startGame(wordList) 
    numGuesses = setGuesses()
    showWordCount = setVisibleWordCount()
    mainWordList = setWordListInitial(wordList,wordLength, mainWordList)
    for i in range(wordLength):
        displayWord = displayWord + "-"
    while gameEnd == False:
        
        updateGame(displayWord, numGuesses, guessedLetters, showWordCount, mainWordList)
        userGuess = makeGuess(guessedLetters)
        mainWordList = setWordList(mainWordList,userGuess, displayWord)
        displayWord = mainWordList[0]
        del mainWordList[0]
        numGuesses = numGuesses - 1
        guessedLetters = guessedLetters + ", " + userGuess
           
        gameEnd = isGameOver(numGuesses, displayWord, mainWordList)
      
    gameResult(mainWordList, displayWord)
    
    
def startGame(wordList):
    #Sets length of word and asks the user for a new input if no words are that length
    wordLengthValid = False
        
    while wordLengthValid == False :
       length = input("How long of a word would you like? ")
       try: 
           wordLength = int(length)
           for word in wordList:
                if len(word) == wordLength:
                    wordLengthValid = True
                    return wordLength
                
       except ValueError:
            print("Input a new number")

def setGuesses():
    #allows the user to choose how many guesses they would like to make 
    #checks to make sure it is an integer           
    numGuessesValid = False
        
    while numGuessesValid == False:
        num = input("How many guesses would you like? ")
        try: 
            numGuesses = int(num)
            numGuessesValid = True
            return numGuesses
        except ValueError:
            print("Please input a number")
            
def setVisibleWordCount():
    #asks the user if they would like to see how many words remain in the list
    userAnswer = input("Would you like to see the word count? (t/f)")
    if userAnswer[0] == "t" :
        return True
    else:
        return False

def setWordListInitial(wordList, wordLength, mainWordList):
    #creates the initial word list of all the words of the user selected length           
    for word in wordList:
        if len(word) == wordLength:
            mainWordList.append(word)
    return mainWordList
    #set display word to _ and length set above
        
    
def updateGame(displayWord, numGuesses, guessedLetters, showWordCount, mainWordList):
    #updates display between turns for the user to see
    print(displayWord)
    print("You have " + str(numGuesses) + " guesses remaining")
    print("Letters that have been guessed: " + guessedLetters)
    if showWordCount:
        print("Remaining words: " + str(len(mainWordList)))
    
    
def isGameOver(numGuesses, displayWord, mainWordList):
    #Checks to see if any end game conditions are met
    if displayWord == mainWordList[0]:
        return True
    elif numGuesses == 0:
        return True
    else:
        return False
        
def makeGuess(guessedLetters):
    #checks to make sure the users guess is a letter 
    validLetter = False
    while validLetter == False:
        letter = input("Please type a letter to guess: ")
        if letter not in guessedLetters:
            if letter[0].isalpha():
                validLetter = True
                return letter[0]
            
def setWordList(mainWordList, userGuess, displayWord):
    
    families = {}
    #check where letter is in the word and create a family based on that
    for word in mainWordList:
        if userGuess not in word:
            if displayWord in families:
                families[displayWord] = families[displayWord] + "," + word
            else:
                families[displayWord] = word
            
        else:
            newWord = displayWord
            index = word.find(userGuess)
            
            currentWord = []
            for letter in word:
                currentWord.append(letter)
            
            
            displayList = []
            for letter in displayWord:
                displayList.append(letter)
             
            for i in range(0,len(currentWord)):
                if userGuess == currentWord[i]:
                    displayList[i] = userGuess
                    newWord = "".join(displayList)
            
            #creates families for each of the possible 
            if newWord in families:
                families[newWord] = families[newWord] + "," + word
            else:
                families[newWord] = word
        
    #checks for largest family then returns that family with the new display word
    longestKey = 0 
    keyName = ""    
    for key in families.keys():
        if len(families[key]) > longestKey:
            keyName = key
            longestKey = len(families[key])
    displayWord = keyName
    mainWordList = families[keyName].split(",")
    mainWordList.insert(0, displayWord)
    return mainWordList
    
    
def gameResult(mainWordList,displayWord):
    #displays the result of the game based on what has occured to end it
    if displayWord == mainWordList[0]:
        print("You win! The word was: " + mainWordList[0])
    else:
        print("You lose! The word was: " + mainWordList[0])
    
    
    
    
main()