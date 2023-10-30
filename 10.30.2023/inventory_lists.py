inventory_item_list = []
inventory_quantity_list = []

def add_new_item(new_item, number_available: int):
	"""
	Add a new item to the inventory with quantity number_available.
	Raises an exception if the item is already in the 
	inventory.
	"""
	if new_item in inventory_item_list:
		raise Exception('We already sell that.')
	inventory_item_list.append(new_item)
	inventory_quantity_list.append(number_available)

def get_number_available(item_to_find) -> int:
	"""
	Return the number of the given item that are available
	in the inventory.
	Raises a KeyError if the item is not found in the inventory.
	"""
	for index, item in enumerate(inventory_item_list):
		if item == item_to_find:
			return inventory_quantity_list[index]			
	raise KeyError(f'Key {item_to_find} not found.')

def update_number_available(item_to_find, number_purchased: int):	
	"""
	Update the number of the given item that are available in 
	the inventory.
	Raises an Exception if there is not a sufficient quantity 
	of the item available. 
	"""
	for index, item in enumerate(inventory_item_list):
		if item == item_to_find:
			if inventory_quantity_list[index] >= number_purchased:
				inventory_quantity_list[index] -= number_purchased
				return True
			else:
				raise Exception('Insuffient quantity.')
	raise KeyError(f'Key {item_to_find} not found.')

def show_inventory():
	"""
	Display the item names and amounts for all items in the
	inventory.
	"""
	print('Inventory:')
	for i in range(len(inventory_item_list)):
		print(f'\t{inventory_item_list[i]} - {inventory_quantity_list[i]}')

def main():
	try:
		add_new_item('Kit Kat', 15)
		add_new_item('Twix', 25)
		add_new_item('Milky Way', 30)
		show_inventory()
		# print(get_number_available('Twix'))
		update_number_available('Twix', 5)
		show_inventory()
	except Exception as ex:
		print('exception occurred')
		print(ex)

if __name__ == '__main__':
	main()