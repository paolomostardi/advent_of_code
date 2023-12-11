file = open('day2\input.txt')
total_sum = 0 

red_amount = 12
green_amount = 13 
blue_amount = 14

red,blue,green = 'red','blue','green'

for line in file:
    id,line = line.split(':')   
    line = line.split(';')
    possible = True

    for piece in line :
        piece = piece.split(',')
        for color in piece:

            if red in color:
                if red_amount < int(color.split()[0]):
                    possible = False

            elif blue in color:
                if blue_amount < int(color.split()[0]):
                    possible = False

            elif green in color:
                if green_amount < int(color.split()[0]):
                    possible = False 

    if possible:
        total_sum += int(id.split()[1])
    
print('total sum: ', total_sum)
file.close()

