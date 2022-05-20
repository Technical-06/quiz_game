#NUMBER GUESSER GAME
class guess:
    def setdata(self):
        self.lower_bound=22
        self.upper_bound=78
    
    def play(self):
        attempts = 0
        #loop until we get the actual number
        while True:
            attempts += 1
            guess = int(input("Hey guess the number you have in your mind:\n"))
            if guess<self.lower_bound:
                print("Your guess was too low buddy dont worry keep trying!")
            elif guess>self.upper_bound:
                print("Your guess was too high buddy dont worry keep trying!")
            else:
                print(f"You guessed the number in {attempts} attempts")
                break
        print("Congratulations you guessed right,Thanks for playing!")
a=guess()
a.setdata()
a.play()