import random
import time

from typing import Sequence, Union, Any
from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    min_index = 0
    max_index = len(arr) - 1
    while max_index >= min_index:
        mid_index = (max_index + min_index) // 2
        value = arr[mid_index]
        if value == elem:
            return mid_index
        if value > elem:
            max_index = mid_index - 1
        if value < elem:
            min_index = mid_index + 1
    #
    # t_1 = time.time()
    # a = [random.randint(-10000, 10000) for _ in range(3000000)]
    # for i in range(5):
    #     min_search(a)
    #
    # print((time.time() - t_1) / 5)
    #
    #
    # print(elem, arr)
    # return None
