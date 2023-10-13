# See: https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/os.html

def convert(value, target_type):
	"""
	Write a function to convert value into the target type. 
	Valid type for target_type is int or float.
	If the value is already the target_type
		return the value without conversion
	If the target_type is not int or float
		generate a TypeError
	If the value cannot be converted
		return a ValueError
	"""
	pass


def read_file(filename: str):
	"""
	Write a function to display the contents of a file.
	The function will throw an exception if the file is
	not found.
	"""
	pass

def search_replace(search:str, 
	replace:str, 
	infilename:str, 
	outfilename:str):
	"""
	Write a function that will replace all instances of a search
	term in a given file with a replace term. The result will be 
	saved to a new file.
	
	Parameters:
	search : str
		the string to replace
	replace : str
		the replacement string
	infilename : str
		the name of the original file
	outfilename : str
		the name of the file where the result will be saved
	"""
	pass
