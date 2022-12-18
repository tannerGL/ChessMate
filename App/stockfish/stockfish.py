# Stockfish Chess Engine  API for 
# Move Analysis, Human v. Human, Bot v. Bot & Bot v. Human
# @Author: Tanner Lindsay

# Description:

# update_board(self, uci_string): Takes a move in standard algebraic notation
# and updates the board object

# analyze_position(self): Analyzes position for Dark and Light pieces then 
# returns the "score" for each side. 
# Score is the chance of winning.

import asyncio
import re
import chess
import chess.engine



# Class for stockfish engine initialization and command handling
class Stockfish:
    def __init__(self, game_type):
        self.engine = chess.engine('/usr/bin/stockfish')
        self.board = chess.board()


    def get_bot_move(self):
        if self.board.is_game_over(): return (0, self.board.fen())
        bot_move = self.engine.play(board, chess.engine.Limit(time=0.1))
        self.board.push(bot_move)
        return (1, self.board.fen())

    # Parameter: UCI string containing a potential move
    # Return Value -1: Move is illegal on current board
    # Return Value 0: Game is already over
    # Return Value 1: Move is legal and has been pushed to board move stack
    def update_board(self, uci_string):
        if self.board.is_game_over(): return (0, self.board.fen())

        # Check uci_string is in expected format
        assert re.search(self.uci_string_regex, uci_string)

        # Parse UCI move string and push to board
        move = chess.Move.from_uci(uci_string)
        if not move in self.board.legal_moves: return (-1, self.board.fen())
        self.board.push(move)

        return (1, self.board.fen())
    
    def analyse_position(self):
        analysis = self.engine.analyse(self.board, self.engine.Limit(time=0.1))
        return analysis['score']

    def game_over(self):
        if self.board.is_game_over():
            game_outcome = self.board.outcome()
            self.engine.quit()
            return game_outcome.result()


# Testing
if __name__=='__main__':
    s = Stockfish()
