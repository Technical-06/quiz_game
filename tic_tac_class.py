#TIC TAC TOE GAME
class tic_tac_toe:
    def tictacBoard(xState, yState):
        zero = 'X' if xState[0] else ('O' if yState[0] else 0)
        one = 'X' if xState[1] else ('O' if yState[1] else 1)
        two = 'X' if xState[2] else ('O' if yState[2] else 2)
        three = 'X' if xState[3] else ('O' if yState[3] else 3)
        four = 'X' if xState[4] else ('O' if yState[4] else 4)
        five = 'X' if xState[5] else ('O' if yState[5] else 5)
        six = 'X' if xState[6] else ('O' if yState[6] else 6)
        seven = 'X' if xState[7] else ('O' if yState[7] else 7)
        eight = 'X' if xState[8] else ('O' if yState[8] else 8)
        print(f"{zero} | {one} | {two} ")
        print(f"--|---|---")
        print(f"{three} | {four} | {five} ")
        print(f"--|---|---")
        print(f"{six} | {seven} | {eight} ")

    def checkWinner(xState, yState):
        #cases for winning the game
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            #if this satisfies the condition that the sum of xState===3 then it will won otherwise yState will win
            if(xState[win[0]]+ xState[win[1]]+ xState[win[2]] == 3):
                print("X Won the match")
                return 1
            if(yState[win[0]]+ yState[win[1]]+ yState[win[2]] == 3):
                print("O Won the match")
                return 0
        return -1
       
    if __name__ == "__main__":
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0] #xState array
        yState = [0, 0, 0, 0, 0, 0, 0, 0, 0] #yState array
        turn = 1 # 1 for X and 0 for O
        print("Let's Play Tic Tac Toe Game")
        while(True):
            tictacBoard(xState, yState)
            if(turn == 1):
                print("X's Chance")
                value = int(input("Please enter a value: "))
                xState[value] = 1
            else:
                print("O's Chance")
                value = int(input("Please enter a value: "))
                yState[value] = 1
            cwin = checkWinner(xState, yState)
            if(cwin != -1):
                print("Match over")
                break
           
            turn = 1 - turn
a=tic_tac_toe()

