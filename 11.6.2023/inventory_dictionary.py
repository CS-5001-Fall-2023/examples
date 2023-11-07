inventory = {}

def add_new_item(new_item, number_available: int):
	if new_item in inventory:
		raise Exception('We already sell that.')
	inventory[new_item] = number_available

def get_number_available(item_to_find) -> int:
	return inventory[item_to_find]

def update_number_available(item_to_find, number_purchased: int):
	if number_purchased <= inventory[item_to_find]:
		inventory[item_to_find] -= number_purchased
	else:
		raise Exception('Insufficent quantity.')
		
def show_inventory():
	print('Inventory:')
	for item in inventory.keys():
		print(f'\t{item} - {inventory[item]}')


def main():
	try:
		add_new_item('Kit Kat', 15)
		add_new_item('Twix', 25)
		add_new_item('Milky Way', 30)
		show_inventory()
		# print(get_number_available('reeses'))
		update_number_available('Twix', 5)
		show_inventory()
	except KeyError as ex:
		print('exception occurred')
		print(ex)

if __name__ == '__main__':
	main()