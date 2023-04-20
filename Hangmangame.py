import tkinter as tk
window = tk.Tk()
import random

# creating list of words
words = ["solomon", "jude", "matthew", "samson", "tomisan", "imole", "christiana", "temilade", "david", "moses", "amin", "damilanre"]
# creating a code for hangman graphics
hangman_graphics = ['_',
                    '__',
                    '__\n |',
                    '__\n |\n O',
                    '__\n |\n O\n |',
                    '__\n |\n O\n/|',
                    '__\n |\n O\n/|\ ',
                    '__\n |\n O\n/|\ \n/',
                    '__\n |\n O\n/|\ \n/ \ ',
]
# creating a rule for playing the hangman game
number_of_mistakes = 0
letters_guessed = []
number_of_mistake_allowed = len(hangman_graphics)
word = random.choice(words)
letter_words = (word)
wrong_letters = []

print()
print("the word has {} letter", format(len(letter_words)))

# creating a loop to play hangman game
while number_of_mistakes < number_of_mistake_allowed:
    print()
    print('wrong_letters: ', end='')
    print()
    print("Guesses left: {} ",  format(number_of_mistake_allowed - number_of_mistakes))
    letters_user = input("enter_a_letter -->")

    while letters_user in letters_guessed or letters_user in wrong_letters:
        print()
        print("you have already enter this letter, enter another one")
        letters_user = input("Enter a letter --> ")

    if letters_user not in letter_words:
        number_of_mistakes += 1
        wrong_letters.append('letter user')
        print()
        print("word: " , end="")

        for letter in letter_words:
            if letters_user == letter:
                letters_guessed.append(letters_user)
    
        for letter in letter_words:
            if letter in letters_guessed:
                print(letter + " ", end="")
        
        else:
            print("_ ", end="")
        
        print()
        if number_of_mistakes:
            print(hangman_graphics [number_of_mistakes - 1])
        print()
        print("------------------------")
    if len(letters_guessed) == len(letter_words):
        print()
        print("you win!!!")
        break

    if number_of_mistake_allowed == number_of_mistake_allowed:
        print()
        print("you lost\nyou let a goodman die!!!")

            