#This program hashes a password of choice
import bcrypt

#password used
password = b'Hello World'

#salt generator
salt = bcrypt.gensalt()

#hashes password
hasher = bcrypt.hashpw(password,salt)

print('Your password hashed is: ')
print(hasher)