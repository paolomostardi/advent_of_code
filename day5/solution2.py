def transorm_seeds(seeds):
    new_seeds = []
    for index, seed in enumerate(seeds):
        if index % 2 == 0:
            new_seeds.append(range(seed, seed + seeds[index + 1]))

    seeds = []

    print('assing the seeds')

    for i in new_seeds:
        for j in i:
            seeds.append(j)


    return seeds 




file = open('day5\input.txt')

seeds = list(map(int,file.readline().split(':')[1].split()))
file.readline()
maps = []
index = -1

seeds = transorm_seeds(seeds)


print('seeds done')

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

for wee in maps:
    print('seeds batch done')
    for seed_index,seed in enumerate(seeds):
        skipping = False
        for line in wee:
            if line != ():
                if line[1] <= seed <= line[1] + line[2]:
                    seeds[seed_index] += line[0] - line[1] 
                    skipping = True 
                    break
     

print(min(seeds))
print(seeds)