import unittest

def broken_addition(x, y):
    return_value = x + y + 1
    return return_value

class PyLadiesTC(unittest.TestCase):
    def test_my_addition_func(self):
        return_value = broken_addition(1, 3)
        self.assertEqual(return_value, 3)

    def love_testing(self):
        """Methods must start with test* to be run as a test"""
        return_value = broken_addition(2, 5)
        self.assertEqual(return_value, 7)

if __name__ == '__main__':
    unittest.main()
