import math

x1 = int(input('Inpyt point x1: '))
y1 = int(input('Inpyt point y1: '))

x2 = int(input('Inpyt point x2: '))
y2 = int(input('Inpyt point y2: '))

print(f'The distance from your points are {math.sqrt(((x1-x2)**2)+((y1-y2)**2))}')