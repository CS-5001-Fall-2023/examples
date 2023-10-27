
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

def merge_sorted_lists(list1: list, list2: list) -> list:
	result = []

	# append to result
	list1_index = 0
	list2_index = 0

	while list1_index < len(list1) and list2_index < len(list2):
		if list1[list1_index] <= list2[list2_index]:
			result.append(list1[list1_index])
			list1_index += 1
		else:
			result.append(list2[list2_index])
			list2_index += 1

	# if we aren't at the end of list1, add the rest
	while list1_index < len(list1):
		result.append(list1[list1_index])
		list1_index += 1

	# if we aren't at the end of list2, add the rest
	while list2_index < len(list2):
		result.append(list2[list2_index])
		list2_index += 1

	return result

def valid_phone(string: str) -> bool:
	# (415)555-1212 -> True
	# (718)3334567 -> False
	# 123-456-7896 -> False
	# 1234567892 -> False
	# (aaa)bbb-cccc -> False
	# (9ab)12334r5 -> False

	# length must be 13
	# string[0] == '('
	# string[4] == ')'
	# string[8] == '-'
	# area_code = string[1:4]
	# prefix = string[5:8]
	# extension = string[9:]

	# make sure area_code, prefix, and extension are numbers
	# -- use isdigit method of string
	# -- create a list of all digits and iterate over to confirm in list
	# -- try to convert each to int (int(area_code))



def main():
	print(merge_sorted_lists([1, 3, 4, 5, 7, 12], [2, 6, 9, 12, 14]))


	# print(is_palindrome_rec('maam'))
	# print(is_palindrome_rec('cat'))
	# print(is_palindrome_rec(''))
	# print(is_palindrome_rec('racecar'))

if __name__ == '__main__':
	main()
