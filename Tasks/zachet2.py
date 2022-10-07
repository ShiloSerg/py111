from collections import Counter


dna_strs = [
    ['A', 'T', 'T', 'A'],
    ['A', 'C', 'T', 'A'],
    ['A', 'G', 'C', 'A'],
    ['A', 'C', 'A', 'A'],
             ]


def DNA(some_strs: list) -> str:
    """
    Задача консенсуса DNA ридов
    """
    # some_strs_len = len(some_strs)
    dict_values = {key: [] for key in range(len(some_strs))}
    for list_ in some_strs:
        for ind, value in enumerate(list_):
            dict_values[ind].append(value)

    result = ""
    for value in dict_values.values():
        c = Counter(value)
        values = dict(c)
        sorted_key_values = dict(sorted(values.items(), key=lambda item: item[1]))
        max_value = list(sorted_key_values.keys())
        result += "".join(max_value[-1])
    print(result)
    return result


if __name__ == '__main__':
    DNA(dna_strs)