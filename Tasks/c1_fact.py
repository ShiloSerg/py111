def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError('Число не должно быть отрицательным')
    if n in (0, 1):
        return 1
    return factorial_recursive(n - 1) * n


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError('Число не должно быть отрицательным')
    value = 1
    while n != 0:
        value *= n
        n -= 1
    return value

    # 1 -------------------

    # result = 1
    #
    # while n > 1:
    #     result *= n
    #     n -= 1
    #
    # return result

    # 2 -------------------

    # fact = 1
    #
    # for i in range(fact, n+1):
    #     fact *= i
    #
    # return fact


def factorial_generator(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError('Число не должно быть отрицательным')
    value = 1
    for i in range(1, n):
        value *= i
        yield value

    # 2 ---------------
    # if n < 0:
    #     raise ValueError
    #
    # fact = 1
    #
    # if n in (0, 1):
    #     yield fact
    #
    # for i in range(1, n + 1):
    #     yield fact
    #     fact *= i



if __name__ == '__main__':
    f_gen = factorial_generator(12)
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
    print(next(f_gen))
