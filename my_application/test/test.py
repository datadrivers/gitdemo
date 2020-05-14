import unittest
from my_application.src import main

class TestCalc(unittest.TestCase):

    def test_sell_and_buy_is_equal_greater_the_origin(self):
        euro_amount = 100
        sell = main.sell(euro_amount,"US-Dollar")
        buy = main.buy(sell,"US-Dollar")
        self.assertGreaterEqual(euro_amount,buy)

if __name__ == "__main__":
    unittest.main()
