def iterate_row(row_list):
    sequences = [row_list]
    current_level = row_list
    while any(current_level):
        current_level = [y - x for x,y in zip(current_level,current_level[1:])]
        sequences.append(current_level)

    for idx,sequence in enumerate(sequences[::-1][1:]):
        sequence.append(sequences[::-1][idx][-1] + sequences[::-1][idx+1][-1])
    return sequences[0][-1]


with open ('day9_input.txt','r') as input:
    input_array = [[int(num) for num in row.split()] for row in input]
    
    #Q1
    total_sum = 0
    for row in input_array:
        total_sum += iterate_row(row)
    print(total_sum)

    #Q2
    q2_total_sum = 0
    for row in input_array:
        q2_total_sum += iterate_row(row[::-1])
    print(q2_total_sum)
