"""This module contains the unit tests for the ShoppingListApplication class"""
import unittest
from flask import session
from app.server import ShoppingListApplication
from app.models.shopping_list import ShoppingList
from app.models.user import User
from app.models.item import Item


class TestShoppingListApplication(unittest.TestCase):
    """Test cases for the ShoppingListApplication class"""

    def setUp(self):
        """This method sets up the variables for the tests"""
        self.application = ShoppingListApplication()

        self.item_1 = Item('Tooth paste', 4000)
        self.shopping_list_1 = ShoppingList('books', {})
        self.shopping_list_2 = ShoppingList('Food', {})

        self.shopping_lists = {
            self.shopping_list_1.title: self.shopping_list_1}
        self.user_1 = User('aturinda', 'ivan', 'ivo', '1234', {})
        self.user_2 = User('aturinda', 'elijah', 'ivo2', '444', self.shopping_lists)

    def test_application_instance(self):
        """This method tests if the class creates an instance of itself"""
        self.assertIsInstance(self.application, ShoppingListApplication,
                              msg='The object should be an instance of the `ShoppingListApplication` class')

    def test_signup(self):
        """This method tests if the class successfully registers users"""
        #self.application.signup(self.user_1.username, self.user_1.password, self.user_1.first_name, self.user_1.last_name)
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.assertTrue("ivo" in self.application.users.keys(),
                        msg='The object should contain the user `ivo`')

    def test_login(self):
        """This method tests if the class successfully signs in users"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.assertTrue("ivo" in self.application.logged_in.keys(),
                        msg='The object should contain the user ivo')
        self.assertTrue(self.application.logged_in["ivo"],
                        msg='The user ivo should be logged in')

    def test_logout(self):
        """This method tests if the class successfully signs out users"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.logout(self.user_1.username)
        self.assertTrue("ivo" in self.application.logged_in.keys(),
                        msg='The object should contain the user ivo')
        self.assertFalse(self.application.logged_in["ivo"],
                         msg='The user ivo should be logged out')

    def test_create_shopping_list(self):
        """This method tests if the class successfully creates new shopping lists"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Shoes", self.user_1.username)
        self.assertTrue("Shoes" in self.application.users[self.user_1.username].shopping_lists.keys(),
                        msg='The object should contain the list Shoes')

    def test_edit_shopping_list(self):
        """This method tests if the class successfully edits shopping lists"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Shoes", self.user_1.username)
        self.application.edit_shopping_list(
            "Shoes", "Flats", self.user_1.username)
        self.assertTrue("Flats" in self.application.users[self.user_1.username].shopping_lists.keys(),
                        msg='The object should contain the list Flats')
        self.assertFalse("Shoes" in self.application.users[self.user_1.username].shopping_lists.keys(),
                         msg='The object should not contain the list Shoes')

    def test_remove_shopping_list(self):
        """This method tests if the class successfully removes shopping lists"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Shoes", self.user_1.username)
        self.application.remove_shopping_list(
            "Shoes", self.user_1.username)
        self.assertFalse("Shoes" in self.application.users[self.user_1.username].shopping_lists.keys(),
                         msg='The object should not contain the list Shoes')

    def test_share_shopping_list(self):
        """This method tests if the class successfully shares shopping lists"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Shoes", self.user_1.username)
        self.application.share_shopping_list(
            "Shoes", self.user_1.username)
        self.assertTrue("Shoes" in self.application.sharing_pool[self.user_1.username].keys(),
                        msg='The object should contain the list Shoes')

    def test_add_item(self):
        """This method tests if the class successfully creates new shopping list items"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Shoes", self.user_1.username)
        self.application.add_item(
            self.item_1.name, "Shoes", self.item_1.price, self.user_1.username)
        self.assertTrue("Tooth paste" in self.application.users[self.user_1.username].shopping_lists["Shoes"].items.keys(),
                        msg='The object should contain the item `Tooth paste`')

    def test_edit_item(self):
        """This method tests if the class successfully edits shopping list items"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Shoes", self.user_1.username)
        self.application.add_item(
            self.item_1.name, "Shoes", self.item_1.price, self.user_1.username)
        self.application.edit_item(
            "Shoes", self.item_1.name, "Coffee", 9000, self.user_1.username)
        self.assertTrue("Coffee" in self.application.users[self.user_1.username].shopping_lists["Shoes"].items.keys(),
                        msg='The object should contain the item `Coffee`')
        self.assertFalse("Tooth paste" in self.application.users[self.user_1.username].shopping_lists["Shoes"].items.keys(),
                         msg='The object should not contain the item `Tooth paste`')

    def test_remove_item(self):
        """This method tests if the class successfully removes shopping list items"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Shoes", self.user_1.username)
        self.application.add_item(
            self.item_1.name, "Shoes", self.item_1.price, self.user_1.username)
        self.application.remove_item(
            "Shoes", "Tooth paste", self.user_1.username)
        self.assertFalse("Tooth paste" in self.application.users[self.user_1.username].shopping_lists["Shoes"].items.keys(),
                         msg='The object should not contain the item `Tooth paste`')

    def test_check_item_toggle(self):
        """This method tests if the class successfully edits shopping list items"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Homers shopping list", self.user_1.username)
        self.application.add_item(
            self.item_1.name, "Homers shopping list", self.item_1.price, self.user_1.username)
        self.application.check_item_toggle(
            "Homers shopping list", self.item_1.name, True, self.user_1.username)
        self.assertTrue(self.application.users[self.user_1.username].shopping_lists["Homers shopping list"].items["Tooth paste"].status,
                        msg='The object status should be True')
        self.application.check_item_toggle(
            "Homers shopping list", self.item_1.name, False, self.user_1.username)
        self.assertFalse(self.application.users[self.user_1.username].shopping_lists["Homers shopping list"].items["Tooth paste"].status,
                         msg='The object status should be False')

    def test_get_all_lists(self):
        """This method tests if the class successfully adds shared shopping lists to the total lists of a user"""
        self.application.signup(self.user_1.first_name, self.user_1.last_name, self.user_1.username, self.user_1.password)
        self.application.login(self.user_1.username, self.user_1.password)
        self.application.create_shopping_list(
            "Homers shopping list", self.user_1.username)
        #self.application.share_shopping_list(
        #    "Homers shopping list", self.user_1.username)
        #self.application.signup(self.user_2.username, self.user_2.email, self.user_2.password)
        self.assertTrue("Homers shopping list" in self.application.get_all_lists(self.user_1.username).keys(),
                        msg='The object should contain the list `Homers shopping list`')


if __name__ == "__main__":
    unittest.main()