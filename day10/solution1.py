def get_next_char(direction,char,current_index):
    
    print(direction, char, current_index )
    
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

    
    print(direction, char, current_index )


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


current_index = [129,88]
current_direction = (1,0)
current_char = 'L'

for line in file:
    matrix.append(line)

while current_char != 'S':

    current_index,current_direction = get_next_char(current_direction,current_char,current_index)
    current_char = matrix[current_index[0]][current_index[1]]
    total_steps += 1


print(total_steps)










