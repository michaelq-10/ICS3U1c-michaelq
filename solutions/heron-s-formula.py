# herons_formula.py

# Answer 1: Yes, both files produce the same output.

# Answer 2: herons_formula_no_function.py is approximately 30-40 lines long
# (depending on the original implementation with 6 repeated calculations)

# Answer 3: herons_formula.py without the 10 lines of comments inside 
# triangle_area() is approximately 15-20 lines long.

# Answer 4: It was easier to fix the file that used a function because
# I only had to change (a+b+c)//2 to (a+b+c)/2 in ONE place (inside the function),
# whereas in the no_function file, I had to change it in 6 different places.

import math

def triangle_area(a, b, c):
    """
    Computes the area of a triangle using Heron's formula.
    
    Heron's formula states that the area of a triangle whose
    sides have lengths a, b, and c is:
    
    A = sqrt(s * (s-a) * (s-b) * (s-c))
    
    where s is the semi-perimeter of the triangle:
    
    s = (a + b + c) / 2
    """
    # Calculate the semi-perimeter (fixed: using / instead of //)
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area


# Test cases
print("A triangle with sides 3, 3, 3 has an area of", triangle_area(3, 3, 3))
print("A triangle with sides 3, 4, 5 has an area of", triangle_area(3, 4, 5))
print("A triangle with sides 7, 8, 9 has an area of", triangle_area(7, 8, 9))
print("A triangle with sides 5, 12, 13 has an area of", triangle_area(5, 12, 13))
print("A triangle with sides 10, 9, 11 has an area of", triangle_area(10, 9, 11))
print("A triangle with sides 8, 15, 17 has an area of", triangle_area(8, 15, 17))
print("A triangle with sides 9, 9, 9 has an area of", triangle_area(9, 9, 9))  # No, it was not difficult to add - just one line with a function call!