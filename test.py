import unittest

class TestSuma(unittest.TestCase):
    def test_suma(self):
        from main import suma
        self.assertEqual(suma(3, 4), 7)


if __name__ == "__main__":
    unittest.main()