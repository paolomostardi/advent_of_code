def convert(array):
    sum = 0
    for index,i in enumerate(array):
        sum += int(i) * pow(10,index)
    return sum

def find_adjacent_numbers(x,y,matrix):
    answer = False

    char = matrix[y - 1][x - 1]
    char = matrix[y + 1][x - 1]
    char = matrix[y][x - 1]    
    char = matrix[y - 1][x ]
    char = matrix[y][x ]
    char = matrix[y + 1 ][x ]
    
    

    


    if y > 0:
        if char != '.' and not(char.isdigit()) and char != '\n':
                answer = True
    
    if y < 139:
        char = matrix[y + 1][x - 1]
        if char != '.' and not(char.isdigit()) and char != '\n':
            answer = True

    if x > 0:
        char = matrix[y][x-1]
        if char != '.' and not(char.isdigit()) and char != '\n':
            answer = True

    if x < 139:
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
        if element == '*':
            find_adjacent_numbers(x,y,matrix)

        if number != []:
            print(number,x,y)
            if is_to_add(matrix,(y,x),len(number)):
                total_sum += convert(number[::-1])
                


print('total sum: ', total_sum)
file.close()
