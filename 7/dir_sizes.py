import csv
import re

terminal_lines = []
dirs = {}

with open("./input_data.txt") as file:
    raw_data = csv.reader(file)
    for line in raw_data:
        terminal_lines.append(line[0])

for index, line in enumerate(terminal_lines):
    # print(line)
    if line[0:4] == "$ ls" and index <= len(terminal_lines) - 2:
        dir_being_listed = terminal_lines[index - 1][4:]
        print("dir being listed", dir_being_listed, "index", index)

        inside_dir = True
        current_line = 1
        while inside_dir == True and index <= len(terminal_lines) - 2 and index + current_line <= len(terminal_lines):
            content_line = terminal_lines[index + current_line]
            print(f"content line {index+current_line}: ", content_line)
            # dir_contents = [s for s in terminal_lines[index + current_line]]
            # print(dir_contents)

            # print("index", index + current_line)
            # file_size_list = [
            #     int(s) for s in terminal_lines[index + current_line].split() if s.isdigit()]
            # if len(file_size_list) > 0:
            #     file_size = file_size_list[0]
            #     # print("file size", file_size)
            #     if not dir_being_listed in dirs:
            #         dirs[dir_being_listed] = file_size
            #     else:
            #         dirs[dir_being_listed] += file_size
            if index + current_line <= len(terminal_lines):
                current_line += 1
            if index + current_line < len(terminal_lines) - 1 and not terminal_lines[index + current_line][0].isdigit():
                inside_dir = False
                break

    # print("single value: ", dirs[' bjrbjh'])

    # # print("ALL DIRS", dirs)
    # small_enough = {k: v for (k, v) in dirs.items() if v <= 100000}
    # # print(small_enough)
    # sum_of_values = sum(small_enough.values())
    # print(sum_of_values)
