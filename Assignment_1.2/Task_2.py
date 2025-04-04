import time

def function2(arr):
    global n
    n = 0  # Reset counter
    for i in range(len(arr)):  # Runs n times
        n += 1
        for j in range(len(arr)):  # Nested loop runs n times
            n += 1
            print(arr[i], ",", arr[j])  # O(1) operation

size = 100

array = list(range(1, size + 1))

start_time = time.time()  # Start timer
function2(array)
end_time = time.time()  # End timer

print("Total operations:", n)
print(f"Execution time: {end_time - start_time:.6f} seconds")

# O(n^2)
