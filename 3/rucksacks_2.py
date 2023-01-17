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
	data_list = []
	for line in raw_data:
		data_list.append(line[0])

	elf_groups_list = [data_list[i:i+3] for i in range(0,len(data_list),3)]

	# find the shared item in each elf group
	for elf_group in elf_groups_list:
		shared = list(set(elf_group[0]).intersection(*elf_group))[0]

		# look it up in the priority_map
		shared_item_priority = priority_map[shared]

		# add the priority to a running sum
		priority_sum += shared_item_priority

print("priority final sum: ", priority_sum)