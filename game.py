import random
import string
import os
from words import words

#get a valid word for the user to guess
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

#main function to the game
def main_game():
    user_name = input('\nEnter player name to play : ')
    word = get_valid_word(words) #fetches word from words.py
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #tracks the words used by the user
    chances = 10
    while len(word_letters) > 0 and chances > 0:
        print('\nchances left : ',chances)
        print('\nLetters used : ',' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('\nCurrent word : ',' '.join(word_list))
        user_letter = input('\nEnter your guess : ').upper()
        #game logic starts from the next line
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                chances = chances - 1 #removes one chance on wrong guess
                print('\n\nSorry wrong guess.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter')
        else:
            print('\nEnter a valid alphabet')
    if chances == 0: #when the user it out of chances
        print('\nSorry, you are out of chances. The word was ',word)
        print('\n')
    else:
        print('\nCongratulations ',user_name)
        print('\nThe word is ',word)
        print('\n')

#how to play and the main game help
def game_intro():
    print('\nHow to play\n\n')
    print('You will have 10 chances to guess the word correctly. You have to start by typing an alphabet and the game will show you whether the alphabet you entered is in the word or not. If it is in the word, the game will display it along with other blanks. But if your guessed alphabet is not in the word then you will lose a chance and the game progreses further with the same logic.\n\n')
    choiceyorn = input('\nReady (y/n) : ').upper()
    if choiceyorn == 'Y':
        main_game()
    elif choiceyorn == 'N':
        exit()
        
    else:
        print("Invalid Input")
        game_intro()

if __name__ == '__main__':
    game_intro()
