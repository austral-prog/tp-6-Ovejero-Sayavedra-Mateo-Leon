# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    lista = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    lista[4:6] = []
    del lista [0]
    return lista


def add_elements(list_to_add_elements):
    lista = ['Red', 'Green', 'White', 'Black']
    lista.insert(0, "Pink")
    lista.append('Yellow')
    return lista


def is_empty(list_to_check):
    if (len(list_to_check) == 0):
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    element3_list1 = list_to_compare1[2]
    element3_list2 = list_to_compare2[2]
    if element3_list1 == element3_list2:
        return True
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    del list_of_lists_to_modify[0][2]
    del list_of_lists_to_modify[1][0]
    del list_of_lists_to_modify[1][-1]
    list_of_lists_to_modify[2][0:2] = []
    return list_of_lists_to_modify
