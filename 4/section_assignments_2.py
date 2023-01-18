import csv

with open('./input_data.txt') as file:
	raw_data = csv.reader(file)

	overlapping_pair_count = 0

	for line in raw_data:
		elf_1_assignment = line[0]
		elf_2_assignment = line[1]

		elf_1_range = list(range(int(elf_1_assignment.split("-")[0]), int(elf_1_assignment.split("-")[1]) + 1))
		elf_2_range = list(range(int(elf_2_assignment.split("-")[0]), int(elf_2_assignment.split("-")[1]) + 1))

		if not set(elf_1_range).isdisjoint(elf_2_range):
			overlapping_pair_count += 1

	print(overlapping_pair_count)