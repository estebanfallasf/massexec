#!/usr/bin/python
import sys, os
from time import localtime, strftime

class logger_class:
	'''
	Description:	This module is used to explain the usage of the flags to the user.
	Author:		Anibal G. Vindas <anibal@hp.com>
	Date:		2011.11.11
	Comment:	This new version is a class model and uses a erxternal configuration file (./massexec.conf)

	Compruebo que existe el archivo ./massexec.conf
	En ese archivo cada variable esta separada del contenido por un tab.
	luego leo linea por linea de ese archivo hasta encontrar "log_file"
	si lo encuentro tomo su contenido y lo cargo a la variable log_file
	'''

	'''
	"conf" variable must store the full path for configuration file.
	It is possible to use the local variable "pwd" to refer the current work directory.
	Do not include the path separator in the filename.
	'''
	pwd = os.path.dirname(os.path.realpath(__file__))+os.sep
	conf = pwd+"massexec.conf"
	log_file = "unknown"
	available = False

	def __init__(self):
		'''
		This function get the configuration file
		'''
		print("Checking the configuration file.")
		if not os.path.exists(self.conf):
			print("Configuration file ("+self.conf+") was not found!\n")
			self.available = False
		print("Configuration file <"+self.conf+"> was found.")
		f = open(self.conf, 'r')

		for l in f.readlines():
			i = l.split("\t")
			if i[0] == "log_file":
				self.log_file = i[1].strip()
				print("Log file is: "+self.log_file)
		f.close()
		self.available = True

	def logger(self,ss,cc,ulog):
		'''
		This function gets the log file. Then, it writes the blog.
		'''
		if not os.path.exists(self.log_file):
			print("File "+self.log_file+" <log_file> does not exists.")
			print("Please, check the log_file variable in the configuration file.")
			f = open(self.log_file, "w")
			f.close()
			print("But it was created.")
			return False

		f = open(self.log_file,'a')
		d = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
		f.write(d+" \t"+os.getlogin()+"\t->\t"+ulog+"\t"+ss+"\t\n"+cc+"\n\n")
		f.close()
		return True

'''
l = logger_class()
l.get_configuration()
l.logger("letrasticas.org","comando","algo")
'''
