a = len(arr) - 1  # O(1)
out = list()  # O(1)
while a > 0:  # O(logk(N))
    out.append(arr[a]) # O(1)
    a = a // 1.7  # O(1)
out.merge_sort()  # O(n log n)


O(1) + O(1) + O(logk(N)) + O(1) + O(1)  + O(n log n) = O(logk(N)) + O(n log n)

Ответ: O(logk(N))