import requests
import streamlit as st

# 🔗 API-endpoint fra DEX Screener
url = "https://api.dexscreener.com/latest/dex/pairs"

# 🧠 Funktion til at hente og filtrere relevante par
def get_pairs():
    response = requests.get(url)
    data = response.json()
    pairs = [
        {
            "pair": pair["pairAddress"],
            "token0": pair["token0"]["symbol"],
            "token1": pair["token1"]["symbol"],
            "liquidity": pair["liquidity"]["usd"]
        }
        for pair in data["pairs"]
        if pair["token0"]["symbol"] == "TAYLOR" or
           pair["token1"]["symbol"] == "TAYLOR"
    ]
    return pairs

# 🎨 Streamlit UI
st.set_page_config(page_title="Early Token Dashboard", page_icon="🚀")
st.title("🚀 Early Token Discovery Dashboard")
st.markdown("Fokuserer på par med token-symbol **TAYLOR** og likviditet over $1000")

tokens = get_pairs()

if tokens:
    for token in tokens:
        st.subheader(f"{token['token0']} / {token['token1']}")
        st.write(f"💧 Likviditet: ${token['liquidity']}")
        st.write(f"🔗 Pair Address: `{token['pair']}`")
        st.markdown("---")
else:
    st.warning("Ingen relevante par fundet. Prøv igen senere.")
