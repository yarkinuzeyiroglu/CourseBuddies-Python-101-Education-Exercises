"""
0.0 ile 1.0 arasında bir puan istemek için bir program yazın.
Puan aralık dışındaysa bir hata yazdırın.
Puan 0,0 ile 1,0 arasında ise, aşağıdaki tabloyu kullanarak bir harf notu yazdırın:
Puan		Not
> = 0,9		A
> = 0,8		B
> = 0,7 	C
> = 0,6 	D
<0,6 		F
Kullanıcı aralık dışında bir değer girerse, uygun hata mesajı ve çıkış( quit() ) yapın.
"""

print("Make sure the score you enter is between 0.0 and 1.0")
score = input("Enter Score: ")
try:
    s = float(score)
    if 1.0>=s>=0.9:
        print("Mark:A")
    elif 1.0>s>=0.8:
        print("Mark:B")
    elif 1.0>s>=0.7:
        print("Mark:C")
    elif 1.0>s>=0.6:
        print("Mark:D")
    elif 0.0<=s<0.6:
        print("Mark:F")
    else:
        print("The score you entered is outside the desired range")
except:
    print("Please enter a valid number!")
    quit()
