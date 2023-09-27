'''
Practice with lists!
'''

def fun_with_lists():
	'''
	What can you do with a list?!
	'''
	# Lists are mutable!
	# Creating a list
	# Accessing elements of a list
	# Modifying lists
	# Appending to a list
	# Lists of mixed types
	# Slicing a list
	names = ['amy', 'anna', 'bob']
	values = [34, 5, 2, 5, 17]
	mixed_type_list = ['may', 15, 73.5]
	mixed_type_list.append('hello')
	print(values[1:3])

	# index = 0
	# while index < len(mixed_type_list):
	# 	print(mixed_type_list[index])
	# 	index += 1
	# mixed_type_list[0] = 'june'
	# index = 0
	# while index < len(mixed_type_list):
	# 	print(mixed_type_list[index])
	# 	index += 1


def list_to_string(list_of_string: list[str]) -> str:
	'''
	A function that takes a list of strings and
	combines them into a single string with 
	spaces between each word. Returns the string.		
	'''
	result = ''
	index = 0
	while index < len(list_of_string):
		result += list_of_string[index] + ' '
		index += 1
	return result


def greater_than_100(values: list[int]) -> int:
	'''
	A function that takes as input a list of ints
	and returns the number of ints in the list that
	are greater than 100.
	'''
	TARGET = 100
	count = 0
	index = 0
	while index < len(values):
		if values[index] > TARGET:
			count += 1
		index += 1
	return count

def main():
	# fun_with_lists()
	# values = []
	# result = greater_than_100(values)
	# print(result)
	months = ['may', 'june', 'august', 'september']
	result = list_to_string(months)
	print(result)

if __name__ == '__main__':
	main()

