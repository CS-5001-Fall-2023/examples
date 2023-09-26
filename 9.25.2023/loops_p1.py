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

	while user_guess != secret_word and guesses < MAX_GUESSES:		
		user_guess = input('WRONG! Guess again: ')
		guesses += 1

	if user_guess == secret_word: # guesses <= MAX_GUESSES
	# if guesses < MAX_GUESSES:
		print(f'You guessed the secret word: {secret_word} in {guesses} guess(es).')
	else:
		print(f'Sorry...the secret word was {secret_word}.')


def guess_my_number(secret_number: int):
	'''
	Prompt the user to enter an integer until the user's
	number matches the secret number.
	For incorrect guesses, tell the user whether the
	guess was too high or too low.
	'''
	user_guess = int(input('Guess my number: '))
	high_guesses = 0
	low_guesses = 0

	while user_guess != secret_number:
		if user_guess > secret_number:
			print('Your guess is too high.')
			high_guesses += 1
		else: #if user_guess < secret_number:
			print('Your guess is too low.')
			low_guesses += 1
		user_guess = int(input('Sorry...try again: '))	
	
	print(f'Yep, my number was {secret_number}.')
	print(f'You had {high_guesses} that were too high...')
	print(f'...and {low_guesses} that were too lowx.')

def main():
	# print_to_n(5)
	# print_evens(5)
	# guess_my_word('secret')
	guess_my_number(5)

if __name__ == '__main__':
	main()




