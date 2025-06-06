#from ai import call_gpt
from openai import OpenAI

'''
Wordle.py
--------------
Wordle is a word guessing game where players will need to input the correct word within a set number of tries

Important notes:
- AI will generate the 5-letter word for the player to guess
- Maximum number of attempts is 6
- The guessed word will be verified by the length of the characters provided and if it's a real world using AI
- For each attempt, the program will give out clues if the letters in the player's guess is in the word
- Number of correct letters is not given. Only their position if guessed correctly.
'''



def main():
    # Print a message to inform user the name of the game and its mechanics
    print("Wordle: Guess the 5-letter word in 6 tries.")
    print("")
    print("Correct letters in correct positions are written in uppercase.")
    print("Correct letters in incorrect positions will be writted as '#'.")
    print("Incorrect letters are written as _.")
    print("")
    print("_ _ _ _ _")
    print("")

    # Define the word to guess
    word = define_a_word()

    # Initialize a sequence to contain the guesses
    guesses = []

    # Ask user for a guess
    guess = input(f"Guess {len(guesses) + 1}: ")
    guess = guess.lower()

    # Validate if the word is a real word
    guess = validate_word(guess, guesses)

    # Adds the guess to the sequence
    guesses.append(guess)

    # Gets the index of the guesses sequence
    index = len(guesses) - 1

    # Checks if the guess is equal to the random generated word
    # If the word is guessed correctly, the program will proceed with the statement below
    if guesses[index] == word:
        print(f"Great job! The word was {word.upper()}.")
        print("You got it in the first try.")
    
    # If the guess is incorrect, it will proceed to the else statement below
    else:
        # This will run the function, check_letters, which will verify if the letters in the guess are present in the word
        check_letters(word, guess)

        # Loops asking for an input until the word is guessed or reached the max attempts
        # 5 is set as the max attempt since we already asked 1 input earlier
        while guess != word and len(guesses) <= 5:
            guess = input(f"Guess {len(guesses) + 1}: ")
            guess = guess.lower()

            # Validate the word is this is a 5-letter real word
            guess = validate_word(guess, guesses)

            # Adds the guess to the sequence
            index = len(guesses)

            if len(guess) == 5 and guess != None:
                guesses.append(guess)

            if guesses[ index ] == word:
                print("")
                print(f"Great job! The word was {word.upper()}.")
                print(f"You got it in {len(guesses)} tries.")
            else:
                check_letters(word, guess)
                if len(guesses) == 6:
                    print("")
                    print(f"Nice try. The correct word was {word.upper()}.")

# This function will check all the letters in the guessed word if it is the same with the random word
def check_letters(word, guess):
    # Initializing the variables needed for the verification
    first_letter_inside_word = ""
    second_letter_inside_word = ""
    third_letter_inside_word = ""
    fourth_letter_inside_word = ""
    fifth_letter_inside_word = ""

    # Defining the sequence for the word and guess
    letters_in_word = []
    letters_in_guess = []

    for char in word:
        letters_in_word.append(char) 
    
    for char in guess:
        letters_in_guess.append(char) 

    # This for loop will check if the letter is in the word
    for char in word:
        if char == letters_in_guess[0]:
            first_letter_inside_word = "#"
        if char == letters_in_guess[1]:
            second_letter_inside_word = "#"
        if char == letters_in_guess[2]:
            third_letter_inside_word = "#"
        if char == letters_in_guess[3]:
            fourth_letter_inside_word = "#"
        if char == letters_in_guess[4]:
            fifth_letter_inside_word = "#"

    # Validations for the first letter
    if guess[0] == word[0]:
        first_letter = guess[0].upper()
    elif first_letter_inside_word != "":
        first_letter = first_letter_inside_word
    else:
        first_letter = "_"

    # Validations for the second letter
    if guess[1] == word[1]:
        second_letter = guess[1].upper()
    elif second_letter_inside_word != "":
        second_letter = second_letter_inside_word
    else:
        second_letter = "_"

    # Validations for the third letter
    if guess[2] == word[2]:
        third_letter = guess[2].upper()
    elif third_letter_inside_word != "":
        third_letter = third_letter_inside_word
    else:
        third_letter = "_"

    # Validations for the fourth letter
    if guess[3] == word[3]:
        fourth_letter = guess[3].upper()
    elif fourth_letter_inside_word != "":
        fourth_letter = fourth_letter_inside_word
    else:
        fourth_letter = "_"

    # Validations for the fifth letter
    if guess[4] == word[4]:
        fifth_letter = guess[4].upper()
    elif fifth_letter_inside_word != "":
        fifth_letter = fifth_letter_inside_word
    else:
        fifth_letter = "_"

    return print(f"{first_letter} {second_letter} {third_letter} {fourth_letter} {fifth_letter}\n")


# This function will generate the word for the game
def define_a_word():
    # Ask AI to generate a random 5-letter word for the game
    response = call_gpt('Can you give me a random 5-letter word?')

    # Split the words and save it as an sequence
    words = response.split()

    # Getting the word to guess from the AI's response
    # The random word given should be the last value in the sequence
    index = len(words) - 1
    word = words[index]
    
    cleaned_word = ''.join(char for char in word if char.isalpha())
    return cleaned_word

# This function will call the AI to get a response
def call_gpt(prompt):
    # Setting up the OpenAI API key
    client = OpenAI(
        api_key= "<API-KEY>"  # Replace with your OpenAI API key
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            max_tokens=200,
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# This function will check if the word inputted is a valid word
def validate_word(guess, guesses):
    # Validate if the guess is a 5-letter word     
    while len(guess) != 5:
        print("Invalid input\n")
        guess = input(f"Guess {len(guesses) + 1}: ")
        guess = guess.lower()

    # Ask AI to validate the word
    #is_correct_length = call_gpt('Answer just yes or no. Does the word "' + guess + '" have 5 letters?')

    is_real_word = call_gpt('Answer just yes or no. Is the word "' + guess + '" a real word?')
    #cleaned_word = ''.join(char for char in is_real_word if char.isalpha())

    if is_real_word == 'No.':
        print(f"{is_real_word} {guess.upper()} is not a real word.\n")
        guess = input(f"Guess {len(guesses) + 1}: ")
        guess = guess.lower()
        validate_word(guess, guesses)
        return guess

    return guess
    
if __name__ == "__main__":
    main()