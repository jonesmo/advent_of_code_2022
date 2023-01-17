import string
import csv

lowercase_letters = string.ascii_lowercase[:26]
uppercase_letters = string.ascii_uppercase[:26]
letters = lowercase_letters + uppercase_letters

priority_map = {}
for index, letter in enumerate(letters):
	priority = index + 1
	priority_map[letter] = priority

priority_sum = 0

with open('./input_data.txt') as file:
	raw_data = csv.reader(file)

	for line in raw_data:
		# divide each line in half
		line_half_length = int(len(line[0]) / 2)
		first_half = line[0][0:line_half_length]
		second_half = line[0][line_half_length:]

		# find the shared item between the two halves
		shared = list(set(first_half).intersection(second_half))[0]

		# look it up in the priority_map
		shared_item_priority = priority_map[shared]

		# add the priority to a running sum
		priority_sum += shared_item_priority

print("priority final sum: ", priority_sum)