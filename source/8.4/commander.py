import os

def command_fixer(comm):
	'''
	This function checks the -c argument in order to identify if it is a file
	or a single command line.
	'''
	dot_comma = "#dot_comma#;"
	comm = comm.strip()
	if os.path.isfile(comm):
		print "Reading "+comm+ " file... Ok"
		comm_f = open(comm, 'r')
		comm_list = comm_f.readlines()
		comm_f.close()
	else:
	#If the -c contents a list of commands sepated by ';'
	#It is necessary to identify '\;':
		#print(comm)
		comm = comm.replace('\;',dot_comma)
		comm_list = comm.split(';')

	#Every command must be cleaned. Also dot_comma must be returned to "\;"
	for i in range(len(comm_list)):
		#print(comm_list[i])
		comm_list[i] = comm_list[i].replace('#dot_comma#','\;')
		comm_list[i] = comm_list[i].strip()
		#print(comm_list[i])

	print("Commands to execute:")
	print(comm_list)
	return comm_list


