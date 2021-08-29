"""
Kullanıcı ‘done’ ifadesini girene kadar bir kullanıcıdan sürekli olarak tamsayı sayıları isteyen bir program yazın. 
‘done’ girildikten sonra, sayıların en büyük ve en küçüğünü yazdırın. 
Kullanıcı geçerli bir numaradan başka bir şey girerse, onu bir try/except yardımı ile yakalayın ve uygun bir mesaj yazdırın. 
"""
largest = None
smallest = None
while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            num = int(num)
        except:
            print("Invalid number!")
            continue
        if largest == None and smallest == None:
            largest = num
            smallest = num
            
        if largest < num:
            largest = num
            
        if smallest > num:
            smallest = num
            
print('Smallest Number:', smallest)
print('Largest Number:', largest)

