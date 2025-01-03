
def transorm_seeds(seeds):
    new_seeds = []
    for index, seed in enumerate(seeds):
        if index % 2 == 0:
            new_seeds.append((seed, seed + seeds[index + 1]))

    return new_seeds 

file = open('day5\input.txt')

seeds = list(map(int,file.readline().split(':')[1].split()))
file.readline()
maps = []
index = -1

seeds = transorm_seeds(seeds)

def filter_seed_difference(current_map, seed_difference):

    for line in current_map:
        new_seed = []
        for seed in seed_difference:
            if line != ():
                line_range = (line[1], line[1] + line[2])
                if seed[0] > line_range[1] or seed[1] < line_range[0]:
                    new_seed.append(seed)
                    continue

                if seed[0] < line_range[0]:
                    difference = line_range[0] - seed[0]
                    new_seed.append((seed[0], seed[0] + difference - 1))
                
                if seed[1] > line_range[1]:
                    difference =  seed[1] - line_range[1]
                    new_seed.append((line_range[1] + 1, line_range[1] + difference - 1))
        seed_difference = new_seed       

    return seed_difference

for line in file:

    if 'map' in line:
        index += 1 
        maps.append([])
        continue

    else :
        maps[index].append(line)

for map_index,wee in enumerate(maps):
    for line_index,line in enumerate(wee):
        maps[map_index][line_index] = tuple(map(int,maps[map_index][line_index].split()))


print('maps')
print(maps)
for current_map in maps:
    new_seed = []
    seed_difference = []
    for seed_index,seed in enumerate(seeds):
        skipping = True 
        for line in current_map:
            if line != ():
                
                line_range = (line[1], line[1] + line[2])
                
                if seed[0] > line_range[1] or seed[1] < line_range[0]:
                    print('seed ranges :')
                    print(seed[0] , line_range[1])
                    print(seed[1] , line_range[0])
                    continue
                skipping = False
                current_seed = [seed[0],seed[1]]

                # seed range is coming out from the left 
                if seed[0] < line_range[0]:
                    difference = line_range[0] - seed[0]
                    seed_difference.append((seed[0], seed[0] + difference - 1))
                    current_seed[0] += difference 

                # seed range is coming out from the right 
                if seed[1] > line_range[1]:
                    difference =  seed[1] - line_range[1]
                    seed_difference.append((line_range[1] + 1, line_range[1] + difference - 1))
                    current_seed[1] -=  seed[1] - line_range[1]

                current_seed[0] += line[0] - line[1]
                current_seed[1] += line[0] - line[1]

                new_seed.append(current_seed)
        if skipping:
            print('skipping')
            new_seed.append(seed)

    seed_difference = filter_seed_difference(current_map,seed_difference)

    if seed_difference:
        new_seed.extend(seed_difference)
    seeds = new_seed
    print(seeds)

sort_seeds = sorted(seeds, key=lambda x:x[0])
