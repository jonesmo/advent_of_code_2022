import csv

list_of_sums = []

with open('1.1/input_data.txt') as file:
	single_list = []
	raw_data = csv.reader(file)

	for line in raw_data:
			if len(line) != 0:
				single_list.append(int(line[0]))
			if len(line) == 0:
				# print(single_list)
				list_of_sums.append(sum(single_list))
				single_list = []

# print("FINAL LIST OF SUMS: ", list_of_sums)
print("MAX CALORIES: ", max(list_of_sums))

list_of_sums.sort(reverse=True)
top_three = list_of_sums[:3]
print("TOP THREE SUM: ", sum(top_three))