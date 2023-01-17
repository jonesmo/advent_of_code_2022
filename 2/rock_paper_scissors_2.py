import csv

your_score = 0
your_move = None

win_loss_scoring = {"X": 0, "Y": 3, "Z": 6}
move_scoring = {"A": 1, "B": 2, "C": 3}
win_reference = {"A": {"loser": "C", "defeater": "B"}, "B": {"loser": "A", "defeater": "C"}, "C": {"loser": "B", "defeater": "A"}}

# A = 1; B = 2; C = 3
# A defeats C; B defeats A; C defeats B

def calculate_move_score(opponent_move, your_win_loss_status):
	if your_win_loss_status == "Y":
		your_move = opponent_move
		return move_scoring[your_move]

	# if your strategy is to lose
	if your_win_loss_status == "X":
		your_move = win_reference[opponent_move]["loser"]
		return move_scoring[your_move]

	# if your strategy is to win
	if your_win_loss_status == "Z":
		your_move = win_reference[opponent_move]["defeater"]
		return move_scoring[your_move]

with open('2/input_data.txt') as file:
	raw_data = csv.reader(file)

	for line in raw_data:
			strategy = line[0]
			opponent_move = strategy[0]
			your_win_loss_status = strategy[2]

			move_score = calculate_move_score(opponent_move, your_win_loss_status)

			score_for_round = win_loss_scoring[your_win_loss_status] + move_score

			your_score = your_score + score_for_round

print("Your final score: ", your_score)