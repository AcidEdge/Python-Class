import inc_dec
import unittest
class Test_TestIncrimentDecrement(unittest.TestCase):
    def test_incriment(self):
        self.assertEqual(inc_dec.increment(3), 4)
    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)

if __name__ == '__main__':
    unittest.main()