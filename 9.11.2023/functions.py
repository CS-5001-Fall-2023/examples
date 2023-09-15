'''
A python program to demonstrate how to use functions.
'''

def welcome():
	'''
	Exercise 1: 
	A function to print a multi-line welcome message.
	You can print this documentation using 
	print(welcome.__doc__)
	'''
	print(f'Hello class!')
	print(f'Welcome to CS 5001.')

def greet_by_name(name: str):
	'''
	Exercise 2:
	A function to greet a user by name.
	Parameters
	name: str
		name of the user
	'''
	# first draft:
	# print(f'Hello, {name}')
	# print(f'How are you today?')

	# an example of a function calling other functions
	greeting = get_greeting()
	welcome_by_name_with_greeting(name, greeting)


def get_greeting() -> str:
	'''
	Exercise 3:
	A function to get a specific greeting from the user.
	Returns:
	str 
		greeting provided by the user
	'''
	user_input = input('Enter a greeting: ')
	return user_input

def welcome_by_name_with_greeting(name: str, greeting: str):
	'''
	Exercise 4:
	A function to welcome a user by name with a 
	specific greeting.
	Parameters:
	name: str
		name of the user
	greeting: str
		greeting to use
	'''

	print(f'{greeting} {name}. How are you?')
	print(f'I would like to welcome you (by name with greeting).')

def main():
	# welcome_by_name_with_greeting('sami', 'hello')
	greet_by_name('sami')


if __name__ == '__main__':
	main()