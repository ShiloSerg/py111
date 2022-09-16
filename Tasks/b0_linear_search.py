"""
This module implements some functions based on linear search algo
"""
import random
import time
from typing import Sequence, Union, Any


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    # 1   1.393599271774292

    min_value = arr[0]

    for value in arr:
        if value < min_value:
            min_value = value

    return arr.index(min_value)

    # 2   1.421199893951416

    # min_index = 0
    # min_element = arr[0]
    # for index, element in enumerate(arr):
    #     if element < min_element:
    #         min_index = index
    #         min_element = element
    # return min_index

    # 3   1.3457996368408203

    # elem = min(arr)
    # for i in range(len(arr)):
    #     if arr[i] == elem:
    #         return i
    # return -1

    # 4   1.3687997817993165

    # minimum = min(arr)  # O(n)
    # return arr.index(minimum)

    # нахождение просто min элемента ------------------------------
    #   1.3379998207092285
    # return min(arr)

    #   1.7755400657653808
    # arr.sort()
    # return arr[0]

    #   1.7755400657653808
    # return sorted(arr)[0]


t_1 = time.time()
a = [random.randint(-10000, 10000) for _ in range(3000000)]
for i in range(5):
    min_search(a)

print((time.time() - t_1) / 5)