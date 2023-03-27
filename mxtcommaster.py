import requests
import streamlit as st 
import json
import time

pool = "https://api.moneroocean.stream/miner/"
addr ="49FrBm432j9fg33N8PrwSiSig7aTrxZ1wY4eELssmkmeESaYzk2fPkvfN7Kj4NHMfH11NuhUAcKc5DkP7jZQTvVGUnD243g"
stats ="/stats/"


def resp(worker,ch):
  
  host = pool + addr + stats + worker
  res = requests.get(host)
  time.sleep(10)
  jde = json.loads(str(res.text))
  workt = jde[("lts")]
  t = time.time()
  lst = t - workt
  lstnt = lst / 60
  if lstnt >= 20:
    ch = 1
  else:
    ch = 0
  st.write(worker,"last share", lstnt, "mins ago")
  

dcon = st.container()


while 1==1 :
  dcon.write(resp("mxt"))
  dcon.write(resp("stream"))
  dcon.write(resp("mxtgen1"))
  dcon.write(resp("mxtgen2"))
  dcon.write(resp("mxtgen3"))
  dcon.write(resp("mxtgen4"))
  dcon.write(resp("mxtgen5"))
  dcon.write(resp("mxtgen6"))
  dcon.write(resp("mxtgen8"))
  dcon.write(resp("mv2gen1"))
  dcon.write(resp("mv2gen2"))
  dcon.write(resp("mv2gen3"))
  dcon.write(resp("mv2gen4"))
  dcon.write(resp("mv2gen5"))
  dcon.write(resp("mv2gen6"))
  dcon.write(resp("mv2gen7"))
  dcon.write(resp("mv2gen8"))
  dcon.write(resp("mv2gen9"))
  dcon.write(resp("mv2gen10"))
  st.empty()
  


  
