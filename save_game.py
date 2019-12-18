import chess
import chess.engine
import chess.pgn

game = chess.pgn.Game()
game.headers["Event"] = "Example"

engine = chess.engine.SimpleEngine.popen_uci("stockfish-10-win/stockfish-10-win/Windows/stockfish_10_x64.exe")

board = chess.Board()
init = True

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    move = str(result.move)
    if init:
        node = game.add_variation(chess.Move.from_uci(move))
        init = False
    else:
        node = node.add_variation(chess.Move.from_uci(move))
        info = engine.analyse(board, chess.engine.Limit(depth=20))
        score = int(str(info["score"]))/100.
        print(score)
        node.comment = str(score)


engine.quit()

print(board.result())
print(board)
print(game)
new_pgn = open("games/game.pgn", "w", encoding="utf-8")
exporter = chess.pgn.FileExporter(new_pgn)
game.accept(exporter)
