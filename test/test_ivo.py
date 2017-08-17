import unittest
from apptest.ivo import Item
from apptest.ivo import Cart
from apptest.ivo import User

class CartTestCases(unittest.TestCase):
  def setUp(self):
    self.cart = Cart()
    self.user= User('email', 'pass')
    
  def test_cart_property_initialization(self):
    self.assertIsInstance(self.cart.cartlist, dict, msg='Items is not a dictionary')
    
  def test_add_item(self):
    self.cart.add_item('Eggs', 10)
    self.assertEqual(self.cart.cartlist['Eggs'], 10)
    
  def test_delete_item(self):
    self.cart.add_item('Oranges', 10)
    self.cart.add_item('Mangoes', 10)
    self.cart.delete_item('Oranges', 10)
    
    self.assertEqual(self.cart.cartlist['Mangoes'], 10)

  def test_user_create_shopping_list_successfully(self):
    initial_room_count = len(self.user.shopping_lists)
    cuttlery_list = self.user.create_shopping_list('Cuttlery')
    self.assertTrue(cuttlery_list)
    new_room_count = len(self.user.shopping_lists)
    self.assertEqual(new_room_count - initial_room_count, 1)

  def test_user_update_shopping_list(self):
    self.user.shopping_lists = {'shoes': ['flats']}
    self.assertEqual(self.user.update_shopping_list(
       'shoes', 'flat_shoes'), {'flat_shoes': ['flats']})

  def test_user_update_shopping_list_item(self):
    self.user.shopping_lists = {'shoes': ['flats']}
    self.assertEqual(self.user.update_shopping_list_item(
       'shoes', 'flats', 'flat'), {'shoes': ['flat']})

  def test_user_delete_shopping_list(self):
    self.user.shopping_lists = {'shoes': ['flats', 'highs'], 'grocery': ['onions', 'tomatoes']}
    self.assertEqual(self.user.delete_shopping_list(
        'shoes'), {'grocery': ['onions', 'tomatoes']})
