gradebook = {
	'John': [90, 75, 82, 95],
	'Harvey': [89, 89, 87, 72]
}

for name in gradebook.keys():
	print(f'{name} - {gradebook[name]}')

new_scores = [89, 76, 89, 99]
gradebook['Sue'] = new_scores

for name in gradebook.keys():
	print(f'{name} - {gradebook[name]}')

name = 'Harvey'
score = 90

gradebook[name].append(score)

for name in gradebook.keys():
	print(f'{name} - {gradebook[name]}')


# inventory = {}

# inventory['Twix'] = 25
# inventory['Milky Way'] = 30

# print(inventory['Twix'])

# inventory['Kit Kat'] = 15

# for item in inventory.keys():
# 	print(f'{item} - {inventory[item]}')

# inventory['Twix'] = inventory['Twix'] - 5

# print('\n*********\n')
# for item in inventory.keys():
# 	print(f'{item} - {inventory[item]}')


