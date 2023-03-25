import requests
import streamlit as st 
import json
pool = "https://api.moneroocean.stream/miner/"
addr ="49FrBm432j9fg33N8PrwSiSig7aTrxZ1wY4eELssmkmeESaYzk2fPkvfN7Kj4NHMfH11NuhUAcKc5DkP7jZQTvVGUnD243g"
stats ="/stats/"

def resp(host):
  resp = requests.get(host)
  return resp.text
st.write(resp(pool + addr + stats + "mxt"))
