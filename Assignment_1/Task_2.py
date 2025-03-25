# Sum of Powers
# Write and test a recursive function that returns the sum of the first n elements of an array.


def array_sum(array, n):
    if n <= 0:
        return 0
    return array[n-1] + array_sum(array, n-1)

array = [5, 2, 3, 7, 5, 6, 9, 8, 9, 0]

n = int(input("Input the upper limit: "))

terms = [f"{i}" for i in array[:n]]
expression = " + ".join(terms)
print(f"{expression} = {array_sum(array, n)}")

