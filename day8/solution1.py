def all_nodes_end_with_z(list_of_nodes):
    for node in list_of_nodes:
        if node[0][2] != 'Z':
            return False
    return True


file = open('day8/input.txt')

instruction_dictionary = {
    'L': 0,  
    'R': 1
    }

instructions = file.readline()
instructions = instructions.replace('\n','')
file.readline()
directions = []

counter = 0

for line in file:
    
    direction = line.split(' =')
    direction[1] = direction[1].replace('(','')
    direction[1] = direction[1].replace(')','')
    direction[1] = direction[1].replace(' ','')
    direction[1] = direction[1].replace('\n','')

    direction[1] = direction[1].split(',')
    directions.append(direction)



    
print(direction) 
current_direction = [direction for direction in directions if direction[0] == 'AAA'][0]
current_instruction_index = 0
current_instruction = instruction_dictionary[instructions[current_instruction_index]]

while current_direction[0] != 'ZZZ':
    current_direction = [direction for direction in directions if direction[0] == current_direction[1][current_instruction]][0]
    
    print(current_direction[1][current_instruction])
    print(current_direction)
    print(current_instruction)
    current_instruction_index += 1
    
    if current_instruction_index == len(instructions):
        current_instruction_index = 0
        counter += 1 
    
    current_instruction = instruction_dictionary[instructions[current_instruction_index]]
    

print(current_direction)
print(counter, current_instruction_index)
print(len(instructions))



