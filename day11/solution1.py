

def calcualte_distance(a,b):
    return  abs(a[0] - b[0]) + abs(a[1] - b[1])


file = open('day11/input.txt')

counter1 = 0
galaxies = []
        
for line in file:
    counter2 = 0
    for char in line:
        if char == '#':
            galaxies.append([counter2,counter1])
        counter2 += 1
    counter1 += 1        

columns_rows = [[0,0] for x in range(counter1)] 

for i in galaxies:
    print(i)

print(counter1,counter2)

for i in galaxies: 
    columns_rows[i[0]][0] = 1
    columns_rows[i[1]][1] = 1

print('--------------')
expansion1 = 0
expansion2 = 0 
for index, column_row in enumerate(columns_rows):
    if column_row[0] == 0:
        
        for galaxy_index, galaxy in enumerate(galaxies):
            if galaxy[0] > index + expansion1:
                galaxies[galaxy_index][0] += 1
        expansion1 += 1
                
    if column_row[1] == 0:
        
        for galaxy_index, galaxy in enumerate(galaxies):
            if galaxy[1] > index + expansion2:
                galaxies[galaxy_index][1] += 1
        expansion2 += 1
                
print('--------------')

for i in galaxies:
    print(i)

n = len(galaxies)
print(n)

total_distance = 0
for index, galaxy in enumerate(galaxies):
    for i in range(n - index):
        total_distance += calcualte_distance(galaxy,galaxies[index + i])

print(total_distance)