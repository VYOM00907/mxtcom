import requests
import streamlit as st 
import json
import time

pool = "https://api.moneroocean.stream/miner/"
addr ="49FrBm432j9fg33N8PrwSiSig7aTrxZ1wY4eELssmkmeESaYzk2fPkvfN7Kj4NHMfH11NuhUAcKc5DkP7jZQTvVGUnD243g"
stats ="/stats/"

def resp(worker):
  
  host = pool + addr + stats + worker
  res = requests.get(host)
  time.sleep(12)
  jde = json.loads(str(res.text))
  workt = jde[("lts")]
  t = time.time()
  lst = t - workt
  st.write("workerslast share", lst)
  return res.text
while 1==1 :
  st.write(resp("mxt"))
