from shapely.geometry import Polygon,Point
from shapely.prepared import prep

def find_s(input_array):
    for row_id,row in enumerate(input_array):
        try:
            S_position = (row.index('S'),row_id) #x,y
        except:
            continue
    return S_position

def move(current_char,current_char_position,previous_char_position):
    moveset = {'|':[(0,1),(0,-1)],
                '-':[(1,0),(-1,0)],
                'L':[(1,0),(0,-1)],
                'J':[(-1,0),(0,-1)],
                '7':[(0,1),(-1,0)],
                'F':[(1,0),(0,1)]}
    if current_char in ['|', '-', 'L','7']:
        direction = current_char_position < previous_char_position #if true = 1, false = 0
    elif current_char == 'J':
        direction = current_char_position[0] > previous_char_position[0]
    elif current_char == 'F':
        direction = current_char_position[0] < previous_char_position[0]
        
    next_char_position = (current_char_position[0] + moveset[current_char][direction][0], current_char_position[1] + moveset[current_char][direction][1])
    return next_char_position

with open ('day10_input.txt','r') as input:
    input_array = [[pipe for pipe in row] for row in input]
    start = find_s(input_array) # find S as starting position

    #Q1
    previous_position = start
    current_position = (start[0]+1,start[1]) #cheating here by ignoring up and down since they aren't connected to S in the input hehe, assuming that there is only 1 loop now
    current_char = input_array[current_position[1]][current_position[0]]
    coordinates = [start,current_position]
    steps = 0
    while current_char != 'S':
        next_position = move(current_char,current_position,previous_position)
        previous_position = current_position
        current_position = next_position
        coordinates.append(current_position)
        current_char = input_array[next_position[1]][next_position[0]]
        steps += 1

    print((steps+1)/2) # +1 for manual first step, divide by 2 to find furthest spot in loop

    #Q2
    polygon = Polygon(coordinates) #create polygon from coordinates
    width = len(input_array[0])
    height = len(input_array)
    in_polygon = 0
    # for i in range(height):
    #     for j in range(width):
    #         if polygon.contains(Point(j,i)):   #time for some brute force, loop through all points to see if it's in the polygon hehe
    #             in_polygon += 1
    # print(in_polygon)

    #Q2 optimized
    points = []
    for i in range(height):
        for j in range(width):
            points.append(Point(j,i))
    prepared_polygon = prep(polygon)
    for i in points:
        if prepared_polygon.contains(i):
            in_polygon += 1
    print(in_polygon)

