"""
Bu egzersizde, size bir alışveriş listesi ve bir eşya verilecek. 
Eğer verilen eşya alışveriş listesinde ise True döndürün, alışveriş listesinde değilse False döndürün.
"""
def shopping_list(my_list, item):
    the_list = False
    for material in my_list:
        if material is item:
            the_list = True
    return the_list
    
s_list = ["milk","eggs","bread"]

print(shopping_list(s_list, "milk"))
print(shopping_list(s_list, "eggs"))
print(shopping_list(s_list, "bread"))
print(shopping_list(s_list, "jam"))
print(shopping_list(s_list, "olive"))
print(shopping_list(s_list, "cheese"))