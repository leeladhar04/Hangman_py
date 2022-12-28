import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word=random.choice(word_list)
display=[]
s=set()
print(logo)

print("In this game you would be given a word , you have to guess the letters one by one , for each wrong guess one of the limbs of the hanging person will be cut . Guess all the letters before all limbs disappear!!!")
print("")

for i in range(len(chosen_word)):
  display+="_"
print(f"{' '.join(display)}")

cor=0
print(stages[0])
wrong=0
while ((cor!=len(set(chosen_word))) and (wrong!=6)):
  ok=True
  guess=str(input("Guess the character ")).lower()
  clear()
  print("")

  for i in range(len(chosen_word)):
    if guess==chosen_word[i]:
      ok=False
      if (guess not in s):
        s.add(guess)
        cor+=1
      display[i]=chosen_word[i]
  
  if ok==True:
    wrong+=1
    print(logo)
    print("Wrong guess!!")
    print(stages[wrong])
    
  else :
    print(logo)
    print("Correct Guess!!")
    print(stages[wrong])
  print(f"{' '.join(display)}")

if wrong==6:
  print("You Lose")
  print("The word was",str(chosen_word))
else:
  print("You win ")




