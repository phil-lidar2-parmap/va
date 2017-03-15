# Windows

__version__ = "0.1.1"

import os
from datetime import datetime

current_directory= os.getcwd()

num_files = 0

for files in os.listdir(current_directory):
	if files.endswith(".py"):
		pass
	else:
		num_files += 1
		new_name =  files.replace("hazard", "hazard_parmap")
		print new_name
		os.rename(files,new_name)
		print "[" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]", files, "---->", new_name
print "Number of files: " + str(num_files)
raw_input('\nPress ENTER to exit...')