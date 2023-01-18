import csv

with open('./input_data.txt') as file:
	raw_data = csv.reader(file)

	overlapping_pair_count = 0

	for line in raw_data:
		elf_1_assignment = line[0]
		elf_2_assignment = line[1]

		elf_1_lower_bound, elf_1_upper_bound = list(map(int, elf_1_assignment.split("-")))
		elf_2_lower_bound, elf_2_upper_bound = list(map(int, elf_2_assignment.split("-")))

		if ((elf_1_lower_bound <= elf_2_lower_bound and elf_1_upper_bound >= elf_2_upper_bound) or (elf_2_lower_bound <= elf_1_lower_bound and elf_2_upper_bound >= elf_1_upper_bound)):
			overlapping_pair_count += 1

	print(overlapping_pair_count)