import unittest
from app.models.item import Item
from app.models.shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    """Test cases for the ShoppingList class"""

    def setUp(self):
        """This method sets up the variables for the tests"""
        self.item_1 = Item('Soap', 2500)
        self.item_2 = Item('Pringles', 7500)
        self.item_3 = Item('Cake', 10000)

        self.items = {self.item_1.name: self.item_1,
                      self.item_2.name: self.item_2}
        self.shopping_list_1 = ShoppingList('drinks', {})
        self.shopping_list_2 = ShoppingList('clothes', self.items)

    def test_add_item(self):
        """This method tests if the class adds an item to ShoppingList instances"""
        before = len(self.shopping_list_1.items)
        self.shopping_list_1.add_item(self.item_3)
        after = len(self.shopping_list_1.items)
        self.assertEqual(1, after - before,
                         msg='The object should add an item to the instance')

    def test_remove_item(self):
        """This method tests if the class removes an item from ShoppingList instances"""
        before = len(self.shopping_list_1.add_item(self.item_3))
        after = len(self.shopping_list_1.remove_item(self.item_3))
        self.assertEqual(1, before - after,
                         msg='The object should remove an item from the instance')

    def test_change_title(self):
        """This method tests if the ShoppingList class changes the title of an instance"""
        self.shopping_list_1.change_title("My shopping list")
        self.assertEqual(self.shopping_list_1.title, "My shopping list",
                         msg='The object title should be `My shopping list`')


if __name__ == "__main__":
    unittest.main()