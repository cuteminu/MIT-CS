# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    for char in secret_word :
        for letter in letters_guessed :
            if char == letter :
                i += 1
                break
    if i == len(secret_word) :
        return True
    else :
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for char in secret_word :
        count = 0
        for letter in letters_guessed :
            count += 1
            if char == letter :
                result = result + char
                break
            if count == len(letters_guessed) :
                result = result + "_ "
    return result



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = string.ascii_lowercase
    for letter in letters_guessed :
        for index in range(len(result)) :
            if result[index] == letter :
                result = result[:index] + result[index+1:len(result)]
                break
    return result

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman! \nI am thinking of a word that is %d letters long."%(len(secret_word)))
    print("-------------")
    letters_guessed = ["$"] # Random Initial String -> Any Better Way?
    guess = 6
    warning = 3
    previous_guessed_word = get_guessed_word(secret_word, letters_guessed)
    letters_guessed.remove("$") 
    while guess >= 1 and not is_word_guessed(secret_word, letters_guessed) :
        print("You have %d guesses left." %(guess))
        print("Available letters:", get_available_letters(letters_guessed))
        letter_input = input("Please guess a letter:") 
        if not letter_input.isalpha() :
            if warning > 0 :
                warning -= 1
            else : 
                guess -= 1
            print("Oops! That is not a valid letter. You have %d warnings left:" %(warning), get_guessed_word(secret_word, letters_guessed)) 
            print("---------------")
        else :
            letter_input = letter_input.lower()
            same = False
            # for char in letters_guessed :
            #     if char == letter_input :
            #         same = True
            if letter_input in letters_guessed :
                same = True
            if same : 
                if warning > 0 :
                    warning -= 1
                else : 
                    guess -= 1
                print("Oops! You've already guessed that letter. You now have %d warnings" %(warning), get_guessed_word(secret_word, letters_guessed))
                print("-----------------")
            else :
                letters_guessed.append(letter_input)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if previous_guessed_word != guessed_word :
                    print("Good guess:", guessed_word)
                    print("-----------------")
                else :
                    guess -= 1
                    vowel = ['a', 'e', 'i', 'o']
                    # for char in vowel :
                    #     if char == letter_input :
                    #         guess -= 1
                    #         break
                    if letter_input in vowel :
                        guess -= 1
                    print("Oops! That letter is not in my word:", guessed_word)
                    print("----------------")
                previous_guessed_word = guessed_word
    if guess <= 0 :
        print("Sorry, you ran out of guesses. The word was", secret_word)
    else :
        print("Congratulations, you won!")
        score = guess * len(secret_word)
        print("Your total score for this game is:", score)
    
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = True
    # Get rid of the spaces in the word. Can it be done with strip()?
    word = ""
    for char in my_word :
        if char != " " :
            word += char
    letters_word = []
    for char in word :
        if char != "_":
            letters_word.append(char)
    if len(word) != len(other_word) :
        return False
    for i in range(len(word)) :
        char = word[i]
        if char != "_" :
            if char != other_word[i] :
                result = False
        else : 
            if other_word[i] in letters_word :
                result = False 
    return result


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ""
    for word in wordlist :
        if match_with_gaps(my_word, word) :
            possible_matches += word + " "
    if possible_matches == "" :
        print("No matches found")
    else :
        print(possible_matches)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman! \nI am thinking of a word that is %d letters long."%(len(secret_word)))
    print("-------------")
    letters_guessed = ["$"] # Random Initial String -> Any Better Way?
    guess = 6
    warning = 3
    previous_guessed_word = get_guessed_word(secret_word, letters_guessed)
    letters_guessed.remove("$") 
    while guess >= 1 and not is_word_guessed(secret_word, letters_guessed) :
        print("You have %d guesses left." %(guess))
        print("Available letters:", get_available_letters(letters_guessed))
        letter_input = input("Please guess a letter:") 
        if not letter_input.isalpha() :
            if letter_input == "*" :
                print("Possible word matches are:")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else :
                if warning > 0 :
                    warning -= 1
                else : 
                    guess -= 1
                print("Oops! That is not a valid letter. You have %d warnings left:" %(warning), get_guessed_word(secret_word, letters_guessed)) 
            print("---------------")
        else :
            letter_input = letter_input.lower()
            same = False
            # for char in letters_guessed :
            #     if char == letter_input :
            #         same = True
            if letter_input in letters_guessed :
                same = True
            if same : 
                if warning > 0 :
                    warning -= 1
                else : 
                    guess -= 1
                print("Oops! You've already guessed that letter. You now have %d warnings" %(warning), get_guessed_word(secret_word, letters_guessed))
                print("-----------------")
            else :
                letters_guessed.append(letter_input)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if previous_guessed_word != guessed_word :
                    print("Good guess:", guessed_word)
                    print("-----------------")
                else :
                    guess -= 1
                    vowel = ['a', 'e', 'i', 'o']
                    # for char in vowel :
                    #     if char == letter_input :
                    #         guess -= 1
                    #         break
                    if letter_input in vowel :
                        guess -= 1
                    print("Oops! That letter is not in my word:", guessed_word)
                    print("----------------")
                previous_guessed_word = guessed_word
    if guess <= 0 :
        print("Sorry, you ran out of guesses. The word was", secret_word)
    else :
        print("Congratulations, you won!")
        score = guess * len(secret_word)
        print("Your total score for this game is:", score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    secret_word = "apple"
    hangman_with_hints(secret_word)
