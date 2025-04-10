def is_valid_brackets(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


# Пример:
print(is_valid_brackets("({[]})"))  # True
print(is_valid_brackets("({[})"))  # False