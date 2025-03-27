def function3(arrA, arrB):
    for i in range(len(arrA)):          # Runs m times
        for j in range(len(arrB)):      # Runs n times
            for k in range(1000000):    # Runs a constant 1,000,000 times
                print(arrA[i], ",", arrB[j])


# O(n)*O(m)*O(1000000) = O(m*n)