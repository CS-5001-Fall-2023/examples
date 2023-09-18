
'''
Write a program (remember that programs have a main() function) to print the lyrics of the song "Old MacDonald." Your program should print the lyrics for five different animals (five verses), similar to the example verse below:
'''

# Old MacDonald had a farm, ee-igh, ee-igh, oh!
# And on that farm he had a cow, ee-igh, ee-igh, oh!
# With a moo, moo here and a moo, moo there.
# Here a moo, there a moo, everywhere a moo, moo.
# Old MacDonald had a farm, ee-igh, ee-igh, oh!

# TODO: discuss the string split function

def print_verse(animal: str, sound: str):
	print(f'Old MacDonald had a farm, ee-igh, ee-igh, oh!')
	print(f'And on that farm he had a {animal}, ee-igh, ee-igh, oh!')
	print(f'With a {sound}, {sound} here and a {sound}, {sound} there.')
	print(f'Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.')
	print(f'Old MacDonald had a farm, ee-igh, ee-igh, oh!')

def get_verse(animal: str, sound: str) -> str:
	result = ''
	result += f'Old MacDonald had a farm, ee-igh, ee-igh, oh!\n'
	result += f'And on that farm he had a {animal}, ee-igh, ee-igh, oh!\n'
	result += f'With a {sound}, {sound} here and a {sound}, {sound} there.\n'
	result += f'Here a {sound}, there a {sound}, everywhere a {sound}, {sound}.\n'
	result += f'Old MacDonald had a farm, ee-igh, ee-igh, oh!\n'
	return result

def get_animal_and_sound():
	user_input = input('Give me your animal and sound: ')
	# user_input = 'cow moo'
	animal, sound = user_input.split()
	return animal, sound

def main():
	# call the function to sing one verse
	# print_verse('cow', 'moo')
	# print_verse('pig', 'oink')
	# print_verse('duck', 'quack')
	animal, sound = get_animal_and_sound()
	verse = get_verse(animal, sound)
	print(verse)

	# verse = get_verse('pig', 'oink')
	# print(verse)

	# value = 'a bb ccc ddd'
	# a_chars, b_chars, c_chars, d_chars = value.split()
	# print(c_chars)


if __name__ == '__main__':
	main()
