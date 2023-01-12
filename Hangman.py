# hangman problem
from time import sleep
import random
import list_of_words_letters
import art

print(art.logo + "\n")
print("Welcome to the HANGMAN Game!!\nYou can save the man from dying by guessing the correct letters of the word")
chosen = random.choice(list_of_words_letters.words).lower()
letter = len(chosen)
# printing blank spaces
guess = []
for i in range(0, letter):  # Guess word
    guess.append("_")
# print("Secret:: The chosen word is "+chosen)
# Creating list of letters of CHOSEN WORD (list1)
list1 = []
for i in range(0, letter):
    list1.append(chosen[i])
count = 0


def setting(l, list1, guess, count):
    if count == 0:
        print(art.HANGMANPICS[0])
        print("Oh no so sorry to say.. The pillar has been set for the man to die")
        print("Use your chances and brain wisely to save the man")
    elif count == 1:
        print(art.HANGMANPICS[1])
        print("You did it again.. YamRaj is Unhappy Here comes the head to the rope")
    elif count == 2:
        print(art.HANGMANPICS[2])
        print("It's the third time.. See the man plead for his life with the neck")
        print("Pro tip : Try Vowels")
    elif count == 3:
        print(art.HANGMANPICS[3])
        print("Here comes the hand!! you have only 3 chances left to save him")
    elif count == 4:
        print(art.HANGMANPICS[4])
        print("The upper body is hanged you can still save him. Try Again")
    elif count == 5:
        print(art.HANGMANPICS[5])
        print("Its do or die now. If you are wrong, The man dies")
    else:
        print(art.HANGMANPICS[6])
        print("The man is dead, but you are a warrior try again to save another life!!")
        print("The word was : " + chosen)
        sleep(10)


def printing(guess):
    for i in range(0, len(guess)):
        print(guess[i] + " ", end=" ")
    print("\n")


printing(guess)


def check(guess_letter):
    flag = 0
    for i in range(0, len(guess_letter)):
        if '_' in guess_letter:
            flag = 1
            break
        else:
            continue
    if flag == 0:
        printing(guess_letter)
        print("Congrats.. You have saved the man!!")
        exit(1)


while count != 7:
    l = input("Guess a letter of the word : ").lower()
    if l in list1:
        for i in range(0, len(list1)):
            if l == list1[i]:
                guess[i] = l
        print("Well done you guessed it right..But more to go")
    else:
        setting(l, list1, guess, count)
        count += 1
    check(guess)
    if count != 7:
        print("The letters left are : ")
        printing(guess)
