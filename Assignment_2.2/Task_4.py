from collections import deque

def reverse_queue(q):
    if not q:
        return
    item = q.popleft()
    reverse_queue(q)
    q.append(item)

# Пример:
q = deque([1, 2, 3, 4, 5])
reverse_queue(q)
print(list(q))  # [5, 4, 3, 2, 1]
