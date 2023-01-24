import csv
from collections import defaultdict

terminal_lines = []
dirs = defaultdict(int)
stack = []

with open("./input_data.txt") as file:
    raw_data = csv.reader(file)
    for line in raw_data:
        terminal_lines.append(line[0])

for line in terminal_lines:
    if line.startswith("$ ls") or line.startswith("dir"):
        continue
    if line.startswith("$ cd"):
        destination_dir = line.split()[2]
        # print("destination directory", destination_dir)
        # print("stack", stack)
        if destination_dir == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}_{destination_dir}" if stack else destination_dir
            # print("path", path)
            stack.append(path)
    else:
        size, file = line.split()
        for path in stack:
            dirs[path] += int(size)

# print("all dirs", dirs)
# print("sum under 100K", sum(n for n in dirs.values() if n <= 100000))  # part 1 answer

total_disk_space = 70000000
needed_disk_space = 30000000
free_disk_space = total_disk_space - dirs['/']
minimum_space_to_free = needed_disk_space - free_disk_space

large_enough = dict((k, v)
                    for k, v in dirs.items() if v >= minimum_space_to_free)

large_enough_sorted = {k: v for k, v in sorted(
    large_enough.items(), key=lambda item: item[1])}

print(large_enough_sorted)

# for index, line in enumerate(terminal_lines):
#     # print(line)
#     if line[0:4] == "$ ls" and index <= len(terminal_lines) - 2:
#         dir_being_listed = terminal_lines[index - 1][4:]
#         print("dir being listed", dir_being_listed, "index", index)

#         inside_dir = True
#         current_line = 1
#         while inside_dir == True and index <= len(terminal_lines) - 2 and index + current_line <= len(terminal_lines):
#             content_line = terminal_lines[index + current_line]
#             print(f"content line {index+current_line}: ", content_line)
#             # dir_contents = [s for s in terminal_lines[index + current_line]]
#             # print(dir_contents)

#             # print("index", index + current_line)
#             # file_size_list = [
#             #     int(s) for s in terminal_lines[index + current_line].split() if s.isdigit()]
#             # if len(file_size_list) > 0:
#             #     file_size = file_size_list[0]
#             #     # print("file size", file_size)
#             #     if not dir_being_listed in dirs:
#             #         dirs[dir_being_listed] = file_size
#             #     else:
#             #         dirs[dir_being_listed] += file_size
#             if index + current_line <= len(terminal_lines):
#                 current_line += 1
#             if index + current_line < len(terminal_lines) - 1 and not terminal_lines[index + current_line][0].isdigit():
#                 inside_dir = False
#                 break

# print("single value: ", dirs[' bjrbjh'])

# # print("ALL DIRS", dirs)
# small_enough = {k: v for (k, v) in dirs.items() if v <= 100000}
# # print(small_enough)
# sum_of_values = sum(small_enough.values())
# print(sum_of_values)
