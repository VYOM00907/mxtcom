import requests
import streamlit as st 
import json
import time
from multiprocessing import Process

pool = "https://api.moneroocean.stream/miner/"
addr ="49FrBm432j9fg33N8PrwSiSig7aTrxZ1wY4eELssmkmeESaYzk2fPkvfN7Kj4NHMfH11NuhUAcKc5DkP7jZQTvVGUnD243g"
stats ="/stats/"


def resp(worker):
  
  host = pool + addr + stats + worker
  res = requests.get(host)
  time.sleep(10)
  jde = json.loads(str(res.text))
  workt = jde[("lts")]
  t = time.time()
  lst = t - workt
  lstnt = lst / 60
  if lstnt >= 30:
    # mxt v 1
    if worker == "mxt":
      requests.get("https://vyom00907-mxtcot-app-ikd0lj.streamlit.app/")
    if worker == "mxtgen01":
      requests.get("https://mxt-vyom00907.streamlit.app/")
    if worker == "mxtgen1":
      requests.get("https://vyom00907-mxtfaujh-mxtgen1-pck5yt.streamlit.app/")
    if worker == "mxtgen2":
      requests.get("https://vyom00907-mxtfaujh-mxtgen2-w6l8nj.streamlit.app/")
    if worker == "mxtgen3":
      requests.get("https://vyom00907-mxtfaujh-mxtgen3-e202e2.streamlit.app/")
    if worker == "mxtgen4":
      requests.get("https://vyom00907-mxtfaujh-mxtgen4-pxwkrs.streamlit.app/")
    if worker == "mxtgen5":
      requests.get("https://vyom00907-mxtfaujh-mxtgen5-yjt88z.streamlit.app/")
    if worker == "mxtgen6":
      requests.get("https://vyom00907-mxtfaujh-mxtgen6-yto63j.streamlit.app/")
    if worker == "mxtgen7":
      requests.get("https://vyom00907-mxtfaujh-mxtgen7-jhx3x5.streamlit.app/")
    if worker == "mxtgen8":
      requests.get("https://vyom00907-mxtfaujh-mxtgen8-klnuoc.streamlit.app/")
    
    
    
      

def stch():
    while 1==1 :
      #mv1
      resp("mxt")
      resp("mxtgen01")
      resp("mxtgen1")
      resp("mxtgen2")
      resp("mxtgen3")
      resp("mxtgen4")
      resp("mxtgen5")
      resp("mxtgen6")
      resp("mxtgen8")
     

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
