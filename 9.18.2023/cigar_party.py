'''
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
'''

def cigar_party(cigars: int, is_weekend: bool) -> bool:
	# partial solution for cigar_party problem
	# if is_weekend == True and cigars >= 40:
	# 	return True
	# elif is_weekend == True and cigars < 40:
	# 	return False
	if cigars < 40:
		# print('cigars < 40 -- returning False')
		return False
	else:
		# print('cigars >= 40 -- checking is_weekend')
		if is_weekend == True:
			# print('is_weekend is True -- returning True')
			return True
		else:
			# print('is_weekend is False -- checking cigars again')
			if cigars <= 60:
				# print('cigars <= 60 -- returning True')
				return True
			else: 
				# print('cigars not <= 60 -- returning False')
				return False

def main():
	
	result = cigar_party(70, True)
	print(f'cigar_party(70, True) is {result}')

	result = cigar_party(70, False)
	print(f'cigar_party(70, False) is {result}')

	result = cigar_party(30, True)
	print(f'cigar_party(30, True) is {result}')

	result = cigar_party(30, False)
	print(f'cigar_party(30, False) is {result}')

	result = cigar_party(50, True)
	print(f'cigar_party(50, True) is {result}')

	result = cigar_party(50, False)
	print(f'cigar_party(50, False) is {result}')


 	# How many tests do we need to do
	# to ensure that our function
	# is correct?

	'''
	70, True -> True
	70, False -> False
	30, True/False -> False
	50, False -> True
	50, True -> True	
	'''

if __name__ == '__main__':
	main()