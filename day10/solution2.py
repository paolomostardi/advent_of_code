def get_next_char(direction,char,current_index):
    
    
    if char in dict_straight:
        to_sum = dict_straight[char]
        current_index = [current_index[0] + to_sum[0] * direction[0], current_index[1] + to_sum[1] * direction[1]]
        direction = (to_sum[0] * direction[0],to_sum[1] * direction[1])

    else:
        to_sum = dict_angles[char]
        if direction[0]:
            current_index = [current_index[0],current_index[1] + to_sum[1]]
            direction = (0,to_sum[1])
        else :
            current_index = [current_index[0] + to_sum[0], current_index[1]]
            direction = (to_sum[0],0)



    return  current_index,direction



file = open('day10/input.txt')
 
total_steps = 1

matrix = []


# x and y are inverted (y,x)

dict_straight = {
    '|' : (1,0),
    '-' : (0,1)
}

dict_angles = {

    'L' : (-1,1),
    'J' : (-1,-1),
    '7' : (1,-1),
    'F' : (1,1)
} 

current_index = [4,12]
current_direction = (1,1)
current_char = 'F'

for line in file:
    matrix.append(line)

angles = []

while current_char != 'S':

    if current_char in dict_angles:
        angles.append(current_index)

    current_index,current_direction = get_next_char(current_direction,current_char,current_index)
    current_char = matrix[current_index[0]][current_index[1]]

    total_steps += 1

total_area_1 = 0 
total_area_2 = 0
n = len(angles) 

for index in range(n):
    total_area_1 += angles[index][0] * angles[(index + 1) % n][1]
    total_area_2 += angles[index][1] * angles[(index + 1) % n][0]

total_area = abs(total_area_1 - total_area_2)

for angle in angles:
    print(angle)

print(total_area)
print(total_steps)
print(current_index)









