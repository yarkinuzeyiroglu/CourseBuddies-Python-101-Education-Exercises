"""
romeo.txt dosyasını açın ve satır satır okuyun. Her satırı, split() fonksiyonunu kullanarak satırı bir String listesine bölün .
Program bir kelime listesi oluşturmalıdır.
Her satırdaki her kelime için, kelimenin zaten listede olup olmadığını kontrol edin ve eğer listedeyse tekrar eklemeyin.
Program tamamlandığında, ortaya çıkan kelimeleri alfabetik sıraya göre sıralayın ve yazdırın.
"""

fname = input("Enter file name: ")
fh = open(fname).read().split()
lst = list()
for line in fh:
    if not line in lst:
        lst.append(line)
lst.sort()
print(lst)
for i in range(len(lst)):
    print(lst[i])
