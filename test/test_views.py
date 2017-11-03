import os
import unittest
from flask import session
from app import app
from app.views import the_application


class FlaskTestCase(unittest.TestCase):
    """Test cases for the application views"""

    def setUp(self):
        """This method initializes the varibles of the tests"""
        self.tester = app.test_client(self)
        app.secret_key = os.urandom(12)
        the_application.signup("aturinda", "ivan", "ivo", "1234")

    def test_index(self):
        """This method tests if the route / returns 200"""
        response = self.tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200,
                         msg="The route should return status 200")

    # def test_signup(self):
    #     """This method tests if the application signs up users correctly"""
    #     with self.tester as the_tester:
    #         the_tester.post("/create", data=dict(first_name="aturinda", last_name="ivan", username="ivo", password="1234"),
    #                         follow_redirects=True)
    #         self.assertEqual("ivo", session['username'],
    #             msg="The session should contain a username `ivo`")

    def test_login(self):
        """This method tests if the application logs in users correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            self.assertTrue(the_application.logged_in["ivo"],
                            msg="The session user `ivo` should be logged in")

    def test_logout(self):
        """This method tests if the application logs out users correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.get("/logout", follow_redirects=True)
            self.assertFalse(the_application.logged_in["ivo"],
                             msg="The session user ivo should be logged out")

    def test_create_shopping_list(self):
        """This method tests if the application creates shopping lists correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.post("/create_shopping_list",
                            data=dict(title="List 1"), follow_redirects=True)
            self.assertIn("List 1", the_application.get_all_lists("ivo").keys(),
                          msg="There should be a list named `List 1` in the user lists")

    def test_edit_shopping_list(self):
        """This method tests if the application edits shopping lists correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.post("/create_shopping_list",
                            data=dict(title="List 1"), follow_redirects=True)
            the_tester.post("/edit_shopping_list",
                            data=dict(old_title="List 1",
                                      new_title="New List"),
                            follow_redirects=True)
            self.assertIn("New List", the_application.get_all_lists("ivo").keys(),
                          msg="There should be a list named `List 1` in the user lists")
            self.assertNotIn("List 1", the_application.get_all_lists("ivo").keys(),
                             msg="There should be a list named `List 1` in the user lists")

    def test_remove_shopping_list(self):
        """This method tests if the application removes shopping lists correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.post("/create_shopping_list",
                            data=dict(title="List 1"), follow_redirects=True)
            the_tester.get("/remove_shopping_list/List 1",
                           follow_redirects=True)
            self.assertNotIn("List 1", the_application.get_all_lists("ivo").keys(),
                             msg="There should not be a list named `List 1` in the user lists")

    def test_add_item(self):
        """This method tests if the application adds shopping list items correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.post("/create_shopping_list",
                            data=dict(title="List 1"), follow_redirects=True)
            the_tester.post("/add_item",
                            data=dict(list_title="List 1", name="Item 1", price=5000), follow_redirects=True)
            self.assertIn("Item 1", the_application.users["ivo"].shopping_lists["List 1"].items.keys(),
                          msg="There should be an item named `Item 1` in the user list items")

    def test_edit_item(self):
        """This method tests if the application edits shopping list items correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.post("/create_shopping_list",
                            data=dict(title="List 1"), follow_redirects=True)
            the_tester.post("/add_item",
                            data=dict(list_title="List 1", name="Item 1", price=5000), follow_redirects=True)
            the_tester.post("/edit_item",
                            data=dict(list_title="List 1", old_name="Item 1",
                                      new_name="New Item", price=3000),
                            follow_redirects=True)
            self.assertIn("New Item", the_application.users["ivo"].shopping_lists["List 1"].items.keys(),
                          msg="There should be an item named `New Item` in the user list items")
            self.assertNotIn("Item 1", the_application.users["ivo"].shopping_lists["List 1"].items.keys(),
                             msg="There should not be an item named `Item 1` in the user list items")

    def test_remove_item(self):
        """This method tests if the application removes shopping list items correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.post("/create_shopping_list",
                            data=dict(title="List 1"), follow_redirects=True)
            the_tester.post("/add_item",
                            data=dict(list_title="List 1", name="Item 1", price=5000), follow_redirects=True)
            the_tester.get(
                "/remove_item?list_title='List 1'&name='Item 1'", follow_redirects=True)

            self.assertIn("Item 1", the_application.users["ivo"].shopping_lists["List 1"].items.keys(),
                             msg="There should not be an item named `Item 1` in the user list items")

    def test_check_item_toggle(self):
        """This method tests if the application edits shopping list item statuses correctly"""
        with self.tester as the_tester:
            the_tester.post("/login", data=dict(username="ivo", password="1234"),
                            follow_redirects=True)
            the_tester.post("/create_shopping_list",
                            data=dict(title="List 1"), follow_redirects=True)
            the_tester.post("/add_item",
                            data=dict(list_title="List 1", name="Item 1", price=5000), follow_redirects=True)
            the_tester.get("/check_item_toggle?list_title='List 1'&name='Item 1'&new_status='false'",
                           follow_redirects=True)
            self.assertFalse(the_application.users["ivo"].shopping_lists["List 1"].items["Item 1"].status,
                             msg="The status of item `Item 1` should be False")


if __name__ == '__main__':
    unittest.main()