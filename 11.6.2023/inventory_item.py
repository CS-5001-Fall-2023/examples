class Item:

	def __init__(self, name, quantity, price, weight, sku):
		self.name = name
		self.quantity = quantity
		self.price = price
		self.weight = weight
		self.sku = sku
		self.number_sold = 0

	def __str__(self):
		return f'{self.name} - {self.quantity}'

	def get_name(self):
		return self.name

	# Test 1
	# create an instance of Item
	# call update_quantity with number_purchased <= quantity
	# check if quantity is correct

	def update_quantity(self, number_purchased):
		if (self.quantity >= number_purchased
			and number_purchased > 0):
			self.quantity -= number_purchased
		# TODO: what happens if there aren't enough
		# TODO: number_purchased not an int

	def change_price(self, new_price):
		self.price = new_price		

		