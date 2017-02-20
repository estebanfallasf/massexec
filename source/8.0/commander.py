import os

def command_fixer(comm):
  '''
  This function checks the -c argument in order to identify if it is a file
  or a single command line.
  '''
  comm = comm.strip()
  if os.path.isfile(comm):
    print "Reading "+comm+ " file... Ok"
    comm_f = open(comm, 'r')
    comm_list = comm_f.readlines()
    comm_f.close()
  else:
    comm_list = comm.split(';')
    print ("Commands to execute:")
    print (comm_list)
    print ("\n\n")
    #Every command must be cleaned.
    c = comm_list
    for i in range(len(comm_list)):
       comm_list[i] = comm_list[i].strip()

  return comm_list


#print command_fixer("uname -n")
