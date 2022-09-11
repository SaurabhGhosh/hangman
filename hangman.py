import os
import random


class Hangman:
    """ This class contains all the methods and attributes for the popular word guessing game - Hangman!!
    When the game is started, player will need to guess the letters of the hidden word.
    All letters need to be found before the Hangman image is complete."""
    game_header = '******** HANGMAN ********'
    # This will contain the challenge words retrieved from the file
    words = []
    # Contains the selected challenge word for the play
    challenge_word = ''
    # Contains the blanks for the letters in the challenge word.\
    # This gets updated with matching characters after a correct guess
    filled_word = []
    # The letters input by user during one play
    input_characters = []
    # Number of attempts made by player for one play.
    # When a new challenge word is selected, it resets
    attempt_count = 0
    # This is the length of the Hangman image or it can be thought as the maximum allowed attempts
    hangman_length = 8
    # Hangman image array
    hangman_array = \
        ['    --',
         '    | ',
         '    O ',
         '    | ',
         '   \\|/',
         '    | ',
         '    | ',
         '   / \\']
    # Array for the hanging pole
    hangman_stick = \
        ['--|  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '  |  ',
         '__|__']

    def __init__(self, filename='fruits.txt'):
        """Initiates the class and reads the file mentioned in argument.
        The mentioned file needs to be present in same folder."""
        try:
            # Open the file in read only mode and read the lines into a list
            with open(filename, 'r') as f:
                self.words = [x.strip() for x in f.readlines()]
        except IOError as e:
            # In case the file does not exist, initiate the list with default names
            print('An error occurred:', e)
            print('Initiating default list - Mango, Apple, Banana')
            self.words = ['Mango', 'Apple', 'Banana']

    def pick_next_word(self):
        """Picks the next challenge word"""
        self.challenge_word = random.choice(self.words)

    def initiate_blanks(self):
        """Prepares the blank placeholders for the challenge word.
        It resets the attempt count and the list of letters entered by player."""
        self.filled_word = []
        self.input_characters = []
        self.attempt_count = 0
        for x in self.challenge_word:
            # Assign a '_' in place of the letters in the challenge word
            self.filled_word.append('_' if x != ' ' else ' ')

        # Print initial layout
        print(self.game_header)
        print('\nInput characters -\nNo input yet')
        print('\nGuess the fruit -\n', *self.filled_word,'\n')
        self.draw_hangman()

    def update_hangman(self, input_character):
        """This method checks the letter input by player against the challenge word.
        It updates the placeholder blanks if there is a match.
        It shows the letters input by player so far.
        If maximum attempt is reached, this method exits the play."""
        # Increase attempt count
        self.attempt_count += 1
        # Field to check if all places filled
        all_blanks_filled = False
        print(self.game_header)
        # Add the input letter in the list
        self.input_characters.append(input_character)
        print('\nInput characters -\n', *self.input_characters)
        # Check if the letter entered by player is present in challenge word
        if input_character.upper() in self.challenge_word.upper():
            i = 0
            # Iterate through the letters in the challenge word
            for x in self.challenge_word:
                # If the letter matches with the input letter, update the blank with the input letter
                if x.upper() == input_character.upper():
                    self.filled_word[i] = x
                i += 1
            print('Guess the fruit -\n', *self.filled_word,'\n')
            # Check if all places are guessed already
            if '_' not in self.filled_word:
                all_blanks_filled = True
        else:
            print('Guess the fruit -\n', *self.filled_word)
        # Draw the hangman for this attempt
        if self.attempt_count <= self.hangman_length:
            self.draw_hangman()
            # Exit if maximum attempt reached even if guess is correct
            if self.attempt_count == self.hangman_length:
                print('You died, it was:', self.challenge_word)
                return '1'
        else:
            # Exit if maximum attempt reached
            print('You died, it was:', self.challenge_word)
            return '1'
        # Exit if all the letters are guessed correctly
        if all_blanks_filled:
            print('You live')
            return '1'
        else:
            # return the input letter always till current play is finished
            return input_character

    def draw_hangman(self):
        """Draw the hangman based on the attempt count"""
        i = 0
        for x in self.hangman_stick:
            # Print the Hangman anf the pole (x) for the number of attempts
            if i < self.attempt_count:
                print(self.hangman_array[i], x)
            # Print only the pole for the remaining rows
            else:
                print('      ', x)
            i += 1

    def play_hangman(self):
        """Starts the game"""
        os.system('cls')
        # Pick the next challenge word
        self.pick_next_word()
        # Initiate the blanks
        self.initiate_blanks()
        input_char = ''
        # Continue until player exits
        while input_char != '1':
            # Take player's input with prompt
            input_char = input('\nGuess a character\nPress 1 to exit\nPress 2 to change the challenge\n')
            # If exit letter ('1) is selected, just 'pass' because loop will exit in next iteration
            if input_char == '1':
                pass
            # Pick next challenge word when '2' is pressed
            elif input_char == '2':
                # Clear the screen to give a feeling of same place rendering
                os.system('cls')
                self.pick_next_word()
                self.initiate_blanks()
            # If valid letter is input, update the hangman
            elif input_char.isalpha() and len(input_char) == 1:
                os.system('cls')
                input_char = self.update_hangman(input_char)
            # For invalid input, prompt user
            else:
                print('Please only enter an alphabet')


# Check whether the game is executed from command
if __name__ == '__main__':
    help(Hangman)
    # Initiate object
    hangman = Hangman()
    # Call method to start play
    hangman.play_hangman()
