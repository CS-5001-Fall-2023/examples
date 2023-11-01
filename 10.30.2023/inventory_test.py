from inventory_item import Item

def main():

	# name, quantity, price, weight, sku
	item1 = Item('Twix', 30, 1.99, .5, '1234a')
	item2 = Item('Milky Way', 15, 1.89, .75, '9876z')
	print(item1)
	print(item2)

	item1.change_quantity(50)
	item2.change_quantity(5)

	print(item1)
	print(item2)

	item1.change_price(.25)
	print(item1.price)


	# item1_name = item1.get_name()
	# print(item1_name)

	# item2_name = item2.get_name()
	# print(item2_name)


if __name__ == '__main__':
	main()
