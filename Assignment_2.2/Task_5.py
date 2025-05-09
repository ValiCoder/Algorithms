import heapq

def kth_smallest(arr, k):
    heapq.heapify(arr)
    for _ in range(k - 1):
        heapq.heappop(arr)
    return heapq.heappop(arr)

# Пример:
print(kth_smallest([7, 10, 4, 3, 20, 15], 3))  # 7
