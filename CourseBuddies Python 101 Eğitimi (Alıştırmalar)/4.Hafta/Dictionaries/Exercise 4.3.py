"""
mbox-short.txt dosyasını okumak için bir program yazın ve en çok e-posta mesajını kimin gönderdiğini bulun .
Program ‘From’ satırlarını arar ve bu satırların ikinci kelimesini postayı gönderen kişi olarak alır.
Program, gönderenin posta adresini dosyada görünme sayısı ile eşleyen bir Python sözlüğü oluşturur.
Sözlük oluşturulduktan sonra program, en üretken kaydediciyi bulmak için maksimum döngü kullanarak sözlükten okur.
"""

name = input("Enter file:")
if len(name) < 1 : 
    name = "mbox-short.txt"
handle = open(name)
count = dict()
hlist = list()
for line in handle:
    if line.startswith("From"):
        hList=line.split()
        count[hList[1]] = count.get(hList[1],0) + 1
for i in count:
    if count[i] == max(count.values()):
        print("Most Repeated Mail:",i,max(count.values()),"times")
