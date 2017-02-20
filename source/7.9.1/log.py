import sys, os
from time import localtime, strftime

def logger(ss,cc,ulog):
  '''
  This module stores the log information at log_file.
  Every command line executed successfully most be stored.
  
  '''
  print "Logger called"
  log_file = "/automation/massexec/massexec.log"
  if os.path.exists(log_file):
	f = open(log_file,'a')
	d = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
	f.write(d+" \t"+os.getlogin()+"\t->\t"+ulog+"\t"+ss+"\t\n"+cc+"\n\n")
	f.close()
  else:
	print "File "+log_file+" does not exists."
	sys.exit()
  
  return True

logger("abc","ls -l","anibalito")
