# Simple command line tic-tac-toe game for two players
# Created the ticTacToe class to manage state

from random import randint
import re

class tikTacToeGame:
    def __init__(self, player_one_name: str = 'Player One', player_two_name: str = 'Player Two', x: int = 1):
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.x = x
        self.board = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
    
    # TODO make this not embarrassingly verbose
    def check_win(self):
        for i in range(3):
            if self.board[i][0] != 0 and self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != 0 and self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
            return self.board[0][2]
        return 0

    def check_tie(self):
        non_empty = 0
        for row in self.board:
            for cell in row:
                if cell != 0:
                    non_empty += 1

        return True if non_empty == 9 else False

    
# For when you are running a game via the command line
if __name__ == '__main__':
    # Get Player One's name
    while True:
        try: 
            player_one_name = input("What is Player One's Name?\t")
            break
        except ValueError:
            print("That's not a valid name. Try again")

    print(f"Hi {player_one_name}!")

    # Get Player Two's name
    while True:
        try: 
            player_two_name = input("And how about Player Two's Name?\t")
            break
        except ValueError:
            print("That's not a valid name. Try again")

    print(f"Hi {player_two_name}!")

    # Who starts?
    while True:
        starter = input("Randomly pick who starts? Enter [R]andom or [1] for Player One or [2] for Player Two\t").upper()
        if starter in '12R':
            if starter == '1':
                player_turn = 1
            elif starter == '2':
                player_turn = 2
            else:
                player_turn = randint(1,2)
            break
        else:
            print("Please enter R for Random starter, 1 for Player 1, or 2 for Player 2")

    still_playing = True
    player_one_wins = 0
    player_two_wins = 0
    ties = 0
    while still_playing:
        # Setup the game
        currGame = tikTacToeGame(player_one_name=player_one_name, player_two_name=player_two_name, x=player_turn)
        game_on = True
        turn = 1
        print(f"\n---- Starting tic-tac-toe between {player_one_name} and {player_two_name} ----\n")
        
        # Core game loop
        while game_on:
            # Input guess
            while True:
                move = input(f"{player_one_name if player_turn == 1 else player_two_name}'s turn. Where do you want to go?\t")
                move = re.findall('([012])', move)
                if len(move) == 2:
                    if currGame.board[int(move[0])][int(move[1])] != 0:
                        print(f"That spot is taken!")
                    else:
                        currGame.board[int(move[0])][int(move[1])] = player_turn
                        break
                else:
                    print(f"Your guess should be of the format 0|1|2, 0|1|2 where the first number is the column, second is the row")

            for row in currGame.board:
                disp = ''
                for c in row:
                    if c == currGame.x:
                        disp += 'X'
                    elif c == 0:
                        disp += '_'
                    else:
                        disp += 'O'
                print(disp)

            if currGame.check_win():
                if player_turn == 1:
                    player_one_wins  += 1
                else:
                    player_two_wins += 1
                print(f"\n!!!!{player_one_name if player_turn == 1 else player_two_name} wins!!!\n")
                print(f"Score is {player_one_name}: {player_one_wins}; {player_two_name}: {player_two_wins}, Ties: {ties}")
                game_on = False

            if currGame.check_tie():
                ties += 1
                print(f"\n!!!! Tie Game! No one wins!!!\n")
                print(f"Score is {player_one_name}: {player_one_wins}; {player_two_name}: {player_two_wins}, Ties: {ties}")
                game_on = False

            # TODO use the simple switch for this
            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1

        # Do you want to play again?
        while True:
            again = input(f"Do you want to play again? Y for Yes, N for No.\t").upper()
            if again == 'Y':
                still_playing = True
                break
            elif again == 'N':
                still_playing = False
                break
            else: 
                print(f"Invalid input. Y if yes, N if no")