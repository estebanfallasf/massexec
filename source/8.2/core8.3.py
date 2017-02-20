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
from usage_20110425 import * 
from log import logger
from interrupter import *
from commander import *
from user_20110415 import * 
from server_error import *


###### Variables ##############################
l_userpassword1 = ""
l_userpassword2 = ""

log_file = "/tmp/massexec.log" #Path of the log file.

last_int = 0
last_ev = False
s_last = ""

fail_t = False

total_servers = 0
vortaro = "" #It stores the path of the dictionary file.
com = ""
iteration = 0

real_password = ""
server_list_path = "./servers.lst"
server = ""
out = "/tmp/massexec"
sudo = False
session_started = False

############################ Functions ########################
############ Versions #################
def Ver():
	version = "2011.04.24"
	updates = '''
Core optimized.
Output format improved.
Usage library improved:	'-d' flag accepted. Alse it is a class now.
			'-r' flag is accepted to introduce root when sudo command is executed.

	'''
	print("\nVersion: "+version)
	print("Comments: "+updates+"\n\n")

##############################################
		
######### Function Commands introducer #############

def command_introducer(commands_array,s,ssh,d):
	global real_password
	global session_started
	'''
	This function introduce every command in commands_array
	to the line ssh.exec_command()
	Also it cleans and checks the command before introduce it.
	'''
	session_started = True

	for commands_i in commands_array:
		#This loop is only to clean the command line.
		commands_i = commands_i.strip()

		print('\n')
		print("\nIntroducing command: "+commands_i)
		#Line below executes the command introduced:
		#And returns lists.
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(commands_i)
		time.sleep(1)
		#print(ssh_stderr.channel.closed)
		#print(ssh_stdout.channel.closed)
		if ssh_stdout.channel.closed is False and ssh_stderr.channel.closed is False: 
			if sudo is True:
				print("Shell is waiting for Standard Input and '-r' flag is active.") 
				ssh_stdin.write('%s\n' % real_password)
				print("Last password introduced.")

				#ssh_stdout.channel is still closed
				if ssh_stdout.channel.closed is False:
					time.sleep(1)
					print("Shell is still waiting for Standard Input and '-r' flag is active.")
					print("Trying second password: "+l_userpassword2[0:3]+'****')
					ssh_stdin.write('%s\n' % l_userpassword2)
					time.sleep(1)
					ssh_stdin.write('\n') #Sending two 'Enter' 
					time.sleep(1)
					ssh_stdin.write('\n')
					#ssh_stdin.flush()
					print("Done")
			else:
				print("'-r' flag is not active.")
				ssh_stdin.write('\n') #Sending two 'Enter'
				time.sleep(1)
				ssh_stdin.write('\n')
				time.sleep(1)
				ssh_stdin.write('\n')

			#ssh_stdin.flush()

		output = ssh_stderr.readlines() + ssh_stdout.readlines()
		output_2 = []
		for ox in output:
			#Printing in the standart/error output.
			ox = ox.strip()
			print (ox)
			#Cleaning the lines to avoid double '\n'
			output_2.append(ox)

			#Here is necessary to check the output system to use the dictionary:
			if vortaro != "":
				print("Dictionary function is required!")
				#print("Line to search: "+ox)

		print "Command executed.\n"

		#d is a list (array) where every element is a command line, 
		#error output and command output:

		d.append('\n'+commands_i+'\n')
		d.extend(output_2)
		d.extend(ssh_stdout.readlines())
		#d.extend(ssh_stdout.readlines())
		d.append('\n')
		d.append('------------------------------------')
	return d



##########Function to access server###################

def access_server(s,c = "uname -a"):
	global commands , report_f 
	global commands_array
	global real_password
	global session_started

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
	print "Connecting to server "+s+" as "+l_username
	
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
		oo = "SSH error in first connection for server "+s+"\n"
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
		                if session_started is True:
                		        oo = "=!! Error during the session. !!="
                        		#Storing server in failed list:
                        		failed_servers.append_error(s+"\tSession error.")
                		else:
					oo = "Server "+s+" was not accessed. \n"
                        		#Storing server in failed list:
                        		failed_servers.append_error(s+"\tUnkown server.")

                		print (oo)
                		report_f.write(oo)
                		session_started = False
				fail = True
	
	except:
		if session_started is True:
			oo = "=!! Error during the session. !!="
			#Storing server in failed list:
			failed_servers.append_error(s+"\tSession error.")
		else:
			oo = "=!! Error server "+s+" is unkown. !!="
			#Storing server in failed list:
			failed_servers.append_error(s+"\tUnkown server.")

		print (oo)
		report_f.write(oo)
		session_started = False

	return d


############### Function to access the server list ###########

def get_servers(sl):
	global total_servers

	server_list = open(sl, 'r')
	servernames = server_list.readlines()
	server_list.close()
	total_servers = len(servernames)

	return servernames
 

############################  Start  ####################################

os.system('clear')
print("Starting...")
#print welcome() #It is replaced for the function of the usage class.
#Loading usage class :
usage = useClass()
print(usage.welcome())


Ver()

'''

Checking the options with use()
initializating com and server_list_path variables.
server_list_path has a default value of "./servers.lst"

'''
#Getting option and arguments:
#valid_init,com,server_list_path,out,vortaro = use() # New usage class replace this line:

#If option not valid exits. Some of thoses checks could be deleted, because usage module performed it.
if not usage.use():
	sys.exit()
else:
	com = usage.com_
	server_list_path = usage.servers_
	out = usage.out_file
	vortaro = usage.vort
	sudo = usage.sudo
#It was removed, because new usage module performs this task.
#else:
#	if server_list_path.strip() == "": server_list_path = "./servers.lst"
#l_username , l_userpassword1 , l_userpassword2 = get_user() #New user class replaced this line.
print("Calling userClass")
u = userClass()
if u.get_user():
	l_username = u.l_username
	l_userpassword1 = u.l_userpassword1
	l_userpassword2 = u.l_userpassword2
else:
	sys.exit()


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
		report_f.write(line)
		report_f.write('\n')
 

report_f.close()
failed_servers.close_error()

print ("\n\n")

