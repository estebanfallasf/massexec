import getpass
import os, sys


class userClass:
	l_username = ""
	l_userpassword1 = ""
	l_userpassword2 = ""
	
	def get_user(self):
		self.l_username = os.getlogin()
		pr = "Enter your username ["+self.l_username+"]: "
		print("press ctrl+c to exit.")
	
		try:
			l_user = raw_input(pr)
			l_user = l_user.strip()
			if (l_user != ""):
				self.l_username = l_user
				print("Using login name "+self.l_username)
			else:
				print(self.l_username)
	
		except KeyboardInterrupt:
			print("Exiting...")
			return False
		try:
			self.l_userpassword1 = getpass.getpass("Please introduce your password: ")
		except KeyboardInterrupt:
			print("Exiting...")
			return False
			
		try:
			self.l_userpassword2 = getpass.getpass("Please introduce alternative password: ")
		except KeyboardInterrupt:
			print("Exiting...")
			return False
	
		return True
	
'''
u = userClass()
u.get_user()

print("Hola "+u.l_username)
'''

