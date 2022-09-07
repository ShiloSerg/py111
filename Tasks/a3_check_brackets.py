def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    if len(brackets_row) == 0:
        return True
    if brackets_row[0] == ')':
        return False
    list_of_values = ['(', ')']
    counter = 0
    for value in brackets_row:
        if value not in list_of_values:
            return False
        if value == '(':
            counter += 1
        if value == ')':
            counter -= 1
    if counter == 0:
        return True
    else:
        return False
