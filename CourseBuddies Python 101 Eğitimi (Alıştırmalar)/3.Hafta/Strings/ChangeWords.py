"""
Bu alıştırmada size iki kelimeden oluşan bir string(dize) veriliyor.
Bu iki kelimenin değiştirildiği bir string(dize) döndürmeniz gerekir.
"""
def switch_words(phrase):
    nphrase = phrase.split()
    if len(nphrase)>2:
        print("Please enter only 2 words!")
    elif len(nphrase)<2:
        print("Please enter only 2 words!")
    else:
        print(nphrase[-1],nphrase[-2])
print("EXAMPLE:")
switch_words("Golden Bear")
switch_words("day snow")
print("YOUR TURN!")
word = input("Enter 2 words: ")
switch_words(word)
