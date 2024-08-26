import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.random_player = 'O'
        
        
    def print_board(self):
        row1 = f'| {self.board[0]} | {self.board[1]} | {self.board[2]} |'
        row2 = f'| {self.board[3]} | {self.board[4]} | {self.board[5]} |'
        row3 = f'| {self.board[6]} | {self.board[7]} | {self.board[8]} |'
        
        
        print()
        print(row1)
        print(row2)
        print(row3)
        print()
        
    def check_win(self):
        win_conditions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != '':
                return True
            
            return False
        
    # def check_draw(self):
    #     return ' ' not in self.board()
    
    def play_game(self):
        while True:
            self.print_board()
            player_move = input(f"Player {self.current_player}, enter your move (1 - 9): ")
            random_move = random.randint(1,9)
            
            while player_move == random_move:
                random_move = random.randint[0,10]
            
            
            if self.board[int(player_move) - 1] == ' ' and self.board[random_move] == ' ':
                self.board[int(player_move) - 1] = self.current_player
                self.board[random_move] = self.random_player
                
                if self.check_win(): 
                        self.print_board()
                        print(f"Player {self.current_player} wins! Congratulations!")
                        break
                    
                # elif self.check_draw():
                #         self.print_board()
                #         print("It's a draw!")
                #         break
            
                # self.current_player = 'O' if self.current_player == 'X' else 'X'
                
            else:
                print("Invalid move, try again.")
            
            
            
        
game = TicTacToe()

print(game.play_game())