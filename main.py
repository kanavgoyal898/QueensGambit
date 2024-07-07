import chess as ch
import ChessEngine as engine


def play_engine_move(board, color, max_depth):
    chessbot = engine.Engine(board, color, max_depth)
    move = chessbot.get_best_move()
    board.push(move)
    print('===============')
    print(board)
    print('===============')

def play_human_move(board):
    try:
        if len(list(board.legal_moves)) == 0:
            return
        else:
            print('legal moves:', board.legal_moves)
            move = input('enter your move: ')
            if move.upper() == 'UNDO':
                try:
                    board.pop()
                    board.pop()
                    play_human_move(board)
                except IndexError:
                    print("no more moves to undo...")
                    play_human_move(board)
            elif move.upper() == 'END':
                board.reset()
                print('the game is now terminated...')
                exit()
            else:
                board.push_san(move)
                print('===============')
                print(board)
                print('===============')
    except ValueError:
        print('invalid move! please try again...')
        play_human_move(board)

def start_game(board, color, max_depth):
    if color in ['b', 'black']:
        while not board.is_game_over():
            print('the engine is thinking...')
            play_engine_move(board, ch.WHITE, max_depth)
            play_human_move(board)
    else:
        while not board.is_game_over():
            play_human_move(board)
            print('the engine is thinking...')
            play_engine_move(board, ch.BLACK, max_depth)

    if board.outcome().winner == None:
        print('GAME OVER')
    elif board.outcome().winner == color:
        print('YOU WIN')
    else:
        print('YOU LOSE')

    board.reset()  

def get_user_input():
    board = ch.Board()

    color = None
    colors = ['b', 'black', 'w', 'white']
    while color not in colors:
        color = input('Choose your color (B/W): ').lower()
    color = color.lower()
    
    level = None
    max_depth = None
    levels = {
        'easy' : 3,
        'medium' : 5,
        'difficult' : 7,
        'auto' : 5
    }
    while level not in levels.keys():
        level = input('Choose difficulty level (auto/easy/medium/difficult): ').lower()
    max_depth = levels[level]

    start_game(board, color, max_depth)      


def main():
    get_user_input()

if __name__ == "__main__":
    main()
