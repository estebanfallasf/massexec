#!/usr/bin/python
'''
Description: 	This module is used to explain the usage of the flags to the user.
Author:		Anibal G. Vindas <anibal@hp.com>
Date:		2011.04.14
Comment: 	This new version does not have the flag '-v | --version', because that legend is included in the core script.
		Also the flag '-d' was created in order to pass a dictionary path file.

'''
import os, sys, getopt
from stat import *

def use():

	com_ = ""
	servers_ = ""
	out_file = ""
	vort = ""
	arguments_ar = ['-s','-o','-c'] # Mandatory flags

	howto = """
Usage:
	core.py 
	[-h] [--help] To print this message. 
	[-d <dictionary file>] This flag is optional, but a dictionary file must be included when use it. 
	-s <server list path> This file is mandatory. It must be a list of servers.
	-c <commands string | Text file containing  commands> It is mandatory. A string conteining the commands separeted by ';' must be included.
		Or a path of the file with the commands.
	-o <output file> Mandatory flag with the output report. If the file already exists it will be appended.
"""
   
	#Checking if all the flags were introduced.
	for ar in arguments_ar:
		if not ar in sys.argv:
			print howto
			print("Warning: \nArgument '"+ar+"' not found.\n")
			sys.exit()
   
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hc:s:o:d:", ["help"])

	except getopt.GetoptError, err:
		print str(err) # It'll print something like "option -a not recognized"
		print howto
		sys.exit()



	for o, a in opts:
		#print(o)

		if o in ("-h", "--help"):
			print howto
			sys.exit()

		elif o in ("-d"):
			a = a.strip()
			vort = a
			if not os.path.exists(a):
				print(howto)
				print("Warning:\n\t-d option needs a valid file path.")
				sys.exit()

		elif o in ("-c"):
			a = a.strip()
			com_ = a
			if len(a) < 2:
				print howto
				print "Warning:\n\t-c option cannot be empty or less than two characters."
				sys.exit()

 		elif o in ("-o"):
			a = a.strip()
			out_file = a
			if len(a) < 3 or a == "":
				print(howto)
				print "-o option needs a valid file path. Also argument must has more than 3 characters."
				return False

		elif o in ("-s"):
			a = a.strip()
			if len(a) < 3 or not os.path.exists(a):
           			print(howto)
				print "-s option needs a valid file path."
				sys.exit()
			else:
				servers_ = a

		else:
			assert False, "unhandled option"
			return False

	return True, com_ , servers_ , out_file, vort


def welcome():
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


print welcome()
use()
