def reverse_string(s):
    stack = list(s)
    reversed_s = ''
    while stack:
        reversed_s += stack.pop()
    return reversed_s

# Пример:
print(reverse_string("Hello World"))  # "dlroW olleH"
