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

	def change_quantity(self, new_quantity):
		self.quantity = new_quantity

	def change_price(self, new_price):
		self.price = new_price