file = open('day12/input.txt')


def find_all_legal_placement(row, index = 0):
    
    if   index  == len(row[1]):
        return 1

    counter = index
    for i, char in enumerate(row[0]):
        if counter == 0:
            if char == '?':
                pass

    return find_all_legal_placement(row, index + 1)   


def check_legal(row):
     
    string = list(row[0])

    
    
    for i in row[1]:

        for index,char in enumerate(string):
            if char == '#':
                while string[index] == '#':
                    i -= 1
                    string[index] = '.'
                    index += 1
                    if index == len(string):
                        break
                break

        if i != 0:
            return False
        
    if '#' in string:
        return False
    

    return True    

def get_all_permutations(string):
    if '?' not in string:
        return [string]
    
    index = string.index('?')
    
    string1 = string[:index] + '.' + string[index+1:]
    string2 = string[:index] + '#' + string[index+1:]
    
    return get_all_permutations(string1) + get_all_permutations(string2)





rows = []
for line in file:
    row = line.split()
    row[1] = row[1].split(',')
    rows.append(row)

print(check_legal(['..#..#.....###.',[1, 1, 3]]))



c = 0
for row in rows:
    print('----------------')
    
    for i,_ in enumerate(row[1]):
        row[1][i] = int(_)

    print(row)

    for i in get_all_permutations(row[0]):
        
        if check_legal([i,list(row[1])]):
            c += 1


print(c)

