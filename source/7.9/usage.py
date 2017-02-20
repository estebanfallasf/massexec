#!/usr/bin/python

import os, sys, getopt
from stat import *

def use():

   com_ = ""
   servers_ = ""
   out_file = ""
   
   arguments_ar = ['-s','-o','-c']

   howto = """
	Usage:
		core.py [-h] [--help] [-v][--version] -s <server list path> -c <commands string> -o <output file> """
   
   #Checking if all the flags were introduced.
   for ar in arguments_ar:
      if not ar in sys.argv:
         print howto
         print "Argument '"+ar+"' not found.\n"
         sys.exit()
   
   try:
      opts, args = getopt.getopt(sys.argv[1:], "hvc:s:o:", ["help", "version"])
      
   except getopt.GetoptError, err:
      print str(err) # will print something like "option -a not recognized"
      print howto
      #return False
      sys.exit()

   for o, a in opts:

      if o in ("-h", "--help"):
        print howto
        sys.exit()

      elif o in ("-c"):
        com_ = a.strip()
        if com_ == "":
           print howto
           print "-c option needs a valid command string."
           return False

      elif o in ("-o"):
        out_file = a.strip()
        if out_file == "":
           print howto
           print "-o option needs a valid file path."
           out_file = "default"
           return False

      elif o in ("-s"):
        a = a.strip()
        if a == "" or not os.path.exists(a):
           print howto
           print "-s option needs a valid file path."
           servers_ = "default"
           sys.exit()
        else:
         servers_ = a

      else:
        assert False, "unhandled option"
        return False

   return True, com_ , servers_ , out_file


def welcome():
    sep = "####################################################"
    msg = "          "+sep + """
          Welcome to Mass Executer.
          This program can help you to execute command lines massively.
                """+sep+""""
          This program is an initiative of the Unix computer ITO Automation.
          Any concern or help is going to be welcomed.
                """+sep+"""
          See the instructions using the option '-h'
        """

    return msg



