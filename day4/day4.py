with open('day4_input.txt') as input:
    input_array = [row.replace('\n','') for row in input]
    total_points = 0
    number_of_rows = len(input_array)

    #Q1
    for row in input_array:
        len_winning_numbers = 0
        winner = [x for x in row.split('|')[0].split(':')[-1].split(' ') if x]
        card = [x for x in row.split('|')[-1].split(' ') if x]

        for num in card:
            if num in winner:
                len_winning_numbers += 1
        if len_winning_numbers > 0:
            total_points += 2**(len_winning_numbers-1)
    
    print(total_points)

    #Q2
    total_dict = {}
    win = []
    for row_id,row in enumerate(input_array):
        if row_id not in total_dict:
            total_dict[row_id] = 1 #include original
    
    for row_id,row in enumerate(input_array):
        len_winning_numbers = 0
        winner = [x for x in row.split('|')[0].split(':')[-1].split(' ') if x]
        card = [x for x in row.split('|')[-1].split(' ') if x]
        for num in card:
            if num in winner:                
                len_winning_numbers += 1
        
        win.append(len_winning_numbers)
        
    for i,wins in enumerate(win):
        for j in range(wins):
            try:
                total_dict[i+j+1] += total_dict[i]
            except:
                pass #to deal with key error lol
    print(sum(list(total_dict.values())))