# Task 8: Given two positive integers n and k. Your task is to output all sequences like: x1, x2, ..., xn such that xi - natural and 1<=xi<=k.
# Note. Use recursion for solving this problem.
# Sample Input 1:
# 2 3


def generate_sequences(n, k, current_sequence=None):
    if current_sequence is None:
        current_sequence = []
    if len(current_sequence) == n:
        print(' '.join(map(str, current_sequence)))
        return
    for i in range(1, k + 1):
        generate_sequences(n, k, current_sequence + [i])

n, k = map(int, input().split())
generate_sequences(n, k)

# PRINT 2 NUMBERS SEPARATED BY A SPACE