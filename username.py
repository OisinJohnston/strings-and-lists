username = input("Enter your name: ").lower()
if len(username)<5:
    username = (username + input("Enter your surname: ")).upper()
print(username)

    
