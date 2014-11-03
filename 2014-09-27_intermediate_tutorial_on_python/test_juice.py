import unittest

def juice_maker(fruit):
    if fruit.startswith('A'):
        return 'APPLE FOOL'
    elif fruit.startswith('B'):
        return 'BANANA BOY'
    return fruit + ' Juice'

class JuiceMakerTestCase(unittest.TestCase):
    def setUp(self):
        print ('Set up db')

    def test_juice_maker_B(self):
        fruit = 'Banana'
        result = juice_maker(fruit)
        self.assertEqual(result, 'BANANA BOY')

    def test_juice_maker_A(self):
        fruit = 'Apple'
        result = juice_maker(fruit)
        self.assertEqual(result, 'APPLE FOOL')

    def test_juice_maker_all_else(self):
        fruit = 'Orange'
        result = juice_maker(fruit)
        self.assertEqual(result, fruit + ' Juice')

    def tearDown(self):
        print ('Delete db')


if __name__ == '__main__':
    unittest.main()
