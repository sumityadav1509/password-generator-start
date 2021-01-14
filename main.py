# Step 1 
word_list=["ardvark","baboon","camel"]
# To Do -1 Randomly choose a word from the word_list and assign it to a variable caslled chosen word 
import random 
stages=[
  '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
chosen_word=random.choice(word_list) 
print(chosen_word)
# Create a Empty List
display=[] 
world_length=len(chosen_word)
lives=6
for _ in range(world_length):
  display+="_"
print(display)


# To Do 2 Ask the to guess a letter and assign their answer to a variable called guess.Make the guess lowercase.
end_of_game=False
while not end_of_game:
  guess=input("Guess a Letter: ").lower()


  # To Do 3 Check if the letter user guessed is one of the letters in the chosen word  
  for position in range(world_length):
    letter=chosen_word[position] 
    if letter==guess: 
      display[position]=letter 

  if guess not in chosen_word:
    lives-=1
    if lives==0:
      end_of_game=True 
      print("You Lose.")    

  # print(display)     
  if "-" not in display:
    end_of_game=True 
    print("You Win")


  print(stages[lives])    