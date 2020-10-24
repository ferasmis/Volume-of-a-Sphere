## Author: Feras
## Description: Find the volume of a sphere using a radius from user input

radius = float(input('Enter a radius of a sphere:\n'))
pi = 3.14
volume = (4/3) * pi * radius**3
print('Volume is %.2f' % volume)