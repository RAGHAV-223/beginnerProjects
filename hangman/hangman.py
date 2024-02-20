# Hangman using termcolor and inquirer
from os import system
from termcolor import colored
import random
import string
import inquirer
from words import words
from visuals_list import lives_visual_dict


GAME_LEVEL = [
  inquirer.List('level',
                message="Please select game level",
                choices=['Easiest', 'Easy', 'Normal', 'Hard', 'Very hard'],
                default='Normal'
            ),
]

GAME_LEVEL_MAPPING = {
  "Easiest" : 20,
  "Easy" : 10,
  "Normal" : 6,
  "Hard" : 3,
  "Very hard" : 2,
}

def valid(words):
  w = random.choice(words)
  while '-' in words or ' ' in words:
    w= random.choice(words)

  return w.upper()


def hangman(game_level):

  w = valid(words)
  word_letter =  set(w)
  alphabet = set(string.ascii_uppercase)
  used_letter = set() # letters entered by user [empty for now]

  lives = game_level
  while len(word_letter)>0 and lives>0:
    system('cls')
    print("\nLives : ","💟 "*lives)
    if lives<8:
      print(lives_visual_dict[lives])
    print('Words used : '," " .join(used_letter))
    #list for printing words
    wordcondition=[letter if letter in used_letter else "_" for letter in w]
    print("Word Condition : ", " ".join(wordcondition))

    user_letter = input('\nGuess a letter: ').upper()

    if user_letter in alphabet - used_letter:
      used_letter.add(user_letter)
      
      if user_letter in  word_letter:
        word_letter.remove(user_letter)
      else:
        lives=lives - 1
    elif user_letter in used_letter:
      print(colored("Character already used!", "red"))
      lives = lives - 1
    
    else:
      print(colored("Invalid character!", "red"))

  if lives==0:
    print(lives_visual_dict[lives])
    msg = colored("Lives end, You lose!", "red")
    word_answer = colored(w, "magenta")
    print(f"{msg} \n Word is: {word_answer}")
  else:
    msg = colored("Word guessed correctly", "green")
    word_answer = colored(w, "magenta")
    print(f"{msg}: {word_answer}")


if __name__ == "__main__":
  print("**** Welcome to Hangman Game ****\n")
  answers = inquirer.prompt(GAME_LEVEL)
  game_level = GAME_LEVEL_MAPPING.get(answers["level"])
  hangman(game_level)