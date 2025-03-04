# We need to import the random module to gain access to "random", the random
# number generating object provided by Python.
import random

# Where supported, clear the console between guesses.
import clear_console

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
def print_word(word, letters):
    # Try to clear the console for a more video game like experience
    # (May not work in every Python environment)
    clear_console.clear_console()

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
        # after checking all the guessed letters, did we match?
        if letter_guessed:
            # yes, so increment our match counter for later reporting
            matches += 1 
            # save the guessed letter for later display
            line_to_display += secret_letter + " " 
        else:
            # save an underscore "_" placeholder for later display
            line_to_display += "_ " 
    # display the word to the user.
    print(line_to_display)

    # return the number of letters in the secret word that have been correctly guessed
    return matches

# Defining main function
def play_hangman():
    # Our word list. You can extended it with as many words
    # as you like. The random number generator will respect
    # the length of the list using the len() function.
    word_list = ['kitty', 'rock', 'four', 'star', 'spock']

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
    
    # print the current correct guesses, with underscores for unknowns
    print_word(secret_word, guessed_letters) 

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

    # game play loop. 
    while bad_guesses < max_bad_guesses:
        guessed_letters += input() # Add a letter from the console to the list of guesses
        match_count = print_word(secret_word, guessed_letters) # print the correct guesses, save the number of matching letters
        if match_count == len(secret_word): # Are all the letters correctly guessed?
            matched_all = True # Save the fact that we won
            break # Exit the while loop early, no need to keep going.
        bad_guesses += 1 # guess was incorrect. Increment the bad guess counter
        
    # finished with play. Did we win?
    if matched_all:
        print('You won')
    else:
        print('You lost')
    
    
# Check the special Python-provided variable __name__
# to see if this module was called directly 
# (not imported from another module). 
# If it is we call the play_hangman() function to play the game.
if __name__=="__main__":
    play_hangman()
