file = open('day1\input_1.txt')
total_sum = 0

digits = ['one','two','three','four','five','six','seven','eight','nine']
reversed_digits = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

exit = False

for line in file:
    for index,char in enumerate(line):
        if char.isdigit():
            first_number = int(char)
            break
        
        for digit in digits:
            for digit_index,digit_char in enumerate(digit):
                if digit_char == line[digit_index + index]:
                    if digit_index == len(digit) - 1:
                        first_number = digits.index(digit) + 1 
                        exit = True
                else:
                    break
        if (exit):
            exit = False
            break

    line = line[::-1]

    for index,char in enumerate(line):
        if char.isdigit():
            second_number = int(char)
            break

        for digit in reversed_digits:
            
            for digit_index,digit_char in enumerate(digit):

                if digit_char == line[digit_index + index]:
                    if digit_index == len(digit) - 1:
                        second_number = reversed_digits.index(digit) + 1 
                        exit = True
                else:
                    break

        if (exit):
            exit = False
            break


    total_sum += first_number * 10
    total_sum += second_number

print('total sum: ', total_sum)
file.close()













































 















