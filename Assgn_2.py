# Assignment 2: Gauss-Jordan Elimination
# Name: Roshan Yadav
# Roll no: 2311144
from Func_lib_for_Assgn_2 import *

# Question 1
A= read_matrix("A.txt")  # Read matrix A from file  
b= read_matrix("b.txt")  # Read matrix b from file
b = b[0]  # Taking only the first row
A = matrix(A)
print("Question 1 solution:", A.gauss_jorden(b)) # output: [-2.0, -2.0, 1.0]

# Question 2
C= read_matrix("C.txt")
d= read_matrix("d.txt")
# Converting [[1], [2], [3]] to [1, 2, 3] if needed
if d and isinstance(d[0], list):
    d = [row[0] for row in d]
C= matrix(C)
print("Question 2 solution:", C.gauss_jorden(d)) # Output: [-3.158521292345206, 2.592301663328398, 6.991848819994775, -3.461830532090917, 2.72279892014282, 1.3681529217103545]
