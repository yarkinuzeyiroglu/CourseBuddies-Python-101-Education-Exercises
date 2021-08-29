"""
Python’da, default(varsayılan) argümanları, fonksiyon tanımında girdilere değer atayarak belirleyebilirsiniz.
Eğer argümana bir girdi karşılık gelmezse, tanımlanan değer kullanılacaktır.
Eğer fonksiyona iki girdiyi de sağlarsanız, varsayılan argümanlar yerine iki girdi kullanılır.
Bir default argümanı olan ve onu döndüren bir fonksiyon yazın.
"""

def default(name = 'Tom' , surname = 'Hanks' , grade = 'Fifth'):
    return name + " " + surname + ' studies in ' + grade + ' grade.'

print(default("Andy","Gates","Seventh"))
print(default("Andy","Gates"))
print(default("Andy"))
