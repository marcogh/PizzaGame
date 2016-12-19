from __future__ import absolute_import
from .exceptions import NoValidMove
from .managers import StackManager, TurnManager


class PizzaGame:

    def __init__(self):
        from random import random

        self.players = ['Player One', 'Player Two']

        self.turn = TurnManager(self.players)
        self.stack = StackManager()

    #def is_valid(self, count):
        #if count == 0 or count > self.MAX_MOVES or count == self.last_eat:
            #return False
        #return True

    def main(self):
        while True:
            try: 
                count = self.get_eaten_pizzas()
            except NoValidMove:
                self.stack.eat(0) # the other has lost!
                continue 

            if self.stack.is_poisoned(count):
                print "You lose, the pizza was poisoned!"
                break

            self.stack.eat(count)
            self.turn.next()

    def get_eaten_pizzas(self):
        valid_moves = self.stack.get_valid_moves()
        if len(valid_moves) == 0:
            print "\n%s, you cannot move. You skip your turn." % (
                                    self.turn.get_current_player())
            raise NoValidMove

        while True:
            """
            Waits until a valid input
            """
            print "\n%s pizzas left.\n%s, it's your turn." % (
                            self.stack.status, self.turn.get_current_player())
            try:
                count = int(raw_input('  How many pizzas you want to eat? '))
                if count not in valid_moves:
                    raise ValueError
            except ValueError:
                print "  %s is not a valid number. Valid moves are %s" % (
                        count, valid_moves)
                continue
            return count


if __name__ ==  "__main__":
    p = PizzaGame()
    p.main()

