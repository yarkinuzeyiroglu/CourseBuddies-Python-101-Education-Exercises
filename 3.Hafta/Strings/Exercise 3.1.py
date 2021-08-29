"""
Aşağıdaki satırın sonundaki sayıyı çıkarmak için find () ve dizi dilimlemeyi (bkz. Bölüm 6.10) kullanarak kod yazın.
Çıkarılan değeri ondalıklı sayıya dönüştürün ve yazdırın.
"""
text = "X-DSPAM-Confidence:    0.8475";
num = text.find(".")
nnum = text[num-1:]
nnum = float(nnum)
print("Number:",nnum)
print("Proof that is float number:",type(nnum))
