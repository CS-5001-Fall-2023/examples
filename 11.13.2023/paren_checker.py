from stack import Stack
# from: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/#

'''
Given an expression string, write a python program to find whether a given string has balanced parentheses or not.

Examples:

Input : {[]{()}}
Output : Balanced

Input : [{}{}(]
Output : Unbalanced
'''

open_chars = ['(', '{', '[']
close_chars = [')', '}', ']']

def is_open(char):
	return char in open_chars

def is_close(char):
	return char in close_chars

def match(open_char, close_char):
	if open_char not in open_chars or close_char not in close_chars:
		return False
		
	if open_chars.index(open_char) == close_chars.index(close_char):
		return True
	return False

	# if open_char == '(' and close_char == ')':
	# 	return True
	# if open_char == '{' and close_char == '}':
	# 	return True
	# if open_char == '[' and close_char == ']':
	# 	return True
	# return False

def check(paren_string):
	parens = Stack(10)

	for char in paren_string:	
		if is_open(char):
			parens.push(char)
		elif is_close(char):
			if parens.size() == 0:
				return False
			open_char = parens.pop()
			if not match(open_char, char):
				return False				
	if parens.size() > 0:
		return False
	return True

def main():
	expression = '{[]{()}}'
	print(check(expression))

	expression = '[{}{}(]'
	print(check(expression))

if __name__ == '__main__':
	main()

