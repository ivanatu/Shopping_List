class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart(dict):
    def __init__(self):
        self.cartlist={}
        self.last_itemid=0

    def add_item(self, item, amount):
        try:
            if item in self.cartlist.keys():
                self.cartlist[item]+=amount
            else:
                self.cartlist[item]=amount
        except IndexError:
            self.update({
                item.name: [item.price, amount]
            })
    def delete_item(self, item, amount):
        self.cartlist[item]-=amount

    def view_item(self, item_id):
        return self.cartlist[item_id]

    def get_item(self):
        return self.cartlist

class User():

    def __init__(self,  email, password, name=None):
        super().__init__()
        self.email = email
        self.password = password
        self.name = name
        self.carts = [Cart()]
        self.all_users = []
        self.shopping_lists = {}

    def sign_up(self, user) -> int:
   
        if [existing_user for existing_user in self.all_users
            if existing_user.email == user.email]:
            return False

        if self.all_users:
            id = self.all_users[len(self.all_users) - 1].id + 1
            user.id = id
        else:
            user.id = 1
        self.all_users.append(user)
        return user.id

    def sign_in(self, user):
      
        for existing_user in self.all_users:
            if existing_user.email == user.email and existing_user.password == user.password:
                return existing_user.id
        return False


    def sign_out(self) -> None:
        """Signs out a user"""
        self.name = None
        self.email = None
        self.password = None
    

    
    def create_shopping_list(self, name, *items):
        '''
        method creates shopping list and allows users to add an item or multiple items to the list
        '''
        items = list(items)
        if name not in self.shopping_lists.keys():
            self.shopping_lists[name] = [item for item in items]
        elif name in self.shopping_lists.keys():
            return 'Shopping List already exists!'
        return self.shopping_lists

    def read_list(self, name):
        '''
        Returns items from specified list
        '''
        items = []
        if name in self.shopping_lists.keys():
            items = [item for item in self.shopping_lists[name]]
        return items

    def update_shopping_list(self, list_name, new_name):
        '''
        creates shopping list name
        '''
        if list_name in self.shopping_lists.keys():
            # new_name = ShoppingList.name
            self.shopping_lists[new_name] = self.shopping_lists.pop(list_name)
        else:
            return "list name does not exist here"
        return self.shopping_lists

    def update_shopping_list_item(self, list_name, item_name, new_name):
        '''
        creates shopping list name
        '''
        if list_name in self.shopping_lists.keys():
            for item in self.shopping_lists[list_name]:
                if item == item_name:
                    self.shopping_lists[list_name].remove(item)
                    self.shopping_lists[list_name].append(new_name)
                else:
                    return 'Item not in list'
        else:
            return "list name doesn't exist"
        return self.shopping_lists

    def delete_shopping_list(self, list_name):
        '''
        deletes shopping list
        '''
        if list_name in self.shopping_lists.keys():
            del self.shopping_lists[list_name]
        else:
            return 'List name does not exist in the system'
        return self.shopping_lists



