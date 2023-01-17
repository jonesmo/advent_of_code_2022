import csv

your_score = 0

move_scoring = {"X": 1, "Y": 2, "Z": 3}
move_transcoding = {"X": "A", "Y": "B", "Z": "C"}

# X = A, Y = B, Z = C
# A defeats C; B defeats A; C defeats B

def calculate_win_score(opponent_move, your_move):
	your_move_transcoded = move_transcoding[your_move]

	if your_move_transcoded == opponent_move:
		return 3

	move_set = [opponent_move, your_move_transcoded]

	if (("A" in move_set) and ("C" in move_set)):
		if move_set[0] == "A":
			return 0
		else:
			return 6

	if (("A" in move_set) and ("B" in move_set)):
		if move_set[0] == "B":
			return 0
		else:
			return 6

	if (("B" in move_set) and ("C" in move_set)):
		if move_set[0] == "C":
			return 0
		else:
			return 6

with open('2/input_data.txt') as file:
	raw_data = csv.reader(file)

	for line in raw_data:
			strategy = line[0]
			opponent_move = strategy[0]
			your_move = strategy[2]

			win_loss_score = calculate_win_score(opponent_move, your_move)

			score_for_round = move_scoring[your_move] + win_loss_score

			your_score = your_score + score_for_round

print("Your final score: ", your_score)