Pascal's Triangle Project
Overview
This Python project implements a function, pascal_triangle(n), which returns a list of lists of integers representing Pascal's Triangle for a given number of rows n.

Pascal's Triangle is a triangular array of numbers where the values at each row are the coefficients of the binomial expansion. Each number is the sum of the two directly above it in the previous row.

Requirements
Function Name: pascal_triangle(n)
Parameters:
n (integer): The number of rows in the Pascal's Triangle.
Return:
A list of lists of integers representing Pascal's Triangle up to n rows.
Returns an empty list if n is less than or equal to 0.
Example
python
def pascal_triangle(n):
    # Your implementation here
Sample Output
python
>>> pascal_triangle(5)
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
Edge Case
python
>>> pascal_triangle(0)
[]
Assumptions
The value of n will always be a positive integer or zero.
How to Run
Clone this repository.
Ensure you have Python installed.
Run the function using a Python interpreter or script.
bash

python -i pascal_triangle.py
You can also import the function into other scripts or testing frameworks.

Testing
You can test the function by running it with various values of n to generate Pascal's Triangle with different numbers of rows.

Example:

python
print(pascal_triangle(7)) # Will print the triangle up to 7 rows
Conclusion
This project helps understand recursive patterns and how to build and return nested lists in Python. Pascal's Triangle is a fundamental mathematical concept that provides insight into combinatorics and binomial expansions.
