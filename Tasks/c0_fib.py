def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError('Число не должно быть отрицательным')
    if n in (0, 1):
        return n
    # first_value = 0
    # second_value = 1
    # if n == first_value:
    #     return first_value
    # elif n == second_value:
    #     return second_value
    # else:
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n < 0:
        raise ValueError('Число не должно быть отрицательным')
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b

    return a


    # if n < 0:
    #     raise ValueError('Число не должно быть отрицательным')
    #
    # if n in (0, 1):
    #     return n
    # # if n == 0:
    # #     return 0
    # # if n == 1:
    # #     return 1
    # list_of_numbers = list(range(n + 1))
    #
    # for value in list_of_numbers[2:]:
    #     list_of_numbers[value] = list_of_numbers[value - 1] + list_of_numbers[value - 2]
    # return list_of_numbers[-1]


def fib_generator(n: int) -> int:
    if n < 0:
        raise ValueError('Число не должно быть отрицательным')
    a, b = 0, 1
    for i in range(0, n + 1):
        yield a
        a, b = b, a + b


#     if n < 0:
#         raise ValueError('Число не должно быть отрицательным')
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     list_of_numbers = list(range(n + 1))
#
#     for value in list_of_numbers[2:]:
#         list_of_numbers[value] = list_of_numbers[value - 1] + list_of_numbers[value - 2]
#         new_value = list_of_numbers[value]
#         yield new_value
#     # return list_of_numbers[-1]
