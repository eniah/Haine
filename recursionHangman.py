# Haine Kim - hainek42@gmail.com
# Text file of 1000 common words courtesy of https://gist.github.com/deekayen/4148741

import random
import os

# Variable 
# List with the correct order of letters
originalWord = []
# User's previous correct guesses
goodGuessList = []
# User's previous incorrect guesses
badGuessList = []
# List containing letters of the answer
answerList = []

# Functions
# Print some introduction
def intro():
  print("\nThis is a Hangman game. I've chosen a word for you. Can you guess what it is?\n")

# Print simple rules
def rules():
  print("Type your one-letter guess and press enter to see if my word includes your letter.")
  print("You can try as many times as you want, but you can only be wrong 7 times.")

# Requests user input through cmd, value stored as string
def requestIn():
  print("\nPlease type a letter and press enter.\n")
  guessString = input()
  return guessString

# Check if input is valid letter
def isAlphabet(guess):
  # If input is valid letter, return True and keep input 
  if guess.isalpha() == True:
    return True
  # If input invalid, wipe guessString and return False
  else:
    print("That's not a letter from the alphabet!")
    return False

# Check if input is valid length, only 1 char allowed at a time
def isOneLetter(guess):
  # If guess 1 char, return True, keep input
  if len(guess) == 1:
    return True
  # If guess longer than 1 char, wipe guessString and return False
  else:
    print("Your guess is not a single letter!")
    return False

# Once input checked valid, check if letter is in word
def validGuess(guess):
  # Clear screen after receiving input
  os.system('cls')  
  # If guess is alphabet and single letter
  if (isOneLetter(guess) and isAlphabet(guess)) == True:
    # If guess same as a previous try
    if (guess in goodGuessList) or (guess in badGuessList):
      print("You've already guessed " + guess + ". Please choose another letter.\n")
    # Otherwise, store the guess in an array of correct guesses if correct
    elif (guess in answerList):
      for letters in answerList:
        if (letters == guess):
          goodGuessList.append(guess)
      goodGuessList.sort()
      remaining = 7 - len(badGuessList)
      if (len(badGuessList) == 6):
        print("Nice! One life left.")
      else:
        print("\nGood guess :) " + str(remaining) + " lives remaining.\n")
    # If previous checks weren't triggered, it's a wrong guess
    else:
      badGuessList.append(guess)
      badGuessList.sort()
      remaining = 7 - len(badGuessList)
      if (remaining == 1):
        print("Wrong. Last try.\n")
      else:
        print("Wrong. " + str(remaining) + " lives left.\n")
  # If guess not alphabet nor single letter
  else:
    print("I won't count that as a wrong guess. Try again.")
    # Store the guess in different array

# Generate random number between 1-1000
def getRandomNum():
  return random.randint(1,1000)

# Open text file, choose word
def getWord(ranNum):
  # Open file for reading
  theFile = open('1-1000.txt', 'r')
  # Dump all lines into a list
  tempListWords = theFile.readlines()
  word = tempListWords[ranNum+1]
  # Close file
  theFile.close()
  # Return random word
  return word

# Convert the string word into a list of letters, then sorts list alphabetically
def wordIntoList(wordString):
  print("Chosen word is: " + wordString)
  for letters in wordString:
    # If letter not empty line char
    if (letters != '\n'): 
      # And if letter not apostrophe
      if  (letters != '\''):
        # Put in list of answers
        answerList.append(letters)
      # If not empty line (apostrophe is fair game) add to original word list
      originalWord.append(letters)
  answerList.sort()

# Print previous guesses
def printGuesses(goodList, badList):
  # If goodGuessList not empty
  if (len(goodList) != 0):
    print("You've guessed correctly: ")
    for letters in goodList:
      print(letters + " ", end = ' ')
    print()
  #If badGuessList not empty
  if (len(badList) != 0):
    print("Your wrong guesses: ")
    for letters in badList:
      print(letters + " ", end = ' ')
    print()
  print()

# Show the progression of word
def wordProgress():
  print()
  for letters in originalWord:
    if (letters in goodGuessList):
      print(letters + " ", end = ' ')
    else:
      print("_", end = ' ')

# Show the progression of hangman
def showMan():
  if (len(badGuessList) == 0):
    print("   __________")
    print("  |       ")
    print("  |       ")
    print("  |       ")
    print("  |       ")
    print("  |       ")
    print("__|_____  ")
  if (len(badGuessList) == 1):
    print("   __________")
    print("  |       ")
    print("  |       O")
    print("  |       ")
    print("  |       ")
    print("  |       ")
    print("__|_____  ")
  if (len(badGuessList) == 2):
    print("   __________")
    print("  |       ")
    print("  |       O")
    print("  |       |")
    print("  |       ")
    print("  |       ")
    print("__|_____  ")
  if (len(badGuessList) == 3):
    print("   __________")
    print("  |       ")
    print("  |       O")
    print("  |      /|")
    print("  |       ")
    print("  |       ")
    print("__|_____  ")
  if (len(badGuessList) == 4):
    print("   __________")
    print("  |       ")
    print("  |       O")
    print("  |      /|\ ")
    print("  |       ")
    print("  |       ")
    print("__|_____  ")
  if (len(badGuessList) == 5):
    print("   __________")
    print("  |       ")
    print("  |       O")
    print("  |      /|\ ")
    print("  |      /")
    print("  |       ")
    print("__|_____  ")
  if (len(badGuessList) == 6):
    print("   __________")
    print("  |       ")
    print("  |       O")
    print("  |      /|\ ")
    print("  |      / \ ")
    print("  |       ")
    print("__|_____")

# Runs hangman recursively, stopping if number of wrong guesses exceeds 7 or if word has been guessed correctly
def hangman():
  validGuess(requestIn())
  if (len(badGuessList) >= 7):
    print("   __________")
    print("  |       I")
    print("  |       O")
    print("  |      /|\ ")
    print("  |      / \ ")
    print("  |       ")
    print("__|_____")
    print("You lose!")
  elif (sorted(answerList) == sorted(goodGuessList)):
    os.system('cls')  
    print("You win!")
  else:
    printGuesses(goodGuessList, badGuessList)
    showMan()
    wordProgress()
    hangman()
  
# Main, sort of
intro()
rules()
wordIntoList(getWord(getRandomNum()))
hangman()
print("Your word was :", end = ' ')
print()
for letters in originalWord:
  print(letters, end = ' ')