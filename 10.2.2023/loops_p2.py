'''
Practice with for loops!
'''
VOWELS = ('a', 'e', 'i', 'o', 'u')

def fun_with_for_loops():
	# Remember to call this function :)
	list = ["hello", "there", "cs", "5001", "class"]
	# i = 0
	# while i < len(list):
	# 	item = list[i]		
	# 	print(f'{i} {item}')
	# 	i += 1

	# 15
	# 0 5 10 15

	# Iterating over a list is easier with a for loop!
	# string = 'hello class'
	# for item in list:
	# 	print(item)

	# Accessing the index using range()
	# for i in range(1, len(list), 2):
	# 	item = list[i]
	# 	print(f'{i} {item}')

	# Accessing the index using enumerate
	# for value in enumerate(list):
	# 	print(value)	
	# for i, item in enumerate(list):
	# 	print(f'{i} --- {item}')	

	# Using zip to iterate over two lists at once
	first_names = ['joe', 'jane', 'julio']
	last_names = ['berket', 'saberi', 'vega']

	for first, last in zip(first_names, last_names):
		print(f'First: {first} Last: {last}')


def multiples_of_5(number: int):
	'''
	A function that takes as input a positive integer and
	uses a for loop to print the multiples of 5 that are 
	less than or equal to the number that was entered.
	'''
	for i in range(0, number+1, 5):
		# if i % 5 == 0:
		# 	print(i)
		print(i)


def generate_user_names(first_names: list[str], 
	last_names: list[str]) -> list[str]:
	'''
	A function that takes as input a list of strings
	representing first names and a list of strings representing
	last names and returns a list of usernames where the ith username
	is the first initial of the first name stored at the ith position
	of the first_names list concatenated with the first 7 characters 
	of the last name stored at the ith position of the last_names
	list.
	'''
	usernames = []
	for first, last in zip(first_names, last_names):
		# usernames.append(first[0] + last[:7])

		# get first char of first name
		first_initial = first[0]
		
		# get first 7 characters of last name
		last_part = last[:7]

		# append together to create username
		username = first_initial + last_part

		# add username to list
		usernames.append(username)

	return usernames

def nested_loops():
	board = [
				['x', '-', 'x'], 
				['o', '-', '-'],
				['-', '-', '-']
			]

	for row in board:
		# list that represents a row
		for col in row:
			print(col, end=' ')
		print()

def gradebook():
	grades  = [
				[95, 99, 82],
				[90.5, 92, 84],
				[85, 79, 82],
				]

	# student 1: XXX
	# student 2: YYY
	# student 3: ZZZ
	for student_id, student in enumerate(grades):
		sum = 0
		for grade in student:
			sum += grade
		avg = sum / len(student)
		print(f'student {student_id+1}: {avg}')


def is_vowel(char: str) -> bool:	
	return char in VOWELS

	# if (char == 'a' 
	# 	or char == 'e'
	# 	or char == 'i'
	# 	or char == 'o'
	# 	or char == 'u'):
	# 	return True
	# return False

def count_vowels(sentence: str) -> int:
	'''
	A function that takes as input a string and returns the number
	of vowels (a, e, i, o, u) that are found in the sentence.
	'''
	count = 0
	lower_case_sentence = sentence.lower()
	for char in lower_case_sentence:
		if is_vowel(char):
			count += 1			
	return count

def main():

	gradebook()

	# nested_loops()

	# first_names = ['joe', 'jane', 'sally']
	# last_names = ['ortega', 'saberi', 'berketrollins']
	# # [jortega, jsaberi, sberketr]
	# print(generate_user_names(first_names, last_names))



	# result = count_vowels('hello')
	# print(f'result: {result} expected result: 2')

	# result = count_vowels('hello hello')
	# print(f'result: {result} expected result: 4')

	# result = count_vowels('hEllo hellO')
	# print(f'result: {result} expected result: 4')


if __name__ == '__main__':
	main()

