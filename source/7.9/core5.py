#!/usr/bin/python -O

'''
Mass Executer.
This program is an initiative of the Unix computer ITO Automation.
Autor: Anibal G. Vindas <anibal@hp.com>
'''

#Importing from standart libraries:
import paramiko
import getpass
import os, sys, time, signal
import getopt

#Importing from local libraries and local files:
from usage import * 
from log import logger
from interrupter import *
from commander import *
from user import *
from server_error import *

l_userpassword1 = ""
l_userpassword2 = ""
#l_username = os.getlogin()

log_file = "/tmp/massexec.log" #Path of the log file.

last_int = 0
last_ev = False
s_last = ""

fail_t = False

total_servers = 0

com = ""
iteration = 0

real_password = ""
############ Versions #################

#######################################

server_list_path = "./servers.lst"
server = ""
out = "/tmp/massexec"
valid_init = True
os.system('clear')
 
##############################################
		
######### Function Commands introducer #############

def command_introducer(commands_array,s,ssh,d):
	global real_password
	'''
	This function introduce every command in commands_array
	to the line ssh.exec_command()
	Also it cleans and checks the command before introduce it.
	'''
	c = 1
	for commands_i in commands_array:
		#This loop is only to clean the command line.
		commands_i = commands_i.strip()
		print ("Analizing command line: \n"+commands_i+"\n")


	#If the command includes the code 7PASSWD7, it means that the last
	#success pasword must be introduced after the current command.
	#This section is not working, yet.

		if commands_i.find('7PASSWD7') > 0:
			print ("Begining SUDO block")
			#After to detect the code 7PASSWD7, it removes it.
			com = commands_i.replace('7PASSWD7','').strip()
			print ("Introducing [root/sudo] command "+com)
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(com)
			print (ssh_stdout.readlines()+ssh_stderr.readlines())
			if len(real_password) == 0:
				print ("\nThere is not password typed!")
				print ("You should run this script again and type the password when prompted.")
			else:
				print("Delaying one second...")
				time.sleep(1)
				print ("Introducing last successful password...("+real_password[0:4]+"*****)")
									#ssh_stdin.write(real_password+'\n\n')
				#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(real_password+'\n\n')
				sys.stdin.write(real_password+'\n\n')
				output = ssh_stdout.readlines() + ssh_stderr.readlines()
				print (output)
			sys.stdin.flush()
			print ("End of SUDO block")
		else:
			print "\nIntroducing command: "+commands_i
			#Line below executes the command introduced:
			ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(commands_i)
			time.sleep(1.5)
			output = ssh_stderr.readlines() + ssh_stdout.readlines()
			print (output)
		print "Command executed."

		#d is a list (array) where every element is a command line, 
		#error output and command output:

		d.append('\n'+commands_i+'\n')
		#d = d + ssh_stdout.readlines() + output
		d.append(output)
		d.append('\n')
		print d
		c = c + 1
	return d



##########Function to access server###################

def access_server(s,c = "uname -a"):
	global commands , report_f 
	global commands_array
	global real_password

	data = []
	commands_array = command_fixer(c)
	
	int_text = """\n 
				======================================================
				==== Program PAUSED ==================================
				======================================================
				=== To stop the program press x <ENTER> 
				=== Or press any key <ENTER> to continue
				======================================================
"""
	
	fail = False
	s = s.strip()
	print "Connecting to server "+s+"..."
	
	#Start the object SSH.

	ssh = paramiko.SSHClient()

	#To use the sshkey automaticaly.
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	#This list stores the standart error and output.
	d = []

	#This line is for debugging only. It must be commented when run production.
	paramiko.util.log_to_file('ssh_exec_cmd.log')


	try:
		#Line below starts a ssh sesion in the server:
		ssh.connect(s, username = l_username, password = l_userpassword1,timeout='10')
		logger(s,c,l_username)
		oo = "Access to "+s+" successful as "+l_username+" with first password.\n"
		print (oo)
		report_f.write(oo)
		real_password = l_userpassword1 
		d = command_introducer(commands_array,s,ssh,d)

		ssh.close()
		fail = False

		if l_userpassword1.strip() == "": fail = False

	except KeyboardInterrupt:
		os.system('clear')
		print int_text
		
		interrupper()

	except paramiko.SSHException:
		oo = "SSH error in first connection for server "+s
		print (oo)
		report_f.write(oo)
		if l_userpassword1.strip() == "": fail = False
		fail = True
 
		if (fail):
			oo = "Trying second password for server "+s+" \n"
			print (oo)
			report_f.write(oo)

			try:
				#Line below starts a ssh sesion in the server:
				ssh.connect(s, username = l_username, password = l_userpassword2,timeout='10')

				logger(s,c,l_username)

				oo = "Access to "+s+" successful as "+l_username+" with another password.\n"

				real_password = l_userpassword2

				print (oo)
				report_f.write(oo)
				
				d = command_introducer(commands_array,s,ssh,d)

				ssh.close()
				fail = False
				
			except KeyboardInterrupt:
				os.system('clear')
				print int_text
				interrupper()

			except paramiko.AuthenticationException:
				oo = "=!! Authentication error connecting server "+s+" !!="
				print (oo)
				report_f.write(oo)
				#Storing server in failed list:
				failed_servers.append_error(s+"\tAuthentication error.")
				
				fail = True


			except paramiko.SSHException:
				oo = "SSH error connecting server "+s
				print (oo)
				report_f.write(oo)
				fail = True

			except Exception:
				oo = "Server "+s+" was not accessed. \n"
				print (oo)
				report_f.write(oo)
				fail = True
	

	except:
		oo = "=!! Error server "+s+" is unkown. !!="
		print (oo)
		report_f.write(oo)
		#Storing server in failed list:
		failed_servers.append_error(s+"\tUnkown server.")

	return d


############### Function to access the server list ###########

def get_servers(sl):
	global total_servers

	server_list = open(sl, 'r')
	servernames = server_list.readlines()
	server_list.close()

	total_servers = len(servernames)

	return servernames
 

################################################################

os.system('clear')
print welcome()

'''

Checking the options with use()
initializating com and server_list_path variables.
server_list_path has a default value of "./servers.lst"

'''

valid_init,com,server_list_path,out = use()

if not valid_init:
	sys.exit()

else:
	if server_list_path.strip() == "": server_list_path = "./servers.lst"


l_username , l_userpassword1 , l_userpassword2 = get_user()
print ("Log file "+out)
report_f = open(out, 'a',0)
	
# List of failed servers is raised here.
failed_servers = s_error(out)
print("Servers failed are going to be stored in the file showed adove.")
time.sleep(2)

separator1 = "\n "+"="*10+" \033[1m "
separator2 = " \033[m "+"="*10+" \n"

for server in get_servers(server_list_path):
	server = server.strip()

	if server == "" or server[0] == "#": 
		iteration = iteration + 1
		continue

	iteration = iteration + 1

	report_f.write("\n"+"="*10+" "+server.strip()+" - "+str(iteration)+" "+"="*10+"\n")
	print separator1+server.strip()+" - "+str(iteration)+" of "+ str(total_servers)+separator2
	
	server_output = access_server(server,com)
	
	print ('\n')
	
	for l in range(len(server_output)):
		#line = server_output[l].strip()
		line = server_output[l]
		print (line)
		report_f.write(line)
		report_f.write('\n')
 

report_f.close()
failed_servers.close_error()

print ("\n\n")

