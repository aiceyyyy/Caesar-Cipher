print("Welcome to Caesar Cipher machine!")
ed_choice = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt.\n")
key = int(input("Type your shift key (positive value): "))
word = input(f"Type your word to {ed_choice}: ")
result = ''

def engine(key):
    global result
    for x in word:
        if x.isalpha():

            ascii_x = ord(x)
            ascii_x += key%26

            if x.isupper():
                if ascii_x > 90:
                    ascii_x -= 26
                elif ascii_x < 65:
                    ascii_x += 26
            else:
                if ascii_x > 122:
                    ascii_x -= 26
                elif ascii_x < 97:
                    ascii_x += 26
                    
            result += chr(ascii_x)
        else: 
            result += x
    
if ed_choice == 'encrypt':
    engine(key)
    print(f'Your message is: {result}')
else:
    engine(key * -1)
    print(f'Your message is: {result}')