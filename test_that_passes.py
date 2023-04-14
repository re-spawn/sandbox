import yes
import unittest

class TestExamplePasses(unittest.TestCase):

    def test_yes(self):
        self.assertEqual(yes.yes(), True)

if __name__ == '__main__':
    unittest.main()
