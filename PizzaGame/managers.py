from __future__ import absolute_import
from .exceptions import NoValidMove

class TurnManager:
    """
    Manages players turn
    """

    def __init__(self, players):
        self.turn = 0
        self.players = players
        self.choose_first_player()

    def choose_first_player(self):
        import random 
        return random.choice(self.players)

    def get_current_player(self):
        return self.players[self.turn % len(self.players)]

    def next(self):
        self.turn += 1

class StackManager:
    """
    Manages the stack of pizzas
    """

    def __init__(self):
        from random import random
        self.MAX_MOVES=3
        self.set_status(int(random()*10) + 10) # between 10 and 20
        self.last_eat = None

    def set_status(self, value):
        self.status = value

    def eat(self, count):
        """
        Actually eats the pizzas
        """
        self.status -= count
        self.last_eat = count

    def is_poisoned(self, count):
        if count == self.status:
            return True

    def get_valid_moves(self):
        if self.last_eat is None: # the very first move
            return range(1, self.MAX_MOVES+1)

        therange = range(1, min(self.MAX_MOVES, self.status)+1)
        try:
            # last move could be invalid at this turn
            therange.remove(self.last_eat)
        except ValueError:
            pass
        return therange

