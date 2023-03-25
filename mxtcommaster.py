import requests
import streamlit as st 
import json
import time
pool = "https://api.moneroocean.stream/miner/"
addr ="49FrBm432j9fg33N8PrwSiSig7aTrxZ1wY4eELssmkmeESaYzk2fPkvfN7Kj4NHMfH11NuhUAcKc5DkP7jZQTvVGUnD243g"
stats ="/stats/"

def resp(worker):
  
  host = pool + addr + stats + worker
  resp = requests.get(host)
  jde = json.loads(str(resp))
  #workt = jde[("lts")]
  t = time.time()
  #lst = t - workt
  #st.write("workerslast share", lst)
  return resp.text

st.write(resp("mxtgen8"))
