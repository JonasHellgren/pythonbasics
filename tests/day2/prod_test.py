import unittest
from src.day_two.Product import Product


class TestProduct(unittest.TestCase):

    def test_product_calculation(self):
        p = Product(3, 4)
        self.assertEqual(p.calculate(), 12)


if __name__ == "__main__":
    unittest.main()
