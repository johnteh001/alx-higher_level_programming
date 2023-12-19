#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element 2 lists.

    Args:
        my_list_1: First list.
        my_list_2: Second list.
        list_length: Length of the new list.

    Returns:
        A new list with all divisions.
    """
    result = []

    for i in range(list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except (TypeError, ValueError):
            print("wrong type")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            result.append(quotient)

    return result
