def convert(array):
    sum = 0
    for index,i in enumerate(array):
        sum += int(i) * pow(10,index)
    return sum

def is_to_add(matrix,index,length):
    answer = False
    y,x = index

    if y > 0:
        for i in range(length + 2):
            char = matrix[y - 1][x + i - 1]
            if char != '.' and not(char.isdigit()) and not '\n':
                answer = True
    
    if y < 139:
        for i in range(length + 2):
            char = matrix[y + 1][x + i - 1]
            if char != '.' and not(char.isdigit()) and char != '\n':
                answer = True

    if x > 0:
        char = matrix[y][x-1]
        if char != '.' and not(char.isdigit()) and char != '\n':
            answer = True

    if x < 139 - length:
        char = matrix[y][x + length]
        if char != '.' and not(char.isdigit()) and char != '\n':
            answer = True
    
    return answer

file = open('day3\input.txt')

total_sum = 0

matrix = []

for line in file:
    array = []
    for char in line:
        array.append(char)
    matrix.append(array)
print(matrix[1][79])


for y, array in enumerate(matrix): 
    for x, element in enumerate(array):
        number = []
        while element.isdigit():            
            number.append(element)
            element = array[x + len(number)]
            matrix[y][x+len(number) - 1] = '.'

        if number != []:
            print(number,x,y)
            if is_to_add(matrix,(y,x),len(number)):
                total_sum += convert(number[::-1])
                


print('total sum: ', total_sum)
file.close()
