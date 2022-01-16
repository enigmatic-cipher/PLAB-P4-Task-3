"""
Given n as input. Print the factorial of n.
Note: Factorial of n = 1*2*3*4*.....*n [total product from 1 to n]
"""

n = int(input("Enter number to calculate factorial: "))
for i in range(1, n):
  n = n * i
print(n)
