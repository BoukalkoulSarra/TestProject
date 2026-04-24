# area_calculator.py - Calculate area of shapes

def circle_area(radius):
    return 3.14 * radius * radius

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return side * side

# Test
print(f"Circle area (r=5): {circle_area(5)}")
print(f"Rectangle area (4x6): {rectangle_area(4, 6)}")
print(f"Square area (side=7): {square_area(7)}")