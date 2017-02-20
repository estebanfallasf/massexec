#!/usr/bin/python
'''
Description:	This module is used to explain the usage of the flags to the user.
Author:		Anibal G. Vindas <anibal@hp.com>
Date:		2011.04.14
Comment:	This new version does not have the flag '-v | --version', because that legend is included in the core script.
		Also the flag '-d' was created in order to pass a dictionary path file.

'''
import os, sys, getopt
from stat import *


class useClass:
	'''
	Description:	This module is used to explain the usage of the flags to the user.
	Author:		Anibal G. Vindas <anibal@hp.com>
	Date:		2011.05.26
	Comment:	This new version does not have the flag '-v | --version', because that legend is included in the core script. Also the flag '-d' was created in order to pass a dictionary path file.
	'''
	
	msg = ''
	com_ = ''
	server_list  = ''
	total_servers = 0
	out_file = ''
	vort = ''
	sudo = False
	ver = False
	debug = False
	arguments_ar = ['-s','-o','-c'] # Mandatory flags
	
	def welcome(self):
		sep = "\t####################################################"
		msg = sep + """
		Welcome to Mass Executer.
		This program can help you to execute command lines massively.
"""+sep+"""
		This program is an initiative of the Unix computer ITO Automation.
		Any concern or help is going to be welcomed.
"""+sep+"""
		See the instructions using the option '-h'
"""+sep+"\n\n"
		return msg

	def use(self):
		arguments_ar = ['-s','-o','-c'] # Mandatory flags
		howto = """
	Usage:
		core.py 
		[-h] [--help] To print this message. 
		[-d <dictionary file>] This flag is optional, but a dictionary file must be included when use it. NOT AVAILABLE, YET.
		[-v] To see version comments and logs.
		[-b] Saves the program log in file "debug_file". Used only to debug.
		-s <server list path> This file is mandatory. It must be a list of servers.
		-c <commands string | Text file containing  commands> It is mandatory. A string conteining the commands separeted by ';' must be included.
			Or a path of the file with the commands.
		-o <output file> Mandatory flag with the output report. If the file already exists it will be appended.
		-r Introduces password every time system is waiting for user entry.
	"""

		#Checking if all the flags were introduced.
		for ar in arguments_ar:
			if not ar in sys.argv:
				print(howto)
				print("Warning: \nArgument '"+ar+"' not found.\n")
				sys.exit()
		
		try:
			opts, args = getopt.getopt(sys.argv[1:], "hbrvc:s:o:d:", ["help"])
	
		except getopt.GetoptError, err: #Changed to Python v3
		#except getopt.GetoptError as err:
			print(str(err)) # It'll print something like "option -a not recognized"
			print(howto)
			sys.exit()

		for o, a in opts:
			if o in ("-h", "--help"):
				print(howto)
				sys.exit()
	
			elif o in ('-r'):
				a = a.strip()
				self.sudo = True
				
			elif o in ("-d"):
				a = a.strip()
				self.vort = a
				if not os.path.exists(a):
					print(howto)
					print("Warning:\n\t-d option needs a valid file path.")
					sys.exit()
	
			elif o in ("-c"):
				a = a.strip()
				self.com_ = a
				if len(a) < 2:
					print(howto)
					print("Warning:\n\t-c option cannot be empty or less than two characters.")
					sys.exit()
			
			elif o in ("-v"):
				a = a.strip()
				self.ver = True
			
			elif o in ("-b"):
				a = a.strip()
				self.debug = True


			elif o in ("-o"):
				a = a.strip()
				self.out_file = a
				if len(a) < 3 or a == "":
					print(howto)
					print("-o option needs a valid file path. Also argument must has more than 3 characters.")
					return False

			elif o in ("-s"):
				'''
				This section check the file or the list introduced.
				case switch should work for this task.
				'''
				a = a.strip()

				if len(a) < 3:
					print(howto)
					print("-s option needs a valid file path.")
					sys.exit()
				elif os.path.isfile(a):
					sl = open(a, 'r')
					sx = sl.readlines()
					sn = []

					for s in sx:
						s = s.strip()
						if s != "" or s[0] != "#":
							sn.append(s)

					sl.close()
					self.total_servers = len(sn)
					self.server_list = sn

				elif a.find(';') >= 0:
					sn = a.split(';')
					self.server_list = sn
					self.total_servers = len(sn)
				else:
					print(howto)
					print("-s option needs a valid file path.")
					sys.exit()
			else:
				print(howto)
				assert False, "Unhandled option"
				return False
	
		return True

'''
u = useClass()
print(u.welcome())
u.use()
print(u.com_)
print(u.out_file)
print(u.vort)
print("Lista de servidores:")
print(u.server_list)
print("Total de servidores: ")
print(u.total_servers)
'''
