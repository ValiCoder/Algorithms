# Task 5: Given a positive integer N and a sequence of N elements. You have to display given sequence in reverse order.
# Note. The program is forbidden to declare arrays, and use the cycles (even for input).
# Sample Input: 3
# 1 2 3
# Sample Output: 3 2 1


def input_arr_reverse(n):
    if n == 0:
        return 0
    element = input()
    input_arr_reverse (n-1)
    print(element, end = " ")

n = int(input("Input number of elements, then input the elements of the array:"))
input_arr_reverse(n)
