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

    def get_item(self, item_id):
        return self.cartlist[item_id]

    def get_items(self):
        return self.cartlist

class User(Cart):
    def __init__(self, name):    
        self.name = name
        self.carts = [Cart()]

    def add_cart(self):
        self.carts.append(Cart())

    #def add_item(self, item, amount, cart_index=0):
    #    self.carts[cart_index].add_item(item, amount)
    def view_carts(self):
        return self.carts

def main():
    
    
    test=Cart()
    test.add_item('apple', 30)
    test.get_items()
    

if __name__ == '__main__':
    main() 

