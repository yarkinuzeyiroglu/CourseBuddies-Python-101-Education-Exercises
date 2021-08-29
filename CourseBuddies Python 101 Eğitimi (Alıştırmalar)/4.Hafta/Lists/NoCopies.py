"""
Bir tamsayı listesi oluşturun ve bu listede tekrarlayan sayıları listeden kaldıran remove_duplicates adlı bir fonksiyon yazın.


Misal:

Girdi: remove_duplicates([2, 2, 1])


Çıktı: [1,2]
"""
def remove_duplicates(my_list):
    return list(set(my_list))
print(remove_duplicates([2, 2, 1]))
print(remove_duplicates([2, 3, 1]))
print(remove_duplicates([2, 2, 2]))
print(remove_duplicates([2, 1, 1]))
