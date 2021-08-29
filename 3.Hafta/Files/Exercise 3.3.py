"""
Size bir dosya adı soran, ardından bu dosyayı açan ve dosyanın satırlarını arayarak dosya içini okuyan bir kod verildi. Sizden istediğimiz, “X-DSPAM-Confidence: ” değerlerinin ortalamasını bulmanız. Örnek bir satır:
X-DSPAM-Confidence: 0,8475

Ardından aşağıda gösterildiği gibi bir çıktı oluşturun. Çözümünüzde sum() fonksiyonunu veya sum adlı bir değişken kullanmayın.


İstenilen Çıktı:
Ortalama X-DSPAM-Confidence: 0,7507185185185187
"""
# Dosya adı olarak mbox-short.txt dosya adını kullanın

fname = "mbox-short.txt"
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    fnum = line.find(":")
    num = line[fnum+1:]
    num = float(num)
    count = count + 1
    tot = tot + num
print("Average of X-DSPAM-Confidence:", tot/count)
