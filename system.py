import sqlite3
import hashlib 
import getpass
from colorama import Fore

db = sqlite3.connect('auth.db')


cr = db.cursor()

name = input('Enter Your Name : ')
firstname = input('Enter Your First name : ')
password = getpass.getpass('Enter password : ').lower()

# idetity = input('Enter Your idetity : ')
 
pw = hashlib.md5(password.encode())


ls = [name,firstname,pw.hexdigest()]


try:
	cr.execute('''
 	CREATE TABLE IF NOT EXISTS my_profile ( 
 	 
 	name text , firstname text ,password text ) ''')
except Exception as e:
	print('Error {0}'.format(e))
	 


cr.execute('''INSERT INTO my_profile (name,firstname,password) VALUES(?,?,?) ''',ls)

print(Fore.GREEN,'You Registre Sccessful')
db.commit()

db.close()

