def VersionLog():
	'''
Description:	This module is used to show the version comments.
Author:		Anibal G. Vindas <anibal@hp.com>
Date:		2011.05.26
Comment:	
	'''

	version = "8.5 - 2011.05.26"
	updates = '''
Core optimized.
8.3: commander library improved.
8.4: Usage library improved:
	'-d' flag accepted. Alse it is a class now.
	'-r' flag is accepted to introduce root when sudo command is executed.

8.5: Prompt shell is confirmed after login.
8.5: Version Log was retired from the core. New file ver_log was created.
8.5: Flag '-v' was include again
8.5: Flag '-b' was introduced to debug. It is to store a log in the file debug_file
8.5.1 Flag '-s' allows servers directly in the line, not only from file.
 
	'''

	print("\nVersion: "+version)
	print("Comments: "+updates+"\n\n")


