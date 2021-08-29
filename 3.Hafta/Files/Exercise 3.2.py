"""
Words.txt adlı dosyayı açın, dosyayı okuyun ve dosyanın içeriğini büyük harfle yazdırın.
Çıktıyı üretmek için words.txt dosyasını kullanın.
"""
# Dosya adı olarak words.txt kullanın.

filename = "words.txt"
fh = open(filename)
read_file = fh.read()
print(read_file.upper())
