with open('day6_input.txt') as input:
    #Q1
    input = "".join([row for row in input])
    time_available = list(map(int,input.split('\n')[0].split(':')[-1].split()))
    distance_to_beat = list(map(int,input.split('\n')[-1].split(':')[-1].split()))

    q1_ans_list = []
    for i,race_time in enumerate(time_available):
        win = 0
        for holding_time in range(race_time):
            travel_dist = (race_time - holding_time) * holding_time
            if travel_dist > distance_to_beat[i]:
                win += 1
        q1_ans_list.append(win)

    q1_ans = 1
    for x in q1_ans_list:
        q1_ans *= x
    print(q1_ans)

    #Q2
    input = input.replace(' ','')
    time_available = list(map(int,input.split('\n')[0].split(':')[-1].split()))
    distance_to_beat = list(map(int,input.split('\n')[-1].split(':')[-1].split()))
    q2_ans = 0
    for holding_time in range(time_available[0]):
        travel_dist = (time_available[0] - holding_time) * holding_time
        if travel_dist > distance_to_beat[0]:
            q2_ans += 1
    print(q2_ans)

