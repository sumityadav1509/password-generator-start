# Step 1 
word_list=["ardvark","baboon","camel"]
# To Do -1 Randomly choose a word from the word_list and assign it to a variable caslled chosen word 
import random 
chosen_word=random.choice(word_list)

# To Do 2 Ask the to guess a letter and assign their answer to a variable called guess.Make the guess lowercase.
guess=input("Guess a Letter: ").lower()


# To Do 3 Check if the letter user guessed is one of the letters in the chosen word  
for letter in chosen_word:
  if letter==guess:
    print("Right")
  else: 
      print("Wrong")