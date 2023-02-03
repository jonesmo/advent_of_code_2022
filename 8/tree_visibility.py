import csv
import numpy as np
import pandas as pd
pd.set_option('display.max_colwidth', None)

lr_rows = []
ud_rows = []

with open("./input_data.txt") as file:
    raw_data = csv.reader(file)
    for line in raw_data:
        lr_rows.append(line[0])

for i in range(len(lr_rows)):
    column = ''.join([item[i] for item in lr_rows])
    ud_rows.append(column)

"""
As we go from tree A to tree B along a row in any direction,
if h(B) == h(A) OR h(B) < h(A), then tree B is hidden in that direction.
If h(B) > h(A), then tree B is visible.
NOPE this is wrong because it doesn't take into account the maximum so far
"""

lr_visibility_grid = []
rl_visibility_grid = []
ud_visibility_grid = []
du_visibility_grid = []

# left to right
for lr_row in lr_rows:
    lr_visibility_row = ''
    lr_max_so_far = 0
    for index, height_B in enumerate(lr_row):
        height_A = lr_row[index - 1]
        if index == 0:
            visibility_indicator = '0'
            lr_visibility_row += visibility_indicator
            lr_max_so_far = height_B
        elif index < len(lr_rows) - 1:
            if height_B > lr_max_so_far:
                lr_max_so_far = height_B
                visibility_indicator = '0'
                lr_visibility_row += visibility_indicator
            else:
                visibility_indicator = '1'
                lr_visibility_row += visibility_indicator
        elif index == len(lr_rows) - 1:
            visibility_indicator = '0'
            lr_visibility_row += visibility_indicator
    lr_visibility_grid.append(lr_visibility_row)

# right to left
    rl_row = lr_row[::-1]
    rl_visibility_row = ''
    rl_max_so_far = 0
    for index, height_B in enumerate(rl_row):
        height_A = rl_row[index - 1]
        if index == 0:
            visibility_indicator = '0'
            rl_visibility_row = visibility_indicator + rl_visibility_row
            rl_max_so_far = height_B
        elif index < len(lr_rows) - 1:
            if height_B > rl_max_so_far:
                rl_max_so_far = height_B
                visibility_indicator = '0'
                rl_visibility_row = visibility_indicator + rl_visibility_row
            else:
                visibility_indicator = '1'
                rl_visibility_row = visibility_indicator + rl_visibility_row
        elif index == len(lr_rows) - 1:
            visibility_indicator = '0'
            rl_visibility_row = visibility_indicator + rl_visibility_row
    rl_visibility_grid.append(rl_visibility_row)

# print("lr_visibility_grid", lr_visibility_grid[2])
# print("rl_visibility_grid", rl_visibility_grid[2])

# up to down
for ud_row in ud_rows:
    ud_visibility_row = ''
    ud_max_so_far = 0
    for index, height_B in enumerate(ud_row):
        height_A = ud_row[index - 1]
        if index == 0:
            visibility_indicator = '0'
            ud_visibility_row += visibility_indicator
            ud_max_so_far = height_B
        elif index < len(ud_rows) - 1:
            if height_B > ud_max_so_far:
                ud_max_so_far = height_B
                visibility_indicator = '0'
                ud_visibility_row += visibility_indicator
            else:
                visibility_indicator = '1'
                ud_visibility_row += visibility_indicator
        elif index == len(ud_rows) - 1:
            visibility_indicator = '0'
            ud_visibility_row += visibility_indicator
    ud_visibility_grid.append(ud_visibility_row)

# down to up
    du_row = ud_row[::-1]
    du_visibility_row = ''
    du_max_so_far = 0
    for index, height_B in enumerate(du_row):
        height_A = du_row[index - 1]
        if index == 0:
            visibility_indicator = '0'
            du_visibility_row = visibility_indicator + du_visibility_row
            du_max_so_far = height_B
        elif index < len(lr_rows) - 1:
            if height_B > du_max_so_far:
                du_max_so_far = height_B
                visibility_indicator = '0'
                du_visibility_row = visibility_indicator + du_visibility_row
            else:
                visibility_indicator = '1'
                du_visibility_row = visibility_indicator + du_visibility_row
        elif index == len(lr_rows) - 1:
            visibility_indicator = '0'
            du_visibility_row = visibility_indicator + du_visibility_row
    du_visibility_grid.append(du_visibility_row)

# now take the intersection of the lr and rl bitmaps
lr_intersection_grid = []

for lr_row, rl_row in zip(lr_visibility_grid, rl_visibility_grid):
    intersection_row = ''
    for i in range(len(lr_row)):
        lr_value = lr_row[i]
        rl_value = rl_row[i]
        if lr_value == rl_value:
            intersection_row += lr_value
        else:
            intersection_row += '0'
    lr_intersection_grid.append(intersection_row)

# print("lr_intersecti_grid", lr_intersection_grid[2])

# now take the intersection of the ud and du bitmaps
ud_intersection_grid = []

for ud_row, du_row in zip(ud_visibility_grid, du_visibility_grid):
    intersection_row = ''
    for i in range(len(ud_row)):
        ud_value = ud_row[i]
        du_value = du_row[i]
        if ud_value == du_value:
            intersection_row += ud_value
        else:
            intersection_row += '0'
    ud_intersection_grid.append(intersection_row)

# now take the intersection of the lr_intersection_grid and the ud_intersection_grid
lr_broken_out = []
ud_broken_out = []

for lr_row in lr_intersection_grid:
    lr_list = list(lr_row)
    lr_broken_out.append(lr_list)

for ud_row in ud_intersection_grid:
    ud_list = list(ud_row)
    ud_broken_out.append(ud_list)

lr_array = np.asarray(lr_broken_out, dtype=np.short)
lr_df = pd.DataFrame(lr_array)

ud_array = np.asarray(ud_broken_out, dtype=np.short)
ud_df = pd.DataFrame(ud_array)
ud_df_transposed = ud_df.T

final_intersection_df = pd.DataFrame(columns=lr_df.columns)


def visible_or_not(lr_row, ud_row):
    final_row = []
    for i in range(len(lr_row)):
        if lr_row[i] == ud_row[i]:
            final_row.append(lr_row[i])
        else:
            final_row.append(0)
    return final_row


for colName in lr_df:
    final_intersection_df[colName] = visible_or_not(
        lr_df[colName], ud_df_transposed[colName])

print(final_intersection_df.head())
print("total invisible trees: ", final_intersection_df.values.sum())

total_trees_that_exist = len(lr_rows[0]) * len(lr_rows)
print("total trees that exist: ", total_trees_that_exist)
