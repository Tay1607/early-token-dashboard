import streamlit as st
from utils import get_pairs
import time

# 🖥️ Grundopsætning
st.set_page_config(page_title="Early Token Dashboard", page_icon="🚀")
st.title("🚀 Early Token Discovery Dashboard")
st.write("✅ Appen er startet og kører")

# 🔄 Hent data (med session state, så vi ikke kalder API'et hele tiden)
if 'pairs' not in st.session_state:
    st.session_state.pairs = get_pairs()

if st.button('🔄 Opdater data'):
    st.session_state.pairs = get_pairs()

st.write("Data sidst opdateret: " + time.strftime('%Y-%m-%d %H:%M:%S'))

tokens = st.session_state.pairs

# 🐞 Debug: vis rå data og antal tokens
st.subheader("Debug: rå API-data")
st.write(tokens)
st.write(f"Antal tokens fundet: {len(tokens)}")

# 📊 Vis tokens eller fallback
if tokens:
    st.subheader("📈 Fundne tokens")
    for token in tokens[:20]:  # viser kun de første 20
        st.markdown(f"### {token['token0']} / {token['token1']}")
        st.write(f"💧 Likviditet: ${token['liquidity']}")
        st.write(f"🔗 Pair Address: `{token['pair']}`")
        st.markdown("---")
else:
    st.warning("Ingen tokens fundet lige nu. Prøv igen om lidt.")
