import unittest
from unittest.ivo import Item
from unittest.ivo import Cart
from unitest.ivo import User

class CartTestCases(unittest.TestCase):
  def setUp(self):
    self.cart = Cart()
    
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

