
ROWS = 9
COLS = 9

board = [
	[2, 7, 3, 5, 9, 4, 8, 6, 1],
	[4, 5, 8, 6, 1, 7, 3, 9, 2],
	[1, 6, 9, 8, 3, 2, 4, 7, 5],
	[9, 8, 6, 4, 2, 1, 7, 5, 3],
	[3, 2, 5, 9, 7, 8, 1, 4, 6],
	[7, 4, 1, 3, 5, 6, 2, 8, 9],
	[8, 1, 2, 7, 6, 5, 9, 3, 4],
	[6, 3, 7, 2, 4, 9, 5, 1, 8],
	[5, 9, 4, 1, 8, 3, 6, 2, 7]
	]

def check_rows():
	for row in board:
		for number in range(1, 10):
			if number not in row:
				return False
	return True

def check_cols():	
	pass

def print_board():
	for row in range(ROWS):
		for col in range(COLS):
			if col % 3 == 0:
				print(f'|{board[row][col]} ', end='')
			else:
				print(f'{board[row][col]} ', end='')
		print()

def main():
	print(check_rows())

if __name__ == '__main__':
	main()