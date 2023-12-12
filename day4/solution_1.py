file = open('day4\input.txt')

total_sum = 0

for line in file:
    line = line.split(':')[1]

    winning_numbers,numbers_you_have = line.split('|') 

    winning_numbers = winning_numbers.split()
    numbers_you_have = numbers_you_have.split()

    counter = 0

    for number in numbers_you_have:
        if number in winning_numbers:
            counter += 1

    if counter > 0:
        total_sum += pow(2,counter - 1)
    


print('total sum: ', total_sum)
file.close()
