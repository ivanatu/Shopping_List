import unittest
from datetime import datetime
from app.models.user import User
from app.models.shopping_list import ShoppingList
from app.models.item import Item


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """This method sets up the variables for the tests"""
        self.item_1 = Item('bread', 4000)
        self.shopping_list_1 = ShoppingList('drinks', {})
        self.shopping_list_2 = ShoppingList('clothes', {})

        self.shopping_lists = {self.shopping_list_1.title: self.shopping_list_1}
        self.user_no_list = User('aturinda', 'ivan', 'ivo', '1234', {})
        self.user_with_list = User('aturinda', 'elijah','ivo2', '444', self.shopping_lists)

    # def test_user_instance(self):
    #     """This method tests if the User class creates an instance of itself"""
    #     self.assertIsInstance(self.user_no_list, User,
    #                           msg='The object should be an instance of the `User` class')

    # def test_user_attributes(self):
    #     """This method tests if the class assigns the right attributes to User instances"""
    #     self.assertEqual('homie', self.user_no_list.username,
    #                      msg='The object username should be `homie`')

    def test_change_password(self):
        """This method tests if the User class changes the password of an instance"""
        self.user_no_list.change_password("12345")
        self.assertEqual(self.user_no_list.password, "12345", msg='The object password should be 12345')

    def test_create_shopping_list(self):
        """This method tests if the class adds a shopping_list to User instances"""
        before = len(self.user_no_list.shopping_lists)
        self.user_no_list.create_shopping_list(self.shopping_list_2)
        after = len(self.user_no_list.shopping_lists)
        self.assertEqual(1, after - before,
                         msg='The object should add a shopping list to the instance')

    def test_remove_shopping_list(self):
        """This method tests if the class removes a shopping list from User instances"""
        before = len(self.user_no_list.create_shopping_list(self.shopping_list_2))
        after = len(self.user_no_list.remove_shopping_list(self.shopping_list_2))
        self.assertEqual(1, before - after,
                         msg='The object should remove a shopping list from the instance')

    def test_edit_shopping_list(self):
        """This method tests if the class edits a shopping list from User instances"""
        before = self.shopping_list_1.title
        after = self.user_with_list.edit_shopping_list(before, "My new list").title
        self.assertEqual(after, "My new list",
                         msg='The object should rename the shopping list to My new list')

if __name__ == "__main__":
    unittest.main()