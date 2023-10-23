
def is_palindrome(string: str) -> bool:
	start = 0
	end = len(string) - 1

	while start < end:
		# if item at pos start == item at pos end
		if string[start] == string[end]:
			start += 1
			end -= 1
			#continue
		else:
			return False
	return True

def is_palindrome_rec(string:str) -> bool:
	if len(string) == 0 or len(string) == 1:
		return True
	if string[0] == string[-1]:
		return is_palindrome_rec(string[1:len(string)-1])
	return False

def last_length(phrase: str) -> int:
	# 'the quick brown dog' -> 3
	# 'exam on wednesday' -> 9
	# string methods: split

	# split the phrase -- list of strings
	# find the last item in the list 
	# take the length
	# result = phrase.split()
	# return len(result[-1])
	count = 0
	# i = len(phrase) - 1	
	# while i >= 0:
	for i in range(len(phrase)-1, -1, -1):
		char = phrase[i]
		if char == ' ':
			break
		count += 1
		i -= 1
	return count


def main():
	print(last_length('the quick brown dog'))
	print(last_length('exam on wednesday'))

	# print(is_palindrome_rec('maam'))
	# print(is_palindrome_rec('cat'))
	# print(is_palindrome_rec(''))
	# print(is_palindrome_rec('racecar'))

if __name__ == '__main__':
	main()
