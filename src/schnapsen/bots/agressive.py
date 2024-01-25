
from schnapsen.game import Bot, Move, PlayerPerspective, GamePhase
from schnapsen.game import SchnapsenTrickScorer
from schnapsen.deck import Card, Suit, Rank
import random
from typing import Optional


class AgressiveBot(Bot):

    def __init__(self, start_agressive: bool, rand: random.Random, name: Optional[str] = None) -> None:
        super().__init__(name)
        self.start_agressive = start_agressive
        self.rng = rand

    def get_move(self, perspective: PlayerPerspective, leader_move: Optional[Move]) -> Move:

        moves: list[Move] = perspective.valid_moves()

        if self.is_phase_one(perspective):
            if self.start_agressive:
                return self.agressive_move(perspective, moves)
            else:
                return self.random_move(perspective, moves)
        else:
            if self.start_agressive:
                return self.random_move(perspective, moves)
            else:
                return self.agressive_move(perspective, moves)

    def is_phase_one(self, perspective: PlayerPerspective) -> bool:
        if perspective.get_phase() == GamePhase.ONE:
            return True
        return False
    
    def agressive_move(self, perspective: PlayerPerspective, moves: list[Move]) -> Move:

        if self.trump_exchange_possible(perspective, moves):
            return self.play_trump_exchange(perspective, moves)
        elif self.marriage_possible(perspective, moves):
            return self.play_highest_marriage(perspective, moves)
        elif self.trump_possible(perspective, moves):
            return self.play_highest_trump(perspective, moves)
        else:
            return self.play_highest_regular_move(perspective, moves)
        
    def trump_exchange_possible(self, perspective: PlayerPerspective, moves: list[Move]) -> bool:
        """Returns true if a trump exchange is possible"""
        for move in moves:
            if move.is_trump_exchange():
                return True
        
        return False
    
    def marriage_possible(self, perspective: PlayerPerspective, moves: list[Move]) -> bool:
        """Returns true if a marriage is possible"""
        for move in moves:
            if move.is_marriage():
                return True
        return False
    
    def trump_possible(self, perspective: PlayerPerspective, moves: list[Move]) -> bool:
        """Returns true if a trump is possible"""
        trump_suit: Suit = perspective.get_trump_suit()
        for move in moves:
            if move.card.suit == trump_suit:
                return True
        return False
    
    def play_trump_exchange(self, perspective: PlayerPerspective, moves: list[Move]) -> Move:
        """Returns trump exchange"""
        for move in moves:
            if move.is_trump_exchange():
                return move
    
    def play_highest_marriage(self, perspective: PlayerPerspective, moves: list[Move]) -> Move:
        """Checks if a royal marriage is possible and if so returns the royal marriage. If not the function
        returns the first possible marriage."""
        trump_suit: Suit = perspective.get_trump_suit()
        marriages: list[Move] = [move for move in moves if move.is_marriage()]
        
        for marriage in marriages:
            if marriage._cards()[0].suit == trump_suit:
                return marriage
        return marriages[0]
    
    def play_highest_trump(self, perspective: PlayerPerspective, moves: list[Move]) -> Move:
        trump_suit: Suit = perspective.get_trump_suit()
        trumps: list[Move] = [move for move in moves if move.card.suit == trump_suit]
        highest_trump = max(trumps, key=lambda move: move.card.rank.value)
        return highest_trump
    
    def play_highest_regular_move(self, perspective: PlayerPerspective, moves: list[Move]) -> Move:
        highest_regular_move = max(moves, key=lambda move: move.card.rank.value)
        return highest_regular_move

    def random_move(self, perspective: PlayerPerspective, moves: list[Move]) -> Move:
        move = self.rng.choice(moves)
        return move



    
