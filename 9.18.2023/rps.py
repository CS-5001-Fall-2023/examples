'''
Write a Python program that uses functions to play the game rock, paper, scissors. Play will proceed as follows:

A random number will be selected to represent the computer choice. A 1 will be "rock"; a 2 will be "paper"; and a 3 will be "scissors".

The user will be prompted to enter a choice of rock, paper, or scissors.
If the user choice is valid the computer choice and user choice will be compared and a winner will be declared.
- paper beats rock 
- rock beats scissors
- scissors beats paper

If the user choice is not valid then play will end.

Hints:

- Grading will primarily depend upon how you decompose your program into functions. - Consider the steps listed above as you think about which functions to implement.
- You must validate the user input to confirm that it is either rock, paper, or scissors. 
'''

# get the user's choice -- expect rock, paper, or scissors
#   * name -- user_choice
#	* inputs (parameters) -- none?
#	* output (return value) -- string (or int?)
#	* logic

# get the computer's choice -- choose random number
# compare -- determine winner
# show the result




import random

def main():
	value = random.randint(1, 3)
	print(value)

if __name__ == '__main__':
	main()












