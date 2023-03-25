import requests
import streamlit as st 
def resp(host):
  resp = requests.get(host)
  return resp.text
st.write(resp("https://api.moneroocean.stream/miner/49FrBm432j9fg33N8PrwSiSig7aTrxZ1wY4eELssmkmeESaYzk2fPkvfN7Kj4NHMfH11NuhUAcKc5DkP7jZQTvVGUnD243g/stats/"))
