from .core import PizzaGame
import unittest

def test_race():
    p = PizzaGame()
    p.status = 2
    p.last_eat = 2
    p.main()

class PizzaGameTest(unittest.TestCase):
    def setUp(self):
        self.p = PizzaGame()
        
    def tearDown(self):
        pass

    def test_n_invalid_after_eat_n_pizzas(self):
        self.p.stack.eat(2)
        assert self.p.stack.last_eat == 2

    def test_valid_moves_after_2_with_stack_2(self):
        self.p.stack.set_status(4)
        self.p.stack.eat(2)
        assert self.p.stack.get_valid_moves() == [1]


    def test_game(self):
        self.p.stack.set_status(10)
        self.p.stack.eat(2)
        self.p.stack.eat(3)
        self.p.stack.eat(2)
        assert self.p.stack.is_poisoned(4)

if __name__ == '__main__':
    unittest.main()
