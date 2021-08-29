"""


Fizikte, bir nesnenin sabit ivmeyle hareket ederken son hızını (veya hızını) bulmak için aşağıdaki denklem kullanılabilir:
vf = vi + at
burada:
vf= son hız
vi= ilk hız
a= hızlanma
t= zaman
İlk hız, ivme ve zaman verildiğinde, son hızı döndürecek bir fonksiyon yazın.
"""

def calculate_velocity(vi, a, t):
    vf = int(vi + a*t)
    print("Final velocity: " , vf)
vi = int(input("Enter initial velocity: "))
a =  int(input("Enter acceleration: "))
t = int(input("Enter time: "))
calculate_velocity(vi, a, t)
