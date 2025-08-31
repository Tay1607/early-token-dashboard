import streamlit as st
import requests
from utils import get_pairs

# 🖥️ Grundopsætning af siden
st.set_page_config(page_title="Early Token Dashboard", page_icon="🚀")
st.title("🚀 Early Token Discovery Dashboard")
st.write("✅ Appen er startet og kører")

# 🔄 Funktion til at hente ALLE tokens fra DEX Screener
def get_pairs():
    url = "https://api.dexscreener.com/latest/dex/pairs"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        st.error(f"Fejl ved hentning af data: {e}")
        return []

    pairs = []
    for pair in data.get("pairs", []):
        pairs.append({
            "pair": pair.get("pairAddress"),
            "token0": (pair.get("token0") or {}).get("symbol"),
            "token1": (pair.get("token1") or {}).get("symbol"),
            "liquidity": (pair.get("liquidity") or {}).get("usd", 0)
        })
    return pairs

# 🔄 Hent data
tokens = get_pairs()

# 🐞 Debug: vis rå API-data og antal tokens
st.subheader("Debug: rå API-data")
st.write(tokens)
st.write(f"Antal tokens fundet: {len(tokens)}")

# 📊 Vis tokens eller fallback
if tokens:
    st.subheader("📈 Fundne tokens")
    for token in tokens[:20]:  # viser kun de første 20 for hastighed
        st.markdown(f"### {token['token0']} / {token['token1']}")
        st.write(f"💧 Likviditet: ${token['liquidity']}")
        st.write(f"🔗 Pair Address: `{token['pair']}`")
        st.markdown("---")
else:
    st.warning("Ingen tokens fundet lige nu. Prøv igen om lidt.")
