def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
    if len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
    if len(list_to_remove_elements) >= 1:
        del list_to_remove_elements[0]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    list_to_add_elements.append('Yellow')
    return list_to_add_elements

def is_empty (list_to_check):
    if (len(list_to_check) == 0):
        return True
    else:
        return False
        
def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

def list_to_list(list_of_lists_to_modify):
    del list_of_lists_to_modify[0][2]    # Elimina 3 de [1, 2, 3]
    del list_of_lists_to_modify[1][0]    # Elimina 4 de [4, 5, 6, 7, 8]
    del list_of_lists_to_modify[1][-1]   # Elimina el último (8) de [5, 6, 7, 8]
    list_of_lists_to_modify[2][0:2] = [] # Elimina 9 de [9, 10, 11, 12]
    return list_of_lists_to_modify
