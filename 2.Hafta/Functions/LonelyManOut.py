"""
Çok sayıda insanı ve çok sayıda grubu alan bir fonksiyon yazın.
Kişiler gruplara eşit olarak bölünecektir (fazla kişiler olabilir).
Çift grupları oluşturduktan sonra kalan kişi sayısını döndürür.
"""

def left_over(num_people, num_groups):
    if num_groups * 2 >= num_people and num_people % 2 == 0:
        return 0
    elif num_groups * 2 >= num_people and num_people % 2 == 1:
        return 1
    else:
        return num_people - num_groups * 2
num_people =  int(input("Enter people number:"))
num_groups = int(input("Enter group number:"))
if num_people < 0 or num_groups < 0:
    print("Invalid value! Try Again.")
    quit()
print(left_over(num_people, num_groups), "person/people left alone.")
