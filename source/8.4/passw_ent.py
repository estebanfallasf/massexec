#!/usr/bin/python

class pass_password:
	'''
	1 - Set counter initially in cero: c = 0. Also get the global current password, first password and second password

	'''
	#1:
	c = 0
	passwords = []

	def __init__(self,c_pass,pass_1,pass_2):
		self.c_pass = c_pass
		self.pass_1 = pass_1
		self.pass_2 = pass_2
		self.password = [c_pass,pass_1,pass_2]
		print(pass_2)


