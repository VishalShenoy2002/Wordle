from wordle import Wordle
import random

with open('words.txt','r') as f:
    words=[x.strip() for x in f.readlines()]
    f.close()

word_for_game=random.choice(words)
print(len(word_for_game))
app=Wordle(word_for_game)

while app.can_attempt:
    word=input("\nGuess the Word :")
    app.attempt(word)

if app.SOLVED_BEFORE_ALL_ATTEPMTS==False:
    print("The word is {}".format(word_for_game.upper()))
