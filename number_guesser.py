#NUMBER GUESSER GAME
lower_bound=22
upper_bound=78

attempts = 0
#loop until we get the actual number
while True:
    attempts += 1
    guess = int(input("Hey guess the number you have in yur mind:\n"))
    if guess<lower_bound:
        print("Your guess was too low buddy dont worry keep trying!")
    elif guess>upper_bound:
        print("Your guess was too high buddy dont worry keep trying!")
    else:
        print(f"You guessed the number in {attempts} attempts")
        break
print("Congratulations you guessed right,Thanks for playing!")
