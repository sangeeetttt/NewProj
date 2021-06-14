'''
8. Write a Python program which accepts the radius of a circle from the user and compute the area. (area of circle = PI * r2)

'''
import math

radious = int(input('the radious of the circle in cm: '))
area = math.pi * radious**2
print(f'area of the circle is {area}sq.cm')
