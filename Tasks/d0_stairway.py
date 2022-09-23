from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    stairway = list(stairway)
    list_of_min_values = []
    while True:
        if len(stairway) == 0:
            print(list_of_min_values)
            print(sum(list_of_min_values))
            return sum(list_of_min_values)
        elif len(stairway) == 1:
            list_of_min_values.append(stairway[0])
            del stairway[0]
        elif stairway[0] < stairway[1]:
            list_of_min_values.append(stairway[0])
            del stairway[0]
        elif stairway[0] > stairway[1]:
            list_of_min_values.append(stairway[1])
            del stairway[1]
            del stairway[0]
        else:
            if stairway[0] == stairway[1]:
                list_of_min_values.append(stairway[1])
                del stairway[1]
                del stairway[0]

    # print(get_coast(6))

