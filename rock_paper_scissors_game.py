import random
player_win=0
computer_win=0
#list of choices
options=["rock","paper","scissor"]
while True:
    user_input = input("type rock paper scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    #rock=0,paper=1,scissor=2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick +".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        print("rock can smash scissor")
        player_win += 1
    elif user_input=="paper" and computer_pick == "rock":
        print("You won!")
        print("paper can wrap rock")
        player_win += 1
    elif user_input=="scissor" and computer_pick == "paper":
        print("You won!")
        print("scissor can cut the paper")
        player_win += 1
    elif user_input==computer_pick:
         print("oops! Draw")
    else:
        print("You lost!")
        computer_win +=1

    print("you won",player_win,"times.")
    print("The computer won",computer_win,"times.")
    
    



