import math

with open ('day8_input.txt','r') as input:
    input_array = [row.replace('\n','') for row in input]
    instructions = list(map(int,input_array[0].replace('L','0').replace('R','1')))
    nodes = {}
    for node in input_array[2:]:
        nodes[node.split('=')[0].strip()] = [node.split('=')[-1].strip()[1:4],node.split('=')[-1].strip()[6:9]]

    #Q1
    steps = 0
    current_step = 'AAA'
    while current_step != 'ZZZ':
        for direction in instructions:
            current_step = nodes[current_step][direction]
            steps += 1

    print(steps)

    #Q2
    starts = [key for key in nodes if str(key)[-1] == 'A']
    ends = [key for key in nodes if str(key)[-1] == 'Z']
    steps_for_each_start = []
    for start in starts:
        q2_steps = 0
        q2_current_step = start
        while q2_current_step not in ends:
            for direction in instructions:
                q2_current_step = nodes[q2_current_step][direction]
                q2_steps += 1
        steps_for_each_start.append(q2_steps)

    # going on the assumption that all steps must be multiples of each other to be able to simultaneosly reach Z
    print(math.lcm(*steps_for_each_start)) 



