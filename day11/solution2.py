

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

factor = 1000000 - 1

counter = 0

print(columns_rows)

for index, column_row in enumerate(columns_rows):
    if column_row[0] == 0:
        
        for galaxy_index, galaxy in enumerate(galaxies):
            if galaxy[0] > index + expansion1:
                galaxies[galaxy_index][0] += factor
                counter += 1

        expansion1 += factor
                
    if column_row[1] == 0:
        
        for galaxy_index, galaxy in enumerate(galaxies):
            if galaxy[1] > index + expansion2:
                galaxies[galaxy_index][1] += factor
                counter += 1
        expansion2 += factor
                
print('--------------')

for i in galaxies:
    print(i)

print('--------------')

for i, c in enumerate(columns_rows):
    print(i,c)

print('--------------')


n = len(galaxies)
print(n)

print('expansion of columns : ', (expansion1//factor))
print('expansion of rows : ', (expansion2//factor))
print('total expansion added to coordinates: ', counter)

total_distance = 0
for index, galaxy in enumerate(galaxies):
    print('-------------')
    for i in range(index + 1, n):
        print(total_distance, galaxy, galaxies[i])
        total_distance += calcualte_distance(galaxy, galaxies[i])

print(total_distance)