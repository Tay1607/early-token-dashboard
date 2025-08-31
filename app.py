import streamlit as st
from utils import get_pairs
import time

st.set_page_config(page_title="Early Token Dashboard", page_icon="🚀")
st.title("🚀 Early Token Discovery Dashboard")
st.write("✅ Appen er startet og kører")

if 'pairs' not in st.session_state:
    st.session_state.pairs = get_pairs()

if st.button('🔄 Opdater data'):
    st.session_state.pairs = get_pairs()

st.write("Data sidst opdateret: " + time.strftime('%Y-%m-%d %H:%M:%S'))

tokens = st.session_state.pairs

st.subheader("Debug: rå API-data")
st.write(tokens)
st.write(f"Antal tokens fundet: {len(tokens)}")

if tokens:
    st.subheader("📈 Fundne tokens")
    for token in tokens[:20]:
        st.markdown(f"### {token['token0']} / {token['token1']}")
        st.write(f"💧 Likviditet: ${token['liquidity']}")
        st.write(f"🔗 Pair Address: `{token['pair']}`")
        st.markdown("---")
else:
    st.warning("Ingen tokens fundet lige nu. Prøv igen om lidt.")
