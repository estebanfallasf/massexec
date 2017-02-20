import signal, os, sys

def skipper(signum,frame):
   print "Press x to exit now"

def interrupper():
    '''
    This function listen for the user interruption.
    '''
    
    try:
        user_key = raw_input()
        user_key = user_key.strip()
        if (user_key == 'x'):
            print "Skipping and exiting..."
            sys.exit()
        else:
            print "Skipping to next server."
        
    except KeyboardInterrupt:
            print "Exiting..."
            sys.exit()
