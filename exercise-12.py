import random
import string

# Generate a password of size 12.
passwd_symbols = []
passwd_symbol_string = ''
chars = ''
passwd = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
passlen = 12
passwd_generate = "".join(random.sample(passwd, passlen))
assert isinstance(passwd_generate, object)
print passwd_generate


# Generate password by joining "size" number of characters
def passwd_gen(chars, size=12):
    global passwd_symbol_string
    return ''.join(random.choice(chars) for _ in range(size))


# Exclude some special characters from the password
for entries in string.punctuation:
    if entries not in ('~', '`', '{', '}', '[', ']', ':', ';', '(', ')', '.', ',', '|', '"', '\'', '\\', '^'):
        passwd_symbols.append(entries)

passwd_symbol_string = ''.join([sym for sym in passwd_symbols])

# Main Block
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + passwd_symbol_string
user_passlen = int(raw_input("Enter the length of your password : "))
if user_passlen <= 5:
    print("Password strength is : weak")
    print("Generated password is : " + passwd_gen(chars, size=user_passlen))
elif user_passlen > 5 and user_passlen < 12:
    print("Password strength is : medium")
    print("Generated password is : " + passwd_gen(chars, size=user_passlen))
else:
    print("Password strength is : strong")
    print("Generated password is : " + passwd_gen(chars, size=user_passlen))
