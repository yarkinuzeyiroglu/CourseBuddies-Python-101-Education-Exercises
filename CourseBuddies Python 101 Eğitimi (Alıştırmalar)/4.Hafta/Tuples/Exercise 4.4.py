"""
mbox-short.txt dosyasını okumak için bir program yazın ve her mesaj için günün saatine göre dağılımı hesaplayın. Saati bularak ve ardından iki nokta üst üste kullanarak dizeyi ikinci kez bölerek saati ‘Başlangıç’ satırından çıkarabilirsiniz.


Her saat için sayıları biriktirdikten sonra, aşağıda gösterildiği gibi saate göre sıralanmış sayımları yazdırın.


Gönderen stephen.marquard@uct.ac.za Cmt 5 Ocak 09 : 14: 16 2008


"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
lst = list()
for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        hour = words[5].split(":")
        count[hour[0]] = count.get(hour[0],0) + 1
        continue
for k,v in count.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print(k,v)
