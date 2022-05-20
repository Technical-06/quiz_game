import random
class game:
    def setdata(self):
     self.player_win=0
     self.computer_win=0
#list of choices
     self.options=["rock","paper","scissor"]
    def play(self):
        while True:
            user_input = input("type rock paper scissor or Q to quit: ").lower()
            if user_input == "q":
                break
            if user_input not in self.options:
                continue
            random_number = random.randint(0,2)
            #rock=0,paper=1,scissor=2
            computer_pick = self.options[random_number]
            print("Computer picked",computer_pick +".")

            if user_input == "rock" and computer_pick == "scissor":
                print("You won!")
                print("rock can smash scissor")
                self.player_win += 1
            elif user_input=="paper" and computer_pick == "rock":
                print("You won!")
                print("paper can wrap rock")
                self.player_win += 1
            elif user_input=="scissor" and computer_pick == "paper":
                print("You won!")
                print("scissor can cut the paper")
                self.player_win += 1
            elif user_input==computer_pick:
                print("oops! Draw")
            else:
                print("You lost!")
                self.computer_win +=1

            print("you won",self.player_win,"times.")
            print("The computer won",self.computer_win,"times.")
            
a=game()
a.setdata()
a.play()
