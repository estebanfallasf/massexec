import getpass
import os, sys



def get_user():
  l_username = os.getlogin()
  pr = "Enter your username ["+l_username+"]: "
  print "Press Ctrl+C to exit."

  try:
    l_user = raw_input(pr)
    l_user = l_user.strip()
    if (l_user != ""):
        l_username = l_user
        print "Using login name "+l_username
    else:
        print l_username

  except KeyboardInterrupt:
        print "Exiting..."
        sys.exit()
  try:
        l_userpassword1 = getpass.getpass("Please introduce your password: ")
  except KeyboardInterrupt:
        print "Exiting..."
        sys.exit()
  try:
        l_userpassword2 = getpass.getpass("Please introduce alternative password: ")
  except KeyboardInterrupt:
        print "Exiting..."
        sys.exit()

  return l_username , l_userpassword1 , l_userpassword2


