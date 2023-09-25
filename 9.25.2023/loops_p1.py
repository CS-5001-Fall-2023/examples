'''
Practice with iteration and while loops!
'''

def print_to_n(n: int):
	'''
	Print all numbers from 1 to n inclusive.
	'''
	current_number = 1 # initialization of control variable
	
	while current_number <= n:
		print(current_number)
		current_number += 1 # update control variable


def print_evens(n: int):
	'''
	Print all even numbers from 1 to n inclusive.
	You should be able to implement this using 
	two different approaches!
	'''
	current_number = 2 # initialization of control variable
	
	while current_number <= n:
		print(current_number)
		current_number += 2 # update control variable


	# current_number = 1 # initialization of control variable
	
	# while current_number <= n:
	# 	if current_number % 2 == 0:
	# 		print(current_number)
	# 	current_number += 1 # update control variable

def guess_my_word(secret_word: str):
	'''
	Prompt the user to enter a word until the user's
	word matches the secret word.
	Modification: count the number of guesses.
	Modification: give the user a maximum number of
	tries.
	'''
	MAX_GUESSES = 5
	user_guess = input('Guess a word: ')
	guesses = 1

	while user_guess != secret_word:		
		user_guess = input('WRONG! Guess again: ')
		guesses += 1

	print(f'You guessed the secret word: {secret_word} in {guesses} guess(es).')


def guess_my_number(secret_number: int):
	'''
	Prompt the user to enter an integer until the user's
	number matches the secret number.
	For incorrect guesses, tell the user whether the
	guess was too high or too low.
	'''
	pass

def main():
	# print_to_n(5)
	# print_evens(5)
	guess_my_word('secret')

if __name__ == '__main__':
	main()




