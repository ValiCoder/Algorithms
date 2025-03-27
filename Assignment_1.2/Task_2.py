def function2(arr):
    for i in range(len(arr)):          # Loop runs n times
        for j in range(len(arr)):      # Nested loop runs n times
            print(arr[i], ",", arr[j]) # Constant time operation O(1)

# O(n)* O(n) + O(1) = O((n^2)+1) = O(n^2)