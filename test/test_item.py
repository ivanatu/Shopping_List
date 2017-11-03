import unittest
from app.models.item import Item


class TestItem(unittest.TestCase):
    """Test cases for the Item class"""

    def setUp(self):
        """This method sets up the variables for the tests"""
        self.item_1 = Item('Coffee', 9000)
        self.item_2 = Item('Sugar', 5000)

    def test_status_change(self):
        """This method tests if the Item class changes the status of an instance"""
        self.item_1.change_status(True)
        self.assertTrue(self.item_1.status, msg='The object should be of have a status `True`')

    def test_rename(self):
        """This method tests if the Item class changes the name of an instance"""
        self.item_1.rename("Tea bags")
        self.assertEqual(self.item_1.name, "Tea bags", msg='The object name should be `Tea bags`')

    def test_price_change(self):
        """This method tests if the Item class changes the price of an instance"""
        self.item_2.change_price(3000)
        self.assertEqual(self.item_2.price, 3000, msg='The object price should be 30')


if __name__ == "__main__":
    unittest.main()