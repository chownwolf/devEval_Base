#!/usr/bin/env python
"""
Aurthor chownwolf
The Ness6rest must be imported after it is installed
    Nessrest was created by streck,xorrbit, and updtated by other Contributors 
"""
import socket
import subprocess
import sys
from datetime import datetime
import time
import ness6rest
import textwrap
import itertools
import tabcomplete
import getpass

# Clear the screen
subprocess.call('clear', shell=True)

#Convert input to raw input to make it backwards compatable
try:
    input = raw_input
except:
    pass

# Ask for input
print("-" * 70)
nname = input("Please Enter the name of the Device: ")
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
print("-" * 70)

#Create the document
evaldoc = open(nname+"Eval.txt","w+")

# Print a nice banner with information on which host we are about to scan
print("-" * 70)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 70)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 65095)

# We also put in some error handling for catching errors

try:
    for port in range(1,65095):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:	 Open".format(port))
            evaldoc.write("Port {}: Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print("-" * 70)
print('Port Scan Completed in: ', total)
print("-" * 70)

#Nessus piece down below
print("-" * 70)
print("Now creating a Nessus scan")
print("-" * 70)

#Below will store Vars for Nesscan to work Username Password URL etc
#I have multiple servers that is why you see the menu below. 
print("-" * 70)
print("1. For Server1")
print("2. For Server2")
print("3. For Server3")
print("4. For Server4")
print("-" * 70)
whichscanr = input("Which scanner would you like to use? ")
print("-" * 70)
try:
    if whichscanr == "1":
        print("Server1 selected")
        #Use your URL
        nessus_url = "YourURL:8834"
    elif whichscanr == "2":
        print("Server2 selected")
        #Use your URL
        nessus_url = "YourURL:8834"
    elif whichscanr == "3":
        print("Server3 selected")
        #Use your URL
        nessus_url = "YourURL:8834"
    elif whichscanr == "4":
        print("Server4 selected")
        #Use your URL
        nessus_url = "YourURL:8834"
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

print("-" * 70)
nlogin = input("Please enter your Nessus Username: ")
npass = getpass.getpass("Please enter your password: ")
print("-" * 70)
print('\n')

# YOU dont have to hard code your policy i do
npolicy = "Your policy"

#Login to Nessus 
nscan = ness6rest.Scanner(url=nessus_url,login=nlogin,password=npass,insecure=True)

#Set policy for scan
nscan.policy_set(name=npolicy)

#Set Target for scan
nscan.scan_add(targets=remoteServer,name=nname)

#Run the Scan 
nscan.scan_run()
print("-" * 70)
#Get the results of scan
nscan.scan_results()
results_one = nscan.scan_results()
evaldoc.write(results_one)

#Scan results time
t3 = datetime.now()
nesstimet = t3 - t2
print("-" * 70)
print(nesstimet)
print("-" * 70)

#Close doc for good
evaldoc.close()

#Wait for a little some time before screen clears
time.sleep(5)

#Clear the scan
subprocess.call('clear', shell=True)
