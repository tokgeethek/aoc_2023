import math

def check_for_symbol(symbols_list,map,current_row_id,current_index):
    all_directions = []
    try:
        all_directions.append(map[current_row_id-1][current_index-1]) #above_left
        all_directions.append(map[current_row_id-1][current_index]) #above
        all_directions.append(map[current_row_id-1][current_index+1]) #above_right
        all_directions.append(map[current_row_id+1][current_index-1]) #below_left
        all_directions.append(map[current_row_id+1][current_index]) #below
        all_directions.append(map[current_row_id+1][current_index+1]) #below_right
        all_directions.append(map[current_row_id][current_index-1]) #left
        all_directions.append(map[current_row_id][current_index+1]) #right
    except:
        pass

    symbol_detected = 0
    for dir in all_directions:
        try:
            if dir != '.' and dir in symbols_list:
                symbol_detected = 1
        except:
            pass
    
    return symbol_detected

def check_gear_position(map,current_row_id,current_index):
    all_directions = {}

    coordinates = {
        'above_left': [-1,-1],
        'above': [-1,0],
        'above_right': [-1,1],
        'below_left': [1,-1],
        'below': [1,0],
        'below_right': [1,1],
        'left': [0,-1],
        'right': [0,1],
    }

    try:
        all_directions['above_left'] = (map[current_row_id-1][current_index-1]) #above_left
        all_directions['above'] = (map[current_row_id-1][current_index]) #above
        all_directions['above_right'] = (map[current_row_id-1][current_index+1]) #above_right
        all_directions['below_left'] = (map[current_row_id+1][current_index-1]) #below_left
        all_directions['below'] = (map[current_row_id+1][current_index]) #below
        all_directions['below_right'] = (map[current_row_id+1][current_index+1]) #below_right
        all_directions['left'] = (map[current_row_id][current_index-1]) #left
        all_directions['right'] = (map[current_row_id][current_index+1]) #right
    except:
        pass
    
    gear_position = (0,0) # (row_id,char_id)
    for dir in all_directions:
        try:
            if all_directions[dir] == '*':
                gear_position = (current_row_id+coordinates[dir][0],current_index+coordinates[dir][1])
        except:
            pass
    
    return gear_position

def calculate_distance(tuple1, tuple2):
    return math.sqrt((tuple1[0] - tuple2[0]) ** 2 + (tuple1[1] - tuple2[1]) ** 2)

def find_closest_tuple(target, tuple_list):
    return min(tuple_list, key=lambda x: calculate_distance(target, x))

def nearest_gear(gear_dict,len_tmp,current_row_id,current_index):
    tuple_list = [gear for gear in gear_dict]
    tmp = []
    distance = []
    for i in range(len_tmp):
        tup = (current_row_id,current_index-(i-1))
        tmp.append(tup)
    #find the nearest gear after comparing all indexes

    return min(distance)

with open('day3_input.txt') as input:
    input_array = [row.replace('\n','') for row in input]
    symbols = '-@*=%/$#+&'
    map = []
    q1_sum = []

    for row in input_array:
        row_array = []
        for char in row:
            row_array.append(char)
        map.append(row_array)

    #Q1
    for row_id,row in enumerate(map):
        tmp = []
        tmp_symbol = []
        for char_id,char in enumerate(row):
            if char not in "0123456789":
                if tmp:
                    if any(tmp_symbol):
                        q1_sum.append(int("".join(tmp)))
                tmp = []
                tmp_symbol = []
            else:
                tmp.append(char)
                tmp_symbol.append(check_for_symbol(symbols,map,row_id,char_id))
                if char_id == 139: #include end of row
                    if any(tmp_symbol):
                        q1_sum.append(int("".join(tmp)))

    print(sum(q1_sum))

    #Q2
    gear_position_dict = {}
    q2_sum = 0
    for row_id,row in enumerate(map):
        tmp = []
        tmp_symbol = []
        for char_id,char in enumerate(row):
            if char not in "0123456789":
                if tmp:
                    if any(tmp_symbol):
                        gear_position_dict[nearest_gear(gear_position_dict,len(tmp),row_id,char_id)].append(int("".join(tmp)))
                tmp = []
                tmp_symbol = []
            else:
                tmp.append(char)
                tmp_symbol.append(check_for_symbol('*',map,row_id,char_id))
                gear_position = check_gear_position(map,row_id,char_id)
                if gear_position not in gear_position_dict:
                    gear_position_dict[gear_position] = []


    # print(gear_position_dict)

    for gear in gear_position_dict:
        if len(gear_position_dict[gear]) == 2:
            # print(gear,gear_position_dict[gear])
            q2_sum += gear_position_dict[gear][0]*gear_position_dict[gear][1]
    print(q2_sum)

# 531932
# 73646890