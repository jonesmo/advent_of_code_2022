import csv

signal = ''

with open("./input_data.txt") as file:
    raw_data = csv.reader(file)
    for line in raw_data:
        signal = line[0]

window_size = 14

for index in range(len(signal) - window_size + 1):
    window = signal[index: index + window_size]
    
    if len(set(window)) == window_size:
        print(index + window_size)
        break