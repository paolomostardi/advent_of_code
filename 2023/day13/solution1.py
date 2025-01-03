

def find_simmetry(line,dic,index,matrix) -> int:

    first_index = dic[line]
    second_index = index 



    while first_index > 0 and second_index < len(matrix):
        
        first_index 


    return 0

def calculate(matrix) -> int:

    dic = {}
    for index,line in enumerate(matrix):
        if line in dic:
            check = find_simmetry(line,dic,index,matrix)
            if check != 0:
                return check
        else:
            dic[line] = index
    return 0



matrix= []
result = 0
for line in open('2023/day13/input.txt'):
    if line == '\n':
        result += calculate(matrix)
        matrix = []
    else:
        matrix.append(line[:-1])

print(result)