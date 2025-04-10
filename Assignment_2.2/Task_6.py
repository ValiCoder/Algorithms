import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Пример:
print(heap_sort([5, 3, 8, 4, 2]))  # [2, 3, 4, 5, 8]
