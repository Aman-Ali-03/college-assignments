# Write a function calculate_area(radius) that calculates and returns the area of a circle.

def calculate_area(radious):
    return 3.1416*(radious**2)

radious = int(input('Enter the radious of the circle: '))
print(calculate_area(radious=radious))