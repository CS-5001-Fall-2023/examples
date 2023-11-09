from inventory_item import Item
import unittest

class ItemTest(unittest.TestCase):

	def test_update_quantity_sufficient_quantity(self):
		item1 = Item('Twix', 30, 1.99, .5, '1234a')
		item1.update_quantity(5)
		self.assertEqual(item1.quantity, 25)
	
	def test_update_quantity_insufficent_quantity(self):
		item1 = Item('Twix', 30, 1.99, .5, '1234a')
		item1.update_quantity(31)
		self.assertEqual(item1.quantity, 30)
		
	def test_update_quantity_negative_num_to_purchase(self):
		item1 = Item('Twix', 30, 1.99, .5, '1234a')
		item1.update_quantity(-5)
		self.assertEqual(item1.quantity, 30)
		
	def test_update_quantity_zero_num_to_purchase(self):
		item1 = Item('Twix', 30, 1.99, .5, '1234a')
		item1.update_quantity(0)
		self.assertEqual(item1.quantity, 30)

def main():
	unittest.main()

if __name__ == '__main__':
	main()

# Example -- without a test framework
# item1 = Item('Twix', 30, 1.99, .5, '1234a')
# item1.update_quantity(5)
# # verify that item1.quantity is now 25
# if item1.quantity == 25:
# 	print('PASS')
# else:
# 	print('FAIL')
# # print(f'{item1.quantity} -- expected 25')
