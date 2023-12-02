with open('day2_input.txt') as input:
    input_array = [row.replace('\n','') for row in input]

    # Q1
    possible_dict = {'red': 12,'green': 13,'blue': 14}
    sum_of_id = 0
    sum_of_power = 0

    for game in input_array:
        subsets = game.split(':')[-1].split(';')
        id = int(game.split(':')[0].split(' ')[-1])
        merged_subset = []
        for x in subsets:
            for y in x.split(','):
                merged_subset.append(y)
        
        possible = True
        for cube in merged_subset:
            colour = cube.split(' ')[-1]
            number = int(cube.split(' ')[1])
            if number > possible_dict[colour]:
                possible = False

        if possible:
            sum_of_id += id

        print(sum_of_id)
        
        # Q2
        red_max = 0
        blue_max = 0
        green_max = 0

        for cube in merged_subset:
            colour = cube.split(' ')[-1]
            number = int(cube.split(' ')[1])

            if colour == 'red' and number > red_max:
                red_max = number
            elif colour == 'blue' and number > blue_max:
                blue_max = number
            elif colour == 'green' and number > green_max:
                green_max = number
        
        power = red_max*blue_max*green_max
        sum_of_power += power

        print(sum_of_power)