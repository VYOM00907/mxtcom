from pythonping import ping
import socket as s
print("communication master module for mxt")
hn = "https://www.geeksforgeeks.org/python-program-find-ip-address/"
ip = s.gethostbyname('checkip.dyndns.com')
ping(s.gethostbyname('checkip.dyndns.com'))



