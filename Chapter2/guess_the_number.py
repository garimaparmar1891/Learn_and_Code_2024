import random

def playGuessingGame():
    gameConstants = getGameConstants()
    randomTargetedNumber = generateRandomTargetedNumber(gameConstants["MIN_VALUE"], gameConstants["MAX_VALUE"])
    userGuessCount = 0
    isGuessedCorrectly = False
    while not isGuessedCorrectly:
        userInputNumber = getUserInputNumber(gameConstants["PROMPT_MESSAGE"])
        validUserInput = validateUserInput(userInputNumber, gameConstants)
        userGuessCount += 1
        if validUserInput == randomTargetedNumber:
            gameWonMessage(userGuessCount)
            isGuessedCorrectly = True
        else:
            printFeedbackMessage(validUserInput, randomTargetedNumber, gameConstants)

def getGameConstants():
    return {
        "MIN_VALUE": 1,
        "MAX_VALUE": 100,
        "PROMPT_MESSAGE": "Guess a number between 1 and 100: ",
        "INVALID_INPUT_MESSAGE": "Invalid input. Please enter a number between 1 and 100.",
        "LOW_GUESS": "Too low. Guess again.",
        "HIGH_GUESS": "Too high. Guess again."
    }

def generateRandomTargetedNumber(MIN_VALUE, MAX_VALUE):
    return random.randint(MIN_VALUE, MAX_VALUE)

def getUserInputNumber(prompt_message):
    return input(prompt_message)

def validateUserInput(userInputNumber, gameConstants):
    validInputNumber=None  
    while True:
        if isUserInputValid(userInputNumber, gameConstants["MIN_VALUE"], gameConstants["MAX_VALUE"]):
            validInputNumber =  int(userInputNumber)
            break
        else:
            print(gameConstants["INVALID_INPUT_MESSAGE"])
            userInputNumber = getUserInputNumber(gameConstants["PROMPT_MESSAGE"])
    return validInputNumber
    
def isUserInputValid(userInputNumber, MIN_VALUE, MAX_VALUE):
    return userInputNumber.isdigit() and MIN_VALUE <= int(userInputNumber) <= MAX_VALUE

def printFeedbackMessage(validUserInput, randomTargetedNumber, constants):
    if validUserInput < randomTargetedNumber:
        print(constants["LOW_GUESS"])
    elif validUserInput > randomTargetedNumber:
        print(constants["HIGH_GUESS"])

def gameWonMessage(userGuessCount):
    print(f"Congratulations! You guessed the number in {userGuessCount} guesses!")

playGuessingGame()
