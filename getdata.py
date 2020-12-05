import sqlite3
import hashlib 
import getpass
from colorama import Fore


db = sqlite3.connect('auth.db')


name = input('Enter name : ').lower()
password = getpass.getpass('Enter password : ').lower()

pw = hashlib.md5(password.encode())



cr = db.cursor()

 
cr.execute(" SELECT * FROM my_profile WHERE name = '%s' " % name)




ls = cr.fetchone()

try:
	if ls[2] == pw.hexdigest():
		print(Fore.GREEN,'Your Login')
	else:
		print(Fore.RED,'Invalid name or password!')
except TypeError :
	print(Fore.RED,'Please enter properiate input ')