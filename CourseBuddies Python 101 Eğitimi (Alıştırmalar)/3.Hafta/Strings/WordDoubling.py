"""
Bu egzersizde size 3 kelimelik bir dizi ve bu üç kelimeden birine karşılık gelen bir sayı verilecek. Verilen sayı sırasındaki kelimeyi iki kez yazdıran bir fonksiyon yazın.


double_word(“one two three”, 3) –> “one two three three”


double_word(“cat dog fish”, 2) –> “cat dog dog fish”

cat->1.sırada

dog->2.sırada

fish->3.sırada,

fonksiyonun ikinci girdisi 2 olduğu için, 2.sıradaki dog iki kez yazdırılmış.
"""
def double_word(phrase, ref):
    word = phrase.split()
    if ref == 1:
        print(word[0],word[0],word[1],word[2])
    elif ref == 2:
        print(word[0],word[1],word[1],word[2])
    elif ref == 3:
        print(word[0],word[1],word[2],word[2])
    else:
        print("Invalid value! Only 3 words can be entered!")
        
words = "cat dog fish"
double_word(words,1)
double_word(words,2)
double_word(words,3)
double_word(words,4)
double_word(words,-1)
print()
double_word("one two three",1)
double_word("one two three",2)
double_word("one two three",3)
double_word("one two three",4)
double_word("one two three",-1)
