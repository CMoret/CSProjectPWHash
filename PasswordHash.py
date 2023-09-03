#PasswordHash
#This program hashes a password of choice
import bcrypt

#password used
password = b'Hello World'

#salts the password
salt = bcrypt.gensalt()

#hashes the password
hasher = bcrypt.hashpw(password,salt)

#prints out hash
print('Your password hashed is: ')
print(hasher)
