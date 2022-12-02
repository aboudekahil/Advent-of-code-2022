calories = [0]

with open('./Day01/input.txt', 'r') as file:
	inputtedTxt = file.read().splitlines()

for i in inputtedTxt:
	if(i == ''):
		calories.append(0)
		continue

	calories[-1] += int(i)

calories.sort(reverse=True)

# # max calories
# print(calories[0])

# sum of biggest 3
print(sum(calories[:3]))
