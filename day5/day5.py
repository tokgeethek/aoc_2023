with open('day5_input.txt') as input:
    input = "".join([row for row in input])
    groups = input.split('\n\n')
    seeds = [int(x) for x in groups[0].split(':')[-1].split(' ') if x]
    remaining = groups[1:]
    
    maps = []
    for x in remaining:
        map = {}
        row = x.split('\n')
        key = row[0].split(' ')[0]
        values = []
        for i in row[1:]:
            group = []
            for j in i.split(' '):
                group.append(int(j))
            values.append(group)
        map[key] = values
        maps.append(map)

    #Q1
    location = []
    for i in seeds:
        for map in maps:
            for row in map:
                for dest,source,range in map[row]:
                    if i < source + range and source <= i: # check if in range, else use value as is
                        i = dest + (i - source) # translating input, tmp-source is the difference between source and dest
                        break # break when a match is found in a row from the map
        location.append(i)

    print(min(location))

    #Q2
    q2_seeds = seeds[1::2]
    ranges = seeds[::2]
    # das alot of numbers fam


