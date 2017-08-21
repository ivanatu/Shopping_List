"""This module contains the core functionality methods of the Shopping List application"""
from app.models.item import Item
from app.models.shopping_list import ShoppingList
from app.models.user import User


class ShoppingListApplication(object):
    """This This class describes the structure of the ShoppingListApplication object"""

    def __init__(self):
        self.users = {}
        self.logged_in = {}
        self.sharing_pool = {}

    def login(self, username, password):
        """This method enables stored users to login"""
        self.logged_in[username] = False
        if self.users and username in self.users.keys():
            user = self.users[username]
            if user.password == password:
                self.logged_in[user.username] = True
        return self.logged_in[username]

    def logout(self, username):
        """This method enables stored users to logout"""
        if username in self.logged_in.keys():
            self.logged_in[username] = False
        return self.logged_in[username]

    def signup(self, first_name, last_name, username, password):
        """This method enables new users to create accounts"""
        if username in self.users.keys():
            return None
        new_user = User(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            shopping_lists={}
        )
        self.users[new_user.username] = new_user
        self.logged_in[new_user.username] = True
        return self.users[new_user.username]

    def create_shopping_list(self, title, username):
        """This method enables logged in users to create new shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            title = title.replace("'", "`").replace('"', '``')
            new_shopping_list = ShoppingList(title, {})
            user = self.users[username]
            return user.create_shopping_list(new_shopping_list)
        return None

    def edit_shopping_list(self, old_title, new_title, username):
        """This method enables logged in users to edit their shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            new_title = new_title.replace("'", "`").replace('"', '``')
            user = self.users[username]
            return user.edit_shopping_list(old_title, new_title).title == new_title
        return None

    def remove_shopping_list(self, title, username):
        """This method enables logged in users to edit their shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            user = self.users[username]
            if title in user.shopping_lists.keys():
                shopping_list = user.shopping_lists[title]
                return user.remove_shopping_list(shopping_list)
        return None

    def share_shopping_list(self, title, username):
        """This method enables logged in users to share their shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            user = self.users[username]
            if title in user.shopping_lists.keys():
                not_existing = True
                if user.username in self.sharing_pool.keys():
                    if title in self.sharing_pool[user.username].keys():
                        not_existing = False
                if not_existing:
                    self.sharing_pool[user.username] = {
                        title: user.shopping_lists[title]}
                    return True
        return False

    def add_item(self, name, list_title, price, username):
        """This method enables logged in users to add items to their shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            user = self.users[username]
            if list_title in user.shopping_lists.keys():
                shopping_list1 = user.shopping_lists[list_title]
                name = name.replace("'", "`").replace('"', '``')
                if name not in shopping_list1.items.keys():
                    new_item = Item(name, price)
                    return shopping_list1.add_item(new_item)
        return None

    def edit_item(self, list_title, old_name, new_name, new_price, username):
        """This method enables logged in users to add items to their shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            user = self.users[username]
            if list_title in user.shopping_lists.keys():
                shopping_list2 = user.shopping_lists[list_title]
                if old_name in shopping_list2.items.keys():
                    item = shopping_list2.items[old_name]
                    new_name = new_name.replace("'", "`").replace('"', '``')
                    item.rename(new_name)
                    item.change_price(new_price)
                    shopping_list2.items[new_name] = item
                    if not old_name == new_name:
                        del shopping_list2.items[old_name]
                    return item.name == new_name and item.price == new_price
        return False

    def remove_item(self, list_title, name, username):
        """This method enables logged in users to remove items from their shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            user = self.users[username]
            if list_title in user.shopping_lists.keys():
                shopping_list3 = user.shopping_lists[list_title]
                if name in shopping_list3.items.keys():
                    item1 = shopping_list3.items[name]
                    return shopping_list3.remove_item(item1)
        return None

    def check_item_toggle(self, list_title, name, new_status, username):
        """This method enables logged in users to check and uncheck items on their shopping lists"""
        if username in self.logged_in.keys() and self.logged_in[username]:
            user = self.users[username]
            if list_title in user.shopping_lists.keys():
                shopping_list4 = user.shopping_lists[list_title]
                if name in shopping_list4.items.keys():
                    item2 = shopping_list4.items[name]
                    return item2.change_status(new_status)
        return None

    def get_all_lists(self, username):
        """This method gets all the shopping lists for a user"""
        if username in self.logged_in.keys() and self.logged_in[username] and username in self.users.keys():
            user = self.users[username]
            if self.sharing_pool:
                for share_username, shopping_list_dict in self.sharing_pool.items():
                    if not share_username == user.username:
                        for title, shared_shopping_list in shopping_list_dict.items():
                            if title not in user.shopping_lists.keys():
                                user.shopping_lists[title] = shared_shopping_list
                                break
            return user.shopping_lists
        return {}
