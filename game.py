# guess the number basic gameated by aryan in college because he was bored
# play until u win

import random

list = [1,2,3,4,5,6,7,8,9,10]

def guess():
    randomNo = random.choice(list)
    playerGuess = ''
   
    while randomNo != playerGuess:
        playerGuess = int(input("Guess no. between 1-10 . both 1 and 10 included\n"))
        if randomNo == playerGuess:
            print("you won! congretulations")
        else:
            print("wrong! try again")
            continue
        
guess()