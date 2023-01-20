import csv

moves = []
with open("./input_data.txt") as file:
    raw_data = csv.reader(file)

    for line in raw_data:
        move_nums = [int(s) for s in line[0].split() if s.isdigit()]
        moves.append(move_nums)

stacks = {
    "1": ["D", "M", "S", "Z", "R", "F", "W", "N"],
    "2": ["W", "P", "Q", "G", "S"],
    "3": ["W", "R", "V", "Q", "F", "N", "J", "C"],
    "4": ["F", "Z", "P", "C", "G", "D", "L"],
    "5": ["T", "P", "S"],
    "6": ["H", "D", "F", "W", "R", "L"],
    "7": ["Z", "N", "D", "C"],
    "8": ["W", "N", "R", "F", "V", "S", "J", "Q"],
    "9": ["R", "M", "S", "G", "Z", "W", "V"],
}

for move_set in moves:
    from_stack = move_set[1]
    to_stack = move_set[2]
    num_to_move = move_set[0]

    crates_to_move = stacks[str(from_stack)][-num_to_move:]
    # enable reverse of crates if we're using the CrateMover 9000 instead of the 9001
    # crates_to_move.reverse()

    stacks[str(from_stack)] = stacks[str(from_stack)][
        : len(stacks[str(from_stack)]) - num_to_move
    ]

    stacks[str(to_stack)].extend(crates_to_move)

final_top_crates = []

for key, stack in stacks.items():
    print("key", key)
    print("stack", stack)

    final_top_crates.extend(stack[-1])

print("final top crates: ", "".join(final_top_crates))