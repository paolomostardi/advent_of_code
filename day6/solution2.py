times = [52947594]
distance = [426137412791216]

total_mul = 1

for i,time in enumerate(times):
    whatever = 0
    for j in range(time):  
        total_distance = j * (time - j)
        if total_distance > distance[i]:
            whatever += 1

    total_mul *= whatever

print(total_mul)