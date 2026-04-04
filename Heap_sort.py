# Heap sort
# Time: 0(n log n), Space: 0(n)
# 0 (1) Space is possible via swapping
import heapq
def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    return new_list
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# or
import heapq

def heapsort(arr):
    heapq.heapify(arr)
    sorted_list = []
    while arr:
        sorted_list.append(heapq.heappop(arr))
    return sorted_list

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
