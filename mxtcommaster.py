import socket 

def fetcher(h,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(h)
    print ("ip ",ip)
    s.connect((ip, p))
    resp = s.recv(99999999999999999999)
    return resp


print(fetcher("google.com",443))
    




