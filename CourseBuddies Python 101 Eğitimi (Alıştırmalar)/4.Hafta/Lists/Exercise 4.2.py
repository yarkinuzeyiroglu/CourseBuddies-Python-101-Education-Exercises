"""
mbox-short.txt dosyasını açın ve satır satır okuyun. Aşağıdaki satır gibi ‘From’ ile başlayan bir satır bulduğunuzda:
From stephen.marquard@uct.ac.za Cmt 5 Ocak 09:14:16 2008

“From” satırını split () kullanarak ayrıştıracak ve satırdaki ikinci kelimeyi (yani mesajı gönderen kişinin tüm adresini) yazdıracaksınız. İşlemler tamamlandığında, yazdırdığınız kişi sayısını yazdıracaksınız.

İpucu: ‘From:’ ile başlayan satırların tamamını eklemediğinizden emin olun. Sadece gönderen ismini ekleyeceksiniz. Sayımın nasıl yazdırılacağını görmek için örnek çıktının son satırına da bakın.

Örnek verileri http://www.py4e.com/code3/mbox-short.txt adresinden indirebilirsiniz.
"""
fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"
fh = open(fname).readlines()
count = 0
for line in range(len(fh)):
    if fh[line].startswith("From:"):
        for words in fh[line].split():
            if "@" in words:
                count += 1
                print(count,":",words[:])
print("There were", count , "lines in the file with From as the first word")
