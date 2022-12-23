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
        self.uci_string_regex = r'[a-h][1-8][a-h][1-8]'
        self.engine = chess.engine('/usr/bin/stockfish')
        self.board = chess.board()


    def get_bot_move(self):
        if self.board.is_game_over(): return (0, self.board.fen())
        bot_move = self.engine.play(self.board, chess.engine.Limit(time=0.1))
        self.board.push(bot_move)
        return (1, self.board.fen())

    # Parameter: UCI string containing a potential move
    # Return Value if move is not legal: original fen and 0 for unsucessful
    # Return Value if move legal: new fen and 1 for successful
    def check_move_and_get_fen(self, fen, uci_string):
        # Check uci_string is in expected format
        try:
            assert re.search(self.uci_string_regex, uci_string)
        except:
            return (fen, 0)

        self.board = chess.Board(fen)

        # Parse UCI move string and push to board
        move = chess.Move.from_uci(uci_string)
        if not move in self.board.legal_moves: return (fen, 0)
        self.board.push(move)

        return (self.board.fen(), 1)
    
    def analyse_position(self):
        analysis = self.engine.analyse(self.board, self.engine.Limit(time=0.1))
        return analysis['score']

    async def analyse_position(self) -> None:
        info = await self.engine.analyse(self.board, chess.engine.Limit(time=0.1))
        print(info['score'])
        await self.engine.quit()

    def game_over(self):
        if self.board.is_game_over():
            game_outcome = self.board.outcome()
            self.engine.quit()
            return game_outcome.result()


# Testing
if __name__=='__main__':
    s = Stockfish()
