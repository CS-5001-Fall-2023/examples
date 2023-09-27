'''
Practice with strings!
'''

def fun_with_strings():
	'''
	What can you do with a string?!
	https://docs.python.org/3/library/stdtypes.html#string-methods
	'''
	# Strings are immutable!
	# Accessing individual characters
	# Calling string methods -- like replace!
	# Slicing strings
	name = 'karlo berket'
	# first, last = name.split()
	# print(first)
	# print(last)
	# # user_name = first[-1] + '.' + last
	# user_name = first[len(first)-1] + '.' + last
	# print(user_name)

	sliced = name[0:9:2]
	print(sliced)

	# print(name[5])
	# if name.endswith('ket'):
	# 	print(name)
	# 	print('your string ends with ket')
	# else:
	# 	print('bad ending')
	# result = name.find('ket')
	# print(result)


def reverse(phrase: str) -> str:
	'''
	A function to reverse the string passed as input.
	'''
	return phrase[::-1]

def is_palindrome(word: str) -> bool:
	'''
	A palindrome is a word that is the same forward
	and backward. Examples are madam, racecar, and deed.
	This function takes as input a word and returns True
	if the word is a palindrome and False otherwise.
	You may assume that the string does not contain spaces.
	Consider two different approaches to implementing 
	this function.
	'''
	return word == reverse(word)

	# if word == reverse(word):
	# 	return True
	# else:
	# 	return False

	# first_index = 0
	# last_index = len(word) - 1 
	# while first_index < last_index:
	# 	if word[first_index] == word[last_index]:
	# 		first_index += 1
	# 		last_index -= 1
	# 	else:
	# 		return False
	# return True




def main():
	# fun_with_strings()
	result = is_palindrome('died')
	print(f'result: {result}')

	# result = reverse('class')
	# print(f'result: {result}')


if __name__ == '__main__':
	main()

