"""
Brüt ücreti hesaplamak için input() kullanarak kullanıcıdan çalışma saati alın.
40 saate kadar, her saat başına ücret 10 TL dir. 40 saatin üstündeki saatlerin ücreti 15 TL olmaktadır.
Girilen saate göre ücreti hesaplayan bir kod yazınız.
Test etmek için 30 saat değerini giriniz, sonuç 300 TL çıkmalı, ikincil test olarak 50 değerini giriniz, sonuç 550 TL çıkmalı.
"""

hrs = input("Enter Hours:")
h = float(hrs)
if h<=40:
    print("Salary:" , h*10)
else:
    r= ((h-40)*15) + 400
    print("Salary:" , r)
