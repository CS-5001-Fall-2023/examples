class Stack:

	def __init__(self, max_size):
		self.items = []
		self.max_size = max_size

	def push(self, item):
		if len(self.items) >= self.max_size:
			raise Exception('Stack Full')
		self.items.append(item)

	def pop(self):
		if len(self.items) == 0:
			raise Exception('Stack Empty')
		item = self.items.pop()
		return item

	def size(self):
		return len(self.items)

	def debug(self):
		print(self.items)


