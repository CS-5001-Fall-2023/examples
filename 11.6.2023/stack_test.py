from stack import Stack
import unittest

class StackTest(unittest.TestCase):

	def test_constructor(self):
		stack = Stack(10)
		self.assertEquals(stack.max_size, 10)
		self.assertEquals(len(stack.items), 0)

	# push:
	# -- push onto not full stack
	# -- 

	def test_push(self):
		stack = Stack(2)
		stack.push('banana')
		stack.push('apple')
		self.assertEquals(stack.pop(), 'apple')

	def test_push_full(self):
		stack = Stack(2)
		stack.push(5)
		stack.push(4)
		with self.assertRaises(Exception):
			stack.push(4)

	def test_pop_empty(self):
		stack = Stack(5)
		with self.assertRaises(Exception):
			stack.pop()

	def test_pop_item(self):
		stack = Stack(2)
		stack.push('apple')
		stack.push('banana')
		self.assertEquals(stack.pop(), 'banana')

	def test_size_empty(self):
		stack = Stack(5)
		self.assertEquals(stack.size(), 0)

	def test_size(self):
		stack = Stack(5)
		stack.push('apple')
		self.assertEquals(stack.size(), 1)

	def test_size_max(self):
		stack = Stack(2)
		stack.push(4)
		stack.push(5)
		self.assertEquals(stack.size(), 2)


	"""
	Implement at least two tests for each of the following
	methods: push, pop, size. You will submit at least six
	test cases in total.

	Hint: take a look at the documentation for unittest
	https://docs.python.org/3/library/unittest.html
	and consider how you might use the assertRaises method
	"""

def main():
	unittest.main()

if __name__ == '__main__':
	main()




# from stack import Stack

# stack = Stack(10)
# stack.push(9)
# stack.push(8)
# stack.pop()
# stack.push(17)
# stack.pop()
# stack.push(2)
# stack.push(49)
# stack.pop()
# stack.pop()
# stack.push(45)
# stack.push(55)

# print(stack.pop()) 
# print(stack.size())
# stack.debug()
# print(stack.pop()) 
# print(stack.pop()) 
# print(stack.pop()) 