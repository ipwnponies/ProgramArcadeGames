print('Area of a Trapezoid')
height = float(input('Enter the height of the trapezoid:'))
lengthBottom = float(input('Enter the height of the bottom base:'))
lengthTop = float(input('Enter the height of the top base:'))

area = (lengthTop + lengthBottom) / 2 * height

print('The area is: {0}'.format(area))
