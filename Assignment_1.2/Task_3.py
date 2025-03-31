n = int(0)  # Global variable

def function3(arrA, arrB):
    global n  # Declare that we are modifying the global variable
    for i in range(len(arrA)):  # Runs m times
        for j in range(len(arrB)):  # Runs n times
            for k in range(1000000):  # Runs a constant 1,000,000 times
                print(arrA[i], ",", arrB[j])
                n = n + 1  # Modify the global variable

arrA = [1]
arrB = [1, 2]

function3(arrA, arrB)

print(n)