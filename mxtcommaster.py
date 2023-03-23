from pythonping import ping
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("communication master module for mxt")
hn = "https://www.geeksforgeeks.org/python-program-find-ip-address/"
ip = socket.gethostbyname('checkip.dyndns.com')
s.connect((ip, 443))



