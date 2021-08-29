"""
İki listeyi bir sözlüğe eşleyen ve yeni sözlüğü döndüren bir işlev yazın.

Misal:

list1 = [1, 2, 3]

list2 = [8, 9, 10]

new_dictionary = {1:8 , 2:9 , 3:10}
"""
def two_list(list1, list2):
    dic = dict()
    for key in list1:
        dic[key] = list2[list1.index(key)]
    return dic
list1 = [1,2,3]
list2 = [8,9,10]
print(two_list(list1,list2))
