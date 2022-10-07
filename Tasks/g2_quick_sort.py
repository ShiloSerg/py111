import random
import time
from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    # def partition(array, start, end):
    #     pivot = array[start]
    #     low = start + 1
    #     high = end
    #
    #     while True:
    #         # Если текущее значение, на которое мы смотрим, больше, чем точка поворота
    #         # он в нужном месте (справа от точки поворота), и мы можем двигаться влево,
    #         # к следующему элементу.
    #         # Нам также нужно убедиться, что мы не превзошли нижний указатель, так как
    #         # указывает, что мы уже переместили все элементы на правильную сторону от оси
    #         while low <= high and array[high] >= pivot:
    #             high = high - 1
    #
    #         # Процесс, противоположный предыдущему
    #         while low <= high and array[low] <= pivot:
    #             low = low + 1
    #
    #         # Мы либо нашли значения как для максимума, так и для минимума, которые не соответствуют порядку
    #         # или low выше high, в этом случае выходим из цикла
    #         if low <= high:
    #             array[low], array[high] = array[high], array[low]
    #             # Продолжаем цикл
    #         else:
    #             # Выходим из цикла
    #             break
    #
    #     array[start], array[high] = array[high], array[start]
    #
    #     return high
    #
    # if start >= end:
    #     return
    #
    # p = partition(container, start, end)
    # sort(container, start, p - 1)
    # sort(container, p + 1, end)

    # return container

    # 0.02238828
    if len(container) > 1:
        pivot = container[len(container) // 2]

        less = []
        greater = []
        equal = []

        for i in container:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return sort(less) + equal + sort(greater)
    else:
        return container

    # def quicksort(container: list):
    #     if len(container) <= 1:
    #         return container
    #     else:
    #         q = random.choice(container)
    #     left = [n for n in container if n < q]
    #     equals = [q] * container.count(q)
    #     right = [n for n in container if n > q]
    #     return quicksort(left) + equals + quicksort(right)
    #
    # return quicksort(container)


if __name__ == '__main__':

    arr = [random.randint(-10000, 10000) for _ in range(10000)]

    time_list = []
    for i in range(11):
        start = time.perf_counter()
        sort(arr)
        time_list.append(time.perf_counter() - start)

    print(sum(time_list) / 10)
