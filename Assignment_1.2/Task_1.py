import time

def function1(arr):
    global n
    n = 0

    sum_val = 0
    product = 1
    for i in range(len(arr)):
        n += 1
        sum_val += arr[i]
    for i in range(len(arr)):
        n += 1
        product *= arr[i]
    print(sum_val, ",", product)
 # O(1)+O(n)+O(n)+O(1)=O(2n+2) = O(2n)

size = 1000

array = list(range(1, size + 1))

start_time = time.time()  # Start timer
function1(array)
end_time = time.time()  # End timer

print("Total operations:", n)
print(f"Execution time: {end_time - start_time:.6f} seconds")