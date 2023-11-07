from inventory_item import Item

class Inventory:

	def __init__(self):
		self.inventory = {}

	# new_item, number_available: int
	# option 1
	def add_new_item(self, name, quantity=0, price=0, weight=0, sku=0):
		item = Item(name, quantity, price, weight, sku)
		# TODO: error checking to ensure we don't overwrite an item
		self.inventory[name] = item

	# # option 2
	# def add_new_item(self, item):
	# 	# TODO: error checking to ensure we don't overwrite an item
	# 	self.inventory[name] = item

	def get_number_available(self, item_to_find) -> int:
		return self.inventory[item_to_find].quantity

	def update_number_available(self, item_to_find, number_purchased: int):
		self.inventory[item_to_find].update_quantity(number_purchased)

	def show_inventory(self):
		print('Inventory:')
		for item in self.inventory.values():
			print(f'\t{item}')

	def __str__(self):
		result = 'Inventory:\n'
		for item in self.inventory.values():
			result += f'\t{item}\n'
		return result


