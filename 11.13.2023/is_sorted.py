def is_sorted(things: list) -> bool:
	""""Returns true if the list of things is
	sorted and false otherwise.
	
	start at beginning
	compare adjacent items
	if left is greater than right
	   return False
	else
	   keep going
	if get to end of list: return True

	"""
	for i in range(len(things)-1):
		if things[i] > things[i+1]:
			return False
	return True


def main():
	things = [1, 2, 3, 4, 5, 6]
	# should return true
	print(f'{things} - {is_sorted(things)}')

	things = ['a', 'b', 'c', 'e', 'd']
	# should return false
	print(f'{things} - {is_sorted(things)}')

if __name__ == '__main__':
	main()