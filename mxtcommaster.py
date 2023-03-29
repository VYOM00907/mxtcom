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
    print(worker,"last share", lstnt, "mins ago")
      

def stch():
    while 1==1 :
      #mv1
      resp("mxt")
      resp("mxtgen01")
      resp("mxtgen1")
      resp("mxtgen2")
      resp("mxtgen3")
      resp("mxtgen4")
      resp("mxtgen5")
      resp("mxtgen6")
      resp("mxtgen8")
      #mv2
      resp("mv2gen1")
      resp("mv2gen2")
      resp("mv2gen3")
      resp("mv2gen4")
      resp("mv2gen5")
      resp("mv2gen6")
      resp("mv2gen7")
      resp("mv2gen8")
      resp("mv2gen9")
      resp("mv2gen10")
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

  
