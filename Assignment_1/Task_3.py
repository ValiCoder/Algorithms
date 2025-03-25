# Task 3: Write a recursive method to compute the sum of the first n positive integers

def sum_of_numbers(n):
    if n <= 0:
        return 0
    return n + sum_of_numbers(n - 1)


n = int(input("Input the upper limit: "))

terms = [f"{i}" for i in range (1, n + 1)]
expression = " + ".join(terms)
print(f"{expression} = {sum_of_numbers(n)}")
