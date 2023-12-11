file = open('day2\input.txt')
total_sum = 0 

red_amount = 12
green_amount = 13 
blue_amount = 14

red,blue,green = 'red','blue','green'

for line in file:

    blue_max = 0
    red_max = 0
    green_max = 0

    id,line = line.split(':')   
    line = line.split(';')
    possible = True

    for piece in line :
        piece = piece.split(',')
        for color in piece:

            if red in color:
                red_amount = int(color.split()[0])
                if red_amount > red_max:
                    red_max = red_amount

            elif blue in color:
                blue_amount = int(color.split()[0])
                if blue_amount > blue_max:
                    blue_max = blue_amount

            elif green in color:
                green_amount = int(color.split()[0])
                if green_amount > green_max:
                    green_max = green_amount

    print(red_max,blue_max,green_max)

    print(line)

    total_sum += red_max * blue_max * green_max
    
print('total sum: ', total_sum)
file.close()

