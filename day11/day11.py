import math
from itertools import combinations

with open('day11_input.txt','r') as input:
    input_array = [[char for char in row.replace('\n','')] for row in input]

    #expand rows
    new_row = ['!'] * len(input_array[0])
    for row_id,row in enumerate(input_array):
        if set(row) == {'.'}:
            input_array.insert(row_id+1,new_row)
    input_array = [['.' if x == '!' else x for x in row] for row in input_array]

    # expand columns
    for column_id,char in enumerate(input_array[0]):
        if set([row[column_id] for row in input_array]) == {'.'}:
            for row in input_array:
                row.insert(column_id+1,'!')
    input_array = [['.' if x == '!' else x for x in row] for row in input_array]
    
    galaxy_coordinates = []
    for row_id,row in enumerate(input_array):
        for column_id,column in enumerate(row):
            if column == '#':
                galaxy_coordinates.append((column_id,row_id))
    
    all_combo = combinations(galaxy_coordinates,2)
    total_length = 0
    for x,y in all_combo:
        total_length += abs(x[0]-y[0]) + abs(x[1]-y[1])

    print(total_length)

# Q2 wrong answer - answer too low
# with open('day11_input.txt','r') as input:
#     input_array = [[char for char in row.replace('\n','')] for row in input]

#     #expand rows
#     new_row = ['!'] * len(input_array[0])
#     for row_id,row in enumerate(input_array):
#         if set(row) == {'.'}:
#             print(row_id)
#             for i in range(1_000_000-1):
#                 input_array.insert(row_id+i+1,new_row)
#     input_array = [['.' if x == '!' else x for x in row] for row in input_array]

#     # expand columns
#     for column_id,char in enumerate(input_array[0]):
#         if set([row[column_id] for row in input_array]) == {'.'}:
#             print(row[column_id])
#             for row in input_array:
#                 row.insert(column_id+1,'!')
#     input_array = [['.' if x == '!' else x for x in row] for row in input_array]
    
#     galaxy_coordinates = []
#     for row_id,row in enumerate(input_array):
#         for column_id,column in enumerate(row):
#             if column == '#':
#                 galaxy_coordinates.append((column_id,row_id))
    
#     all_combo = combinations(galaxy_coordinates,2)
#     total_length = 0
#     for x,y in all_combo:
#         total_length += abs(x[0]-y[0]) + abs(x[1]-y[1])

#     print(total_length)

