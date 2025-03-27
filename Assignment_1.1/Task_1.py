# Task 1: Write and test a recursive function that returns
# the sum of the squares of the first n positive integers.

def sum_of_squares(n):
    if n == 1:
        return 1
    return n**2 + sum_of_squares(n - 1)

n = int (input("Input the upper limit: "))
result = sum_of_squares(n)

terms = [f"{i}^2" for i in range(1, n + 1)]
expression = " + ".join(terms)

print(f"{expression} = {result}")