import streamlit as st
import requests

st.title("🚀 Early Token Discovery Dashboard")

def get_new_pairs():
    url = "https://api.dexscreener.com/latest/dex/pairs"
    response = requests.get(url)
    data = response.json()
    
    new_pairs = []
    for pair in data['pairs']:
        if pair['fdv'] and pair['liquidity']['usd']:
            if pair['fdv'] < 1000000 and pair['liquidity']['usd'] > 50000:
                new_pairs.append({
                    'name': pair['baseToken']['name'],
                    'price': pair['priceUsd'],
                    'volume': pair['volume']['h24'],
                    'liquidity': pair['liquidity']['usd'],
                    'url': pair['url']
                })
    return new_pairs

pairs = get_new_pairs()
for token in pairs:
    st.subheader(token['name'])
    st.write(f"💰 Pris: ${token['price']}")
    st.write(f"📊 Volumen (24h): ${token['volume']}")
    st.write(f"💧 Likviditet: ${token['liquidity']}")
    st.markdown(f"[🔗 Se på DEX Screener]({token['url']})")
