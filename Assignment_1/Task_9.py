def permutations(s, left, right):
    if left == right:
        print(''.join(s))
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]  # Swap
            permutations(s, left + 1, right)
            s[left], s[i] = s[i], s[left]  # Backtrack

input_string = input().strip()
n = len(input_string)
s = list(input_string)

permutations(s, 0, n - 1)