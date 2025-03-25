def sum_of_powers(b, n):
    if n <= 0:
        return 0
    return b ** (n - 1) + sum_of_powers(b, n - 1)

base = int(input("Enter the base (b): "))
num_terms = int(input("Enter the number of terms (n): "))

terms = [f"{base}^{i}" for i in range(num_terms)]
expression = " + ".join(terms)

result = sum_of_powers(base, num_terms)
print(f"{expression} = {result}")