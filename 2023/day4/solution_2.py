file = open('day4\input.txt')

total_sum = 0
index = 0

array = [1] * 203

for line in file:
    line = line.split(':')[1]

    winning_numbers,numbers_you_have = line.split('|') 

    winning_numbers = winning_numbers.split()
    numbers_you_have = numbers_you_have.split()

    counter = 0

    for number in numbers_you_have:
        if number in winning_numbers:
            counter += 1

    for j in range(array[index]):
        try:
            for i in range(counter):
                array[index + i + 1] += 1 
        except IndexError:
            pass 
    
    index += 1 

total_sum += sum(array)



print(array)
print('total sum: ', total_sum)
file.close()
