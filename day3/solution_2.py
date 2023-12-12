def convert(array):
    array = array[::-1]
    sum = 0
    for index,i in enumerate(array):
        sum += int(i) * pow(10,index)
    return sum

def find_adjacent_numbers(x,y,matrix):
    answer = []
    
    for i in range(3):
        for j in range(3):
            try:
                if matrix[(y - 1) + i][(x - 1) + j].isdigit():
                    answer.append(find_number((x - 1) + j, (y - 1) + i, matrix))
            except IndexError:
                pass 
    
    return answer


def find_number(x,y,matrix):
    answer = []
    element = matrix[y][x]
    x_backup = x 

    while element.isdigit():
        answer.append(element)
        matrix[y][x] = '.'
        x -= 1
        element = matrix[y][x]

    x = x_backup
    x += 1
    element = matrix[y][x]
    answer = answer[::-1]
    while element.isdigit():
        answer.append(element)
        matrix[y][x] = '.'
        x += 1
        element = matrix[y][x]

    print(answer)

    return answer




file = open('day3\input.txt')

total_sum = 0

matrix = []

for line in file:
    array = []
    for char in line:
        array.append(char)
    matrix.append(array)


for y, array in enumerate(matrix): 
    for x, element in enumerate(array):
        number = []
        if element == '*':
            number = find_adjacent_numbers(x,y,matrix)
        if number != []:
            print(number)

        if len(number) == 2:
            total_sum += convert(number[0]) * convert(number[1])                
                


print('total sum: ', total_sum)
file.close()
