import yes
import unittest

class TestExampleFails(unittest.TestCase):

    def test_yes(self):
        self.assertEqual(yes.yes(), False)

if __name__ == '__main__':
    unittest.main()
