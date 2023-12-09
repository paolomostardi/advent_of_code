file = open('day1\input_1.txt')
total_sum = 0

digits = ['one','two','three','four','five','six','seven','eight','nine']



for line in file:
    for char in line:
        if char.isdigit():
            first_number = int(char)
            break
    for char in line[::-1]:
        if char.isdigit():
            second_number = int(char)
            break
    total_sum += first_number * 10
    total_sum += second_number
    
print('total sum: ', total_sum)
file.close()













































 















