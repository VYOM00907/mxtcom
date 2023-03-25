import socket 

def fetcher(h,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(h)
    print ("ip ",ip)
    s.connect((ip, p))
    resp = s.recv(99999)
    return resp


print(fetcher("https://api.moneroocean.stream/miner/49FrBm432j9fg33N8PrwSiSig7aTrxZ1wY4eELssmkmeESaYzk2fPkvfN7Kj4NHMfH11NuhUAcKc5DkP7jZQTvVGUnD243g/stats/",80))
    




