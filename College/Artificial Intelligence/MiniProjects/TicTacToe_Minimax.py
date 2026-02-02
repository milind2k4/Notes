import math
import copy

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 3x3 board
        self.human = 'X'
        self.ai = 'O'

    def print_board(self):
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def minimax(position, depth, maximizing_player, game):
    # Base cases
    if game.winner(0, game.ai): # AI won (previous move) - hacky check, better to pass last move
        return {'position': None, 'score': 1 * (game.num_empty_squares() + 1)}
    elif game.winner(0, game.human): # Human won
        return {'position': None, 'score': -1 * (game.num_empty_squares() + 1)}
    elif not game.empty_squares(): # Tie
        return {'position': None, 'score': 0}
    
    if maximizing_player:
        best = {'position': None, 'score': -math.inf}
        for possible_move in game.available_moves():
            # Try move
            game.make_move(possible_move, game.ai)
            # Recurse
            sim_score = minimax(position, depth + 1, False, game)
            # Undo move
            game.board[possible_move] = ' '
            
            sim_score['position'] = possible_move
            if sim_score['score'] > best['score']:
                best = sim_score
        return best
    else:
        best = {'position': None, 'score': math.inf}
        for possible_move in game.available_moves():
            # Try move
            game.make_move(possible_move, game.human)
            # Recurse
            sim_score = minimax(position, depth + 1, True, game)
            # Undo move
            game.board[possible_move] = ' '
            
            sim_score['position'] = possible_move
            if sim_score['score'] < best['score']:
                best = sim_score
        return best

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = 'X' # Starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player(game)
        else:
            square = x_player(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')

            if game.winner(square, letter):
                if print_game:
                    print(f'{letter} wins!')
                return letter
            
            letter = 'O' if letter == 'X' else 'X'
    
    if print_game:
        print('It\'s a tie!')

def human_player(game):
    valid_square = False
    val = None
    while not valid_square:
        square = input(f'Human turn. Input move (0-8): ')
        try:
            val = int(square)
            if val not in game.available_moves():
                raise ValueError
            valid_square = True
        except ValueError:
            print('Invalid square. Try again.')
    return val

def ai_player(game):
    if len(game.available_moves()) == 9:
        return 4 # Center is best first move
    
    # Minimax!
    # Note: We need to pass a copy or modify logic to check winner properly inside minimax
    # For simplicity in this snippet, we assume the helper functions work on the current state
    # But `winner` takes `square` which is the LAST move. 
    # Let's fix the winner check in minimax to be robust.
    
    # Actually, the minimax above has a bug: it checks winner(0, ...) which is wrong.
    # It needs to check if the *current state* is a win.
    # Let's rewrite the Minimax loop slightly to be cleaner for this file.
    
    best_score = -math.inf
    best_move = None
    
    for move in game.available_moves():
        game.make_move(move, game.ai)
        score = minimax_score(game, 0, False)
        game.board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def check_winner(board, letter):
    # Helper for minimax recursion
    # Rows
    for i in range(0, 9, 3):
        if all([board[i+j] == letter for j in range(3)]): return True
    # Cols
    for i in range(3):
        if all([board[i+j*3] == letter for j in range(3)]): return True
    # Diagonals
    if board[0] == letter and board[4] == letter and board[8] == letter: return True
    if board[2] == letter and board[4] == letter and board[6] == letter: return True
    return False

def minimax_score(game, depth, is_maximizing):
    if check_winner(game.board, game.ai):
        return 10 - depth
    if check_winner(game.board, game.human):
        return -10 + depth
    if not ' ' in game.board:
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for move in [i for i, x in enumerate(game.board) if x == ' ']:
            game.board[move] = game.ai
            score = minimax_score(game, depth + 1, False)
            game.board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in [i for i, x in enumerate(game.board) if x == ' ']:
            game.board[move] = game.human
            score = minimax_score(game, depth + 1, True)
            game.board[move] = ' '
            best_score = min(score, best_score)
        return best_score

if __name__ == '__main__':
    t = TicTacToe()
    play(t, human_player, ai_player, print_game=True)
