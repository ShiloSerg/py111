from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    # 1 -------------------------------------------------------- не проходит тесты

    # def fun_binary(left_part, right_part):
    #     middle_index = (left_part + right_part) // 2
    #     middle_value = arr[middle_index]
    #
    #     if left_part == right_part != elem:
    #         return None
    #
    #     if middle_value == elem:
    #         return middle_index
    #
    #     elif middle_value < elem:
    #         new_left_part = middle_index + 1
    #         return fun_binary(new_left_part, right_part)
    #
    #     else:
    #         new_right_part = middle_index - 1
    #         if new_right_part < 0:
    #             return None
    #         return fun_binary(left_part, new_right_part)
    #
    # left_part = 0
    # right_part = len(arr) - 1
    #
    # return fun_binary(left_part, right_part)

    # 2 ------------------------------------------------------
    try:
        left = 0
        right = len(arr) - 1
        mid = (left + right) // 2

        if elem == arr[mid]:
            return mid

        if elem > arr[mid]:
            return binary_search(elem, arr[mid + 1:]) + (mid + 1)

        return binary_search(elem, arr[:mid])
    except:
        return None


if __name__ == '__main__':
    print(binary_search(2, [0, 2, 4, 6, 8, 10]))
