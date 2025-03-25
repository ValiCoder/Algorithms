# Task 6: Write and test a recursive function that returns the sum of the first n powers of a base b.
# Given a positive integer N and a sequence of N strings. You have to display given sequence in reverse order.
#
# Note. The program is forbidden to declare arrays (only one char array in function is allowed), and use the cycles (even for input).
#
# Input: First line contains n (1<=n<=100). The next n lines contain onedimension char arrays. Array is no longer that 20 symbols.
#
# Output: The sequence of element in reverse order.
# Sample Input: 3
# Abc
# bcdh
# abcdef
#
# Sample Output:
# abcdef
# bcdh
# abc

def input_arr_reverse(n):
    if n == 0:
        return
    element = input()
    input_arr_reverse (n-1)
    print(element.lower())

n = int(input("Input number of elements, then input the elements of the array:"))
input_arr_reverse(n)