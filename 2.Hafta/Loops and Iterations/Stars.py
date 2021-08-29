"""
Bu alıştırmada, belirli sayıda satır verildiğinde bir yıldız üçgeni oluşturabilecek bir dize(string) döndürmelisiniz:
Misal:
Girilen Sayı: 3
Çıktı:
*

* *

* * *
İpucu: Bir alt satıra geçmek için "\n" ifadesini kullanın.
"""

r = input("Enter a number:")
rows = int(r)
def star(rows):
    for rows in range(rows+1):
        print("*" * rows + "\n")
star(rows)
