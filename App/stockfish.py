# Stockfish Chess Engine  API for 
# Move Analysis, Bot v. Bot & Bot v. Human
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
    def __init__(self):
        self.uci_string_regex = r'[a-h][1-8][a-h][1-8]'
        asyncio.run(self.__init_engine())
        self.board = chess.Board()
        
        #self.__update_board('g1f3')

    # Public Methods:
    async def bot_v_bot(self) -> None:
        self.transport, self.engine = await chess.engine.popen_uci('/usr/bin/stockfish')
        self.board = chess.Board()
        while not self.board.is_game_over():
            result = await self.engine.play(self.board, chess.engine.Limit(time=0.1))
            self.board.push(result.move)
            print('\n',self.board)

        await self.engine.quit()

    #async def human_v_human(self) -> None:
    async def analyse_position(self) -> None:
        info = await self.engine.analyse(self.board, chess.engine.Limit(time=0.1))
        print(info['score'])
        await self.engine.quit()

    # Private Methods:

    # Parameter: UCI string containing a potential move
    # Return Value 0: Move is illegal on current board
    # Return Value 1: Move is legal and has been pushed to board move stack
    def __update_board(self, uci_string) -> None:
        # Check simple_command is in expected format
        assert re.search(self.uci_string_regex, uci_string)

        # Parse UCI move string and push to board
        move = chess.Move.from_uci(uci_string)
        if not move in self.board.legal_moves: return 0
        self.board.push(move)

        return 1
    
    async def __init_engine(self) -> None:
        #asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
        self.transport, self.engine = await chess.engine.popen_uci('/usr/bin/stockfish')
        #await self.engine.quit()

# Testing
if __name__=='__main__':
    s = Stockfish()
    asyncio.run(s.bot_v_bot())
    asyncio.run(s.analyse_position())
