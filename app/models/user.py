class User(object):
    """This class describes the structure of the User object"""


    def __init__(self, username, password, first_name, last_name, shopping_lists):
        """This method creates an instance of the User class"""
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.shopping_lists = shopping_lists

    def change_password(self, new_password):
        """This method changes the password of the User instance"""
        self.password = new_password
        return self.password

    def create_shopping_list(self, shopping_list):
        """This method creates a shopping list in the User instance"""
        self.shopping_lists[shopping_list.title] = shopping_list
        return self.shopping_lists

    def remove_shopping_list(self, shopping_list):
        """This method removes a shopping list from the User instance"""
        if shopping_list.title in self.shopping_lists.keys():
            del self.shopping_lists[shopping_list.title]
        return self.shopping_lists

    def edit_shopping_list(self, old_title, new_title):
        """This method changes the title of a shopping list in the User instance"""
        shopping_list = None
        if old_title in self.shopping_lists.keys():
            shopping_list = self.shopping_lists[old_title]
            shopping_list.change_title(new_title)
            self.shopping_lists[new_title] = shopping_list
            if not old_title == new_title:
                del self.shopping_lists[old_title]
        return self.shopping_lists[new_title]