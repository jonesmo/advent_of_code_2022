import string

lowercase_letters = string.ascii_lowercase[:26]
uppercase_letters = string.ascii_uppercase[:26]
letters = lowercase_letters + uppercase_letters

priority_map = {}
for index, letter in enumerate(letters):
	priority = index + 1
	priority_map[letter] = priority

print(priority_map)