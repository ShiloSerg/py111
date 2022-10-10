from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    # for i in range(len(container)):
    #     for j in range(len(container) - i - 1):
    #         if container[j] > container[j+1]:
    #             container[j], container[j + 1] = container[j+1], container[j]
    # return container

    n = len(container)
    while n != 0:
        for i in range(len(container) - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
        n -= 1
    return container
