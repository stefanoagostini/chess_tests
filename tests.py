import chess
import chess.engine
import chess.svg


"""board = chess.Board()
print(board)

possible_moves = board.legal_moves
print(possible_moves)"""

engine = chess.engine.SimpleEngine.popen_uci("stockfish-10-win/stockfish-10-win/Windows/stockfish_10_x64.exe")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)

engine.quit()
print(board)
print(board.is_checkmate())
chess.svg.board(board=board)
