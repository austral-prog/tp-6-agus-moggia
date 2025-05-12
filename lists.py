def remove_elements(list_to_remove_elements):
    lenlist = len(list_to_remove_elements)

    if lenlist >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements

    elif lenlist == 5: 
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements

    elif lenlist <5 and lenlist>=1:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    else:
        return []


def add_elements(list_to_add_elements):
    list_to_add_elements.append('yellow')
    list_to_add_elements.insert(0,'Pink')
    return list_to_add_elements


def is_empty(list_to_check):
    if list_to_check==[]:
        return True 
    else: 
        return False


def check_lists(list_to_compare1, list_to_compare2):
   lista1==list_to_compare1
   lista2== list_to_compare2
   if len(lista1)>=3 and len(lista2)>=3:
    if lista1[2]==lista2[2]:
        Valor = True
    else:
        Valor = False
   else:
        Valor= False

        return Valor


#separo las listas para simplificar
def list_of_lists(list_of_lists_to_modify):
    list0= list_of_lists_to_modify[0]
    list1 = list_of_lists_to_modify[1]
    list2 = list_of_lists_to_modify[2]

    if len(list0)>2:
        list0_new = [list0[0], list0[1]]
    else:
        list0_new = list0

    len1 = len(list1)
    if len1 == 2:
        list1_new == [list1[1]]
    elif len1 == 3:
        list1_new == [list1[1], list1[2]]
    elif len1 >= 4: 
        list1_new = [list1[1], list1[2], list1[3]]
    else:
        list1_new = []

    len2 = len(list2)
    if len2 > 0:
        list2_new= list2[-2:]
    else:
        list2_new= []

    modified_list=[list0_new, list1_new, list2_new]


    return modified_list
