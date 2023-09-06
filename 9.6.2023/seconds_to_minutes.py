"""
A program to prompt a user to enter a number of seconds and 
covert that to minutes.

# https://docs.python.org/3/tutorial/inputoutput.html

"""

def main():
	# ask the user for the number
	#    - store the number
	seconds = int(input('Enter a number of seconds: '))
	
	# print('You entered',seconds,'seconds.')
	print(f'You entered {seconds} seconds.')
	# print(type(seconds))

	# math operators: + - * / % //
	# perform the calculation from s to m
	minutes = seconds / 60

	# output the result
	print(f'{seconds} seconds is {minutes} minutes')


if __name__ == '__main__':
	main()	