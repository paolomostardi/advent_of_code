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

list_of_all_nodes = []

for node in directions:
    if node[0][2] == 'A':
        list_of_all_nodes.append(node)
   
print(direction) 
current_instruction_index = 0
current_instruction = instruction_dictionary[instructions[current_instruction_index]]

while not all_nodes_end_with_z(list_of_all_nodes):
    
    for index,node in enumerate(list_of_all_nodes):
        list_of_all_nodes[index] = [direction for direction in directions if direction[0] == node[1][current_instruction]][0]

    current_instruction_index += 1
    
    if current_instruction_index == len(instructions):
        current_instruction_index = 0
        counter += 1 
        if counter % 1000 == 0:
            print('increasing the coutner ', counter)
    
    current_instruction = instruction_dictionary[instructions[current_instruction_index]]
    

print(list_of_all_nodes)
print(counter, current_instruction_index)
print(len(instructions))

print(16563603485021)

