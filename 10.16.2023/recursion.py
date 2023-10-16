'''
Practice with recursion!
'''

def factorial_iterative(n: int) -> int:
	"""
	A function that takes as input an integer and returns the 
	factorial of that number.
	"""
	result = 1
	for i in range(1, n+1):
		# result = result * i  
		result *= i  
	return result

def factorial_recursive(n: int) -> int:
	"""
	A function that takes as input an integer and returns the 
	factorial of that number.
	This implementation does not use a loop.
	"""
	if n == 1:
		return 1	
	return n * factorial_recursive(n-1)

def print_string(string: str):
	"""
	Implement a recursive function that takes as input a str and prints 
	the characters of the str one per line *without using a loop*. 
	"""
	# if len(string) == 1:
	# 	print(string)	
	# else:
	# 	print(string[0])
	# 	print_string(string[1:])	

	if len(string) == 0:
		return
	print(string[0])
	print_string(string[1:])	

def print_string_backward(string: str):
	"""
	Implement a recursive function that takes as input a str and prints 
	the characters of the str *in reverse* one per line *without using a loop*. 
	"""
	if len(string) == 0:
		return
	print_string_backward(string[1:])	
	print(string[0])
	

def print_nums_iterative(n: int):
	"""
	A function that takes as input a number and prints from 1 to 
	the number (inclusive).
	"""
	for i in range(1, n+1):
		print(i)

def print_nums_recursive(n: int):
	"""
	Implement print_nums_iterative above without using a loop.
	There are several ways to do this. We will look at how to
	use a helper function.
	"""
	# if n <= 0:
	# 	return
	# if n == 1:
	# 	print(n)
	# 	return
	# print(n)
	# print_nums_recursive(n-1)
	print_nums_helper(1, n)

def print_nums_helper(current: int, n: int):
	# print_nums_helper(1, n)
	if current == n:
		print(n)
		return
	print(current)
	print_nums_helper(current+1, n)	

def find_char_a(string: str) -> int:
	"""
	Implement a function that returns the number of times the 
	character "a" appears in a str without using a loop. 

	You may only access 
	a single character of the string in any iteration of the 
	function.
	"""
	# if len(string) == 0:
	# 	return 0

	# if string[0] == 'a':
	# 	return 1 + find_char_a(string[1:])
	# else:
	# 	return find_char_a(string[1:])
	return find_char_a_helper(string, 0)

def find_char_a_helper(string: str, index: int) -> int:
	if index == len(string):
		return 0
	if string[index] == 'a':
		result = find_char_a_helper(string, index + 1)
		return 1 + result
	else:
		result = find_char_a_helper(string, index + 1)
	 	return result

def a_to_b(string: str) -> str:
	"""
	Write a recursive function that takes as input a string
	and returns a new string where all instances of the
	character a are replaced with the character b.
	You may access position 0 of the string and you 
	may take a slice of the string
	"""
	pass

def in_english(number: int) -> str:
	"""
	Write a recursive function called in_english that takes a 
	integer value as input and returns a string containing 
	the digits of the number in English. For example, 
	in_english(153) would return "one five three".
	"""
	pass

def binarysearch(list: list[int], target: int) -> bool:
 	"""
 	Write a recursive function that returns True if the target
 	exisits in the list and False otherwise.
 	"""
 	pass

def main():
	print(find_char_a(''))

if __name__ == '__main__':
	main()