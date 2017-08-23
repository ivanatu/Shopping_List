class ShoppingList(object):
    """This class describes the structure of the ShoppingList object"""

    def __init__(self, title, items):
        """This method creates an instance of the ShoppingList class"""
        self.title = title
        self.items = items

    def add_item(self, item):
        """This method creates an item in the ShoppingList instance"""
        self.items[item.name] = item
        return self.items

    def remove_item(self, item):
        """This method removes an item from the ShoppingList instance"""
        if item.name in self.items.keys():
            del self.items[item.name]
        return self.items

    def change_title(self, title):
        """This method changes the title of the ShoppingList instance"""
        self.title = title
        return self.title