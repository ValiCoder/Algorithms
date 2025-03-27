def is_power_of_two(n):
    if n == 1:
        return True
    if n < 1 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)


n = int(input("Enter a number: "))
if is_power_of_two(n):
    print(f"{n} is a power of two")
else:
    print(f"{n} is NOT a power of two")