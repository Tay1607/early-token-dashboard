import streamlit as st
from utils.Tay1607 import get_pairs
import time

# 🖥️ Grundopsætning af siden
st.set_page_config(page_title="Early Token Dashboard", page_icon="🚀")
st.title("🚀 Early Token Dashboard")

# Første load af data
if "pairs" not in st.session_state:
    st.session_state.pairs = get_pairs()

# Opdater-knap
if st.button("🔄 Opdater data"):
    st.session_state.pairs = get_pairs()

# Vis tidspunkt for seneste opdatering
st.write(f"Data sidst opdateret: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Hent data fra session state
pairs = st.session_state.pairs

# Hvis get_pairs returnerer en Pandas DataFrame (som i Tay1607.py)
try:
    st.subheader("📊 Token Pairs")
    st.dataframe(pairs, use_container_width=True)
    st.metric("Antal par", len(pairs))
except Exception as e:
    st.error(f"Kunne ikke vise data: {e}")
    st.write(pairs)  # fallback visning
