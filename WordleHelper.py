import random

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def filterGreens(inFilter, validWords):
    count = 0
    for letter in inFilter:        
        if letter != '-':
            validLetters.add(letter)
            newValidWords = set()
            for word in validWords:
                # if letter in position count is the same as the letter we are looking at
                if word[count] == letter:
                    newValidWords.add(word)
            # set old set to new set
            validWords = newValidWords
        # increment as we scan each letter
        count = count + 1
    return validWords

def filterYellows(inFilter, validWords):
    # First part goes by each letter in inFilter and copys all words that have that letter in a spot other than count
    count = 0
    newValidWords = set()
    for letter in inFilter:
        if letter != '-':
            validLetters.add(letter)
            # for each word in the set
            for word in validWords:                
                wcount = 0
                # iterate through word
                for wletter in word:
                    # if it contains letter, and it is not in position count
                    if wletter == letter and wcount != count:
                        newValidWords.add(word)            
        count = count + 1

    # generate set of all filter letters
    filterLetters = set()
    for letter in inFilter:
        if letter != '-':
            filterLetters.add(letter)

    # need to test to see if newValidWords is empty. Can be caused by having all dashes filter
    # if empty, copy validWords over
    if len(newValidWords) == 0:
        newValidWords = validWords

    newValidWords2 = newValidWords.copy()
    for word in newValidWords:
        for l in filterLetters:
            if l not in word:
                newValidWords2.remove(word)
                break
            
    return newValidWords2

def filterGreys(inFilter, validWords):
    # generate set of all letters
    filterLetters = set()
    for letter in inFilter:
        if letter != '-' and letter not in validLetters:
            filterLetters.add(letter)

    newValidWords = validWords.copy()
    
    # iterate through all words
    for word in validWords:
        # iterate through filter letters
        for l in filterLetters:
            # if word contains l, remove from validWords
            if l in word:
                newValidWords.remove(word)
                break

    return newValidWords


def printHelp():
    print()
    print('possible commands: ')
    print('"e": enter data')
    print('"r": pick another word to try')
    print('"p": print all possible words')
    print('"?" or "help": print this help page')
    print('"q": quit program')
    print('Note: When entering data, use the format: (--g--)')
    print()
            
if __name__ == '__main__':
    print('Wordle Helper')
    validLetters = set()
    
    words = load_words()
    validWords = set()
    for word in words:
        if len(word) == 5:
            validWords.add(word)

    # Setup complete, begin program
    printHelp()
    while(True):        
        userChoice = input('enter command: ')

        if userChoice == 'e':
            greens = input('Enter greens:  ')
            print(greens)
            yellows = input('Enter yellows:  ')
            print(yellows)
            greys = input('Enter greys:  ')
            print(greys)    

            print('Proccessing...')            
            validWords = filterGreens(greens, validWords)
            validWords = filterYellows(yellows, validWords)
            validWords = filterGreys(greys, validWords)
            print('Possible words:', len(validWords))
            print(random.choice(tuple(validWords)))

        elif userChoice == 'r':
            print(random.choice(tuple(validWords)))

        elif userChoice == 'q':
            break

        elif userChoice == 'p':
            print(validWords)

        elif userChoice == '?' or 'help':
            printHelp()
        
        else:
            print('invalid command. Please try again.')
