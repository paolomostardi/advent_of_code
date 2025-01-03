def transform_line(line):
    new_line = []
    for index,number in enumerate(line):
        if index == len(line) - 1:
            break 
        new_line.append((line[index + 1] - number))
    return new_line

def calculate_next_sequence(operation):
    
    operation = operation[::-1]
    n = 0
    for index,line in enumerate(operation):
        print(index,line,n)
        n_index = len(line) 
        if index == len(operation) - 1:
            break
        n = operation[index + 1][0] - n
        
    return n

file = open('day9/input.txt')

total_sum = 0

for line in file:
    line = line.split()
    line = [int(number) for number in line]
    operation = []
    operation.append(line)
    while not all(number == 0 for number in line):
        line = transform_line(line)
        operation.append(line)

    print('------------------')
    total_sum += calculate_next_sequence(operation)


print(total_sum)

file.close() 











