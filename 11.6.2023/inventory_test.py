from inventory_item import Item
from inventory import Inventory

def main():

	item1 = Item('Twix', 30, 1.99, .5, '1234a')
	item1.update_quantity(5)
	# verify that item1.quantity is now 25


	# inventory = Inventory()

	# # option 1
	# inventory.add_new_item('Twix', 30, 1.99, .5, '1234a')
	# inventory.add_new_item('Milky Way', 15, 1.89, .75, '9876z')

	# # # option 2
	# # item1 = Item('Twix', 30, 1.99, .5, '1234a')
	# # inventory.add_new_item(item1)


	# print(inventory.get_number_available('Twix')) # 30
	# inventory.update_number_available('Twix', 5)
	# print(inventory.get_number_available('Twix')) # 25

	# inventory.show_inventory()
	# print(inventory)


	# # # name, quantity, price, weight, sku
	
	# # item2 = Item('Milky Way', 15, 1.89, .75, '9876z')
	# # # item3 = Item('Snickers', price=1.89, weight=.5, sku='9293z')
	# # print(item3)
	# # print(item1)
	# # # print(item2)

	# # # item1.change_quantity(50)
	# # # item2.change_quantity(5)

	# # # print(item1)
	# # # print(item2)

	# # # item1.change_price(.25)
	# # # print(item1.price)


	# # # # item1_name = item1.get_name()
	# # # # print(item1_name)

	# # # # item2_name = item2.get_name()
	# # # # print(item2_name)


if __name__ == '__main__':
	main()
