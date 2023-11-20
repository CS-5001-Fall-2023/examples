height = 10
width = 20
half_height = height//2
half_width = width//2

[[print(f'{i} - {j}') for j in range(half_height, height)] for i in range(half_width)]


        # # i have no idea why these two needed to be switched
        # upper_right = [[im.getpixel((i, j)) for j in range(half_height, height)] for i in range(half_width)]
        # lower_left = [[im.getpixel((i, j)) for j in range(half_height)] for i in range(half_width, width)]



        # j == 5 - 10
        # i == 0 - 5

        # width, height

   		# 5 0 -- 0 5
   		# 5 1    1 5
   		# 5 2
   		# 5 3
   		# 5 4
   		# 6 0
   		# 6 1
   		# 6 2
