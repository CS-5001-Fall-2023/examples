'''
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
'''

def cigar_party(cigars: int, is_weekend: bool) -> bool:
	# partial solution for cigar_party problem
	if is_weekend == True and cigars >= 40:
		return True
	elif is_weekend == True and cigars < 40:
		return False

def main():
	
	result = cigar_party(70, True)
	print(f'cigar_party(70, True) is {result}')

	result = cigar_party(30, True)
	print(f'cigar_party(30, True) is {result}')

 	# How many tests do we need to do
	# to ensure that our function
	# is correct?

	'''
	70, True -> True
	70, False -> False
	30, True/False -> False
	50, False -> True	
	'''

if __name__ == '__main__':
	main()