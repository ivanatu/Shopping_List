class Item(object):
    """This class describes the structure of the Item object"""

    def __init__(self, name, price, status=False):
        """This method creates an instance of the Item class"""
        self.name = name
        self.price = price
        self.status = status

    def change_status(self, new_status):
        """This method changes the status in the Item instance"""
        self.status = new_status
        return self.status

    def rename(self, name):
        """This method renames the Item instance"""
        self.name = name
        return self.name

    def change_price(self, price):
        """This method changes the price of the Item instance"""
        self.price = price
        return self.price