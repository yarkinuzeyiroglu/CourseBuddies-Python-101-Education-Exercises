"""
Tüm kullanıcı adlarını ve şifreleri takip eden users  adında sözlüğe dayanarak bir kullanıcı adı ve şifrenin doğru olup olmadığını kontrol eden bir fonksiyon yazın.
Fonksiyonunuz, verilen kullanıcı adı ve şifrenin doğru olup olmadığına bağlı olarak True veya False dönmelidir.
"""
def check_login(users, username, password):
    for key, val in users.items():
        if key == username and val==password:
            return True
    return False
    
users={"Hello":"bye", "a":"b", "no":"yes","x":"y"}
try: 
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print(check_login(users, username, password))
except:
    print("Please enter invalid value")
    quit()
