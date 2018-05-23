import subprocess
import sys
import os
import pyshark
print "Please enter the name of the capture file"
old_stdout = sys.stdout
log_file = open("logged.log","w")
sys.stdout = log_file
name = raw_input("File Name?")
cap = pyshark.FileCapture('./'+name)
for i in range (1,10):
 print cap[i]
else:
 print "Packet ends"

sys.stdout = old_stdout
log_file.close()
print "Done"
os.system('python GUI.py')
