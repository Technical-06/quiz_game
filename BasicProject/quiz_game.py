#quiz game with few questions:-
from tkinter.messagebox import YES
print("welcome to my computer quiz")
#userInput
playing = input("Do you want to play?")
#if-else condition whether answer is correct or not
if playing != "yes":
    quit()
print ("Okay! Let's play! :)")
score = 0
answer = input("Is cat runs faster than a tiger?")
if answer == "no":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is the extension for python?")
if answer == ".py":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("Who invented python language?")
if answer == "guido van rossum":
    print('Correct!')
    score += 1

else:
    print('Incorrect')

answer = input("What's the full form of OS?")
if answer == "operating system":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
answer = input("Which one is object oriented language:c or c++?")
if answer == "c++":
    print('Correct!')
    score += 1
else:
    print('Incorrect')
#calculating correct questions
print("You got " + str(score) + "questions correct!")
#calculating percentage
print("You got " + str((score/5) *100) + "%")
if ((score/5) *100)<60:
    print('Fail')
else:
    print('Pass')

