from random import randint
import time
from g2_quick_sort import sort as q_sort
from g1_merge_sort import sort as m_sort
from g0_bubble_sort import sort as b_sort

if __name__ == '__main__':
    time_list = []
    list_of_values = [randint(13, 25) for _ in range(10**6)]


    def q_sorta(list_values: list):
        """
        Измерение скорости работы Алгоритма quick_sort
        """
        q_list = list_values  # 0.2964115999639034
        start_ = time.perf_counter()
        q_sort(q_list)
        time_list.append(time.perf_counter() - start_)
        print(q_list)


    def m_sorta(list_values: list):
        """
        Измерение скорости работы Алгоритма merge_sort
        """
        m_list = list_values  # 3.2425225999904796
        start_ = time.perf_counter()
        m_sort(m_list)
        time_list.append(time.perf_counter() - start_)
        print(m_list)


    def b_sorta(list_values: list):
        """
        Измерение скорости работы Алгоритма bubble_sort
        """
        b_list = list_values  # Не дождался =(
        start_ = time.perf_counter()
        b_sort(b_list)
        time_list.append(time.perf_counter() - start_)
        print(b_list)

    q_sorta(list_of_values)
    m_sorta(list_of_values)
    b_sorta(list_of_values)

    print(time_list)
