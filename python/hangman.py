# We need to import the random module to gain access to "random", the random
# number generating object provided by Python.
import random

gallows_strings = [ [
    "      ",
    "      ",
    "      ",
    "      ",
    "      ",
    "      ",
    "      "], [
    "      ",
    "      ",
    "      ",
    "      ",
    "      ",
    "      ",
    "______"], [
    "      ",
    " |    ",
    " |    ",
    " |    ",
    " |    ",
    " |    ",
    "______"], [
    " ---  ",
    " |    ",
    " |    ",
    " |    ",
    " |    ",
    " |    ",
    "______"], [
    " ---  ",
    " | |  ",
    " |    ",
    " |    ",
    " |    ",
    " |    ",
    "______"], [
    " ---  ",
    " | |  ",
    " | O  ",
    " |/ \\ ",
    " | |  ",
    " |/ \\ ",
    "______"]
]
            

def print_gallows(guess_number):
    gallows_string = '\n'.join(gallows_strings[guess_number])
    print(gallows_string)

# Count the number of letters in the secret word that have been 
# correctly guessed.
# Parameters:
# word is the word we're trying to guess, 
# letters is a string with all the guessed letters.
#
# Return Value: 
# The function returns an integer, the number of letter (positions) 
# in the secret word that have been correctly guessed so far.
# For example, if the word is "sass" and the only letter that has been
# guessed so far is "s", then the return value is 3.
def count_matches(word, letters):

    # At the end, we are going to report (return) the number of 
    # letters of the secret word that are among the correct guesses
    # so far.
    matches = 0 


    # For each letter of the secret word
    for secret_letter in word: 
        # We don't know if the guess is correct, yet.
        letter_guessed = False 
        # for each of the letters guessed
        for guess_letter in letters: 
            # if the guessed letter matches the current secret word letter
            if secret_letter == guess_letter: 
                # Record the fact that the guess was correct.
                letter_guessed = True 
                # No need to check the rest of the guest letters 
                # because we already matched. 
                # We can break out of the 'for guess_letter' loop.
                break 
        # We just finished checking all the guessed letters, did we match?
        if letter_guessed:
            # yes, so increment our match counter for later reporting
            matches += 1 
    # Return the number of letters in the secret word 
    # that have been correctly guessed so far. For example,
    # if the secret word is "kick" and only "k" has been guessed,
    # we return 2, because there are two "k"s in "kick". If both
    # "c" and "k" have been guessed, we return 3.
    # The calling routine can check this number to see if it is the
    # same as the length of the secret word, which means that the 
    # game is won.
    return matches

# Print the current state of the game: the secret word, with underscores
# as placeholders for unguessed letters.
#
# Parameters:
# word is the word we're trying to guess, 
# letters is a string with all the guessed letters.
#
# Return Value: 
# The function returns an integer, the number of letter (positions) 
# in the secret word that have been correctly guessed so far.
# For example, if the word is "sass" and the only letter that has been
# guessed so far is "s", then the return value is 3.
#
# Side Effects:
# This function prints a line to the console, consisting of the secret word
# with spaces between letters. Correctly guessed letters are shown.
# Still-secret letters are represented with an underscore. ("_")
#
def print_word(word, letters):

    # At the end, we are going to report (return) the number of 
    # letters of the secret word that are among the correct guesses
    # so far.
    matches = 0 
    
    # Instead of displaying each letter to the console one at a time
    # let's save them all in one string, then we can print the whole
    # all at once at the end. We initialize it to an empty string.
    line_to_display = ""

    # For each letter of the secret word
    for secret_letter in word: 
        # We don't know if the guess is correct, yet.
        letter_guessed = False 
        # for each of the letters guessed
        for guess_letter in letters: 
            # if the guessed letter matches the current secret word letter
            if secret_letter == guess_letter: 
                # Record the fact that the guess was correct.
                letter_guessed = True 
                # No need to check the rest of the guest letters 
                # because we already matched. 
                # We can break out of the 'for guess_letter' loop.
                break 
        # We just finished checking all the guessed letters, did we match?
        if letter_guessed:
            # save the guessed letter for later display
            line_to_display += secret_letter + " " 
        else:
            # save an underscore "_" placeholder for later display
            line_to_display += "_ " 
    print(line_to_display)

# Defining main function
def play_hangman():
    # Our word list. You can extended it with as many words
    # as you like. The random number generator will respect
    # the length of the list using the len() function.
    word_list = ['kitty', 
                 'rock', 
                 'four', 
                 'star', 
                 'spock']

    # Pick the secret word from the word list.
    # We use the len() function to set the high limit of the
    # random number, remembering to subtract 1 from the length,
    # because list indexes are zero-based.
    secret_word = word_list[random.randint(0, len(word_list) - 1)]
    
    # This string holds the set of letters guessed so far.
    # Initialized to an empty string.
    # If we did not declare this variable here, before the loop,
    # an error would be generated on the line that adds the user input
    # to the string, using the += operator.
    guessed_letters = ""
    
    # Keep track of whether the player has correctly guessed all letters
    # We declare it here in case the while loop never runs
    # (in case something goes wrong and max_bad_guesses is 0)
    # because that would cause an "object not found" error when
    # we check its value after the loop exits.
    matched_all = False
    
    # Maximum number of allowed bad guesses.
    max_bad_guesses = 5
    
    # keep track of the number of wrong guesses.
    bad_guesses = 0 


    # print the current correct guesses, with underscores for unknowns
    # Since nothing has been guessed yet, we will see only 
    # underscore placeholders.
    #print_word(secret_word, guessed_letters, bad_guesses) 

    # print_word() reports number of matched letters.
    # we keep track of this in a variable called match_count.
    match_count = 0

    # game play loop. 
    while bad_guesses < max_bad_guesses:
        print_gallows(bad_guesses)
        print_word(secret_word, guessed_letters)
        print('Enter your guess: ', end="")
        
        # Add a letter from the console to the list of guesses
        guessed_letters += input() 
        # We are about to update the value of match_count,
        # and we need to see if it is different from blast time,
        # so we save the current value of match_count in old_match_count.
        old_match_count = match_count
        # print the correct guesses, save the number of matching letters
        match_count = count_matches(secret_word, guessed_letters)
        

        # Are all the letters correctly guessed?
        if match_count == len(secret_word):
            # Save the fact that we won 
            matched_all = True
            # Exit the 'while' loop early, no need to keep going. 
            break 

        # If the player guessed correctly, match_count will be different.
        if match_count == old_match_count:
            # Guess was incorrect. Increment the bad guess counter
            bad_guesses += 1 
        
        
    # finished with play. Did we win?
    if matched_all:
        print_word(secret_word, guessed_letters)
        print('You won')
    else:
        print_gallows(bad_guesses)
        print('You lost')
    
    
# Check the special Python-provided variable __name__
# to see if this module was called directly 
# (not imported from another module). 
# If it is we call the play_hangman() function to play the game.
if __name__=="__main__":
    play_hangman()
