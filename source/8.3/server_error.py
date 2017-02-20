import os


class s_error:
	'''
	Date: January 22 2011
	Author: A. G. Vindas
	'''

	def __init__(self,f) :
		'''
		
		This library is a helper to store the error messages related to server error
		in a file, named "<output_file>.err"
		
		This simple library gets two parameters:
		1-File name output
		2-String to write.
	
		'''
		self.f = f+".err"
		self.f_error = open(self.f,'a+')
		print("File "+self.f+" raised.")
		
	def append_error(self,s):
		self.f_error.write(s+"\n")
		self.f_error.flush()
		print "File "+self.f+" was updated.\n"
		return True

	def close_error(self):
		self.f_error.close()
		print "File "+self.f+" has been closed."
		return True


'''
f = "abc.txt"

c = s_error(f)
c.append_error("Prueba...")
c.append_error("Prueba...1")
c.append_error("Prueba...2")
c.close_error()

'''

