from stack import Stack

def check_parens(expression):
	stack = Stack(25)
	for char in expression:
		stack.push(char)

	while stack.size() > 0:
		top_char = stack.pop()
		print(top_char, end='')	

def main():
	expression = '{[]{()}}'
	check_parens(expression)

if __name__ == '__main__':
	main()