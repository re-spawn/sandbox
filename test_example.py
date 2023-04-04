import example
import unittest

class TestExample(unittest.TestCase):

    def test_yes(self):
        self.assertEqual(example.yes(), True)

if __name__ == '__main__':
    unittest.main()
