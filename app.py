import streamlit as st
from utils.get_parts import get_pairs

# 🖥️ Grundopsætning
st.set_page_config(page_title="Early Token Dashboard", page_icon="🚀")
st.title("🚀 Early Token Discovery Dashboard")

# ✅ Testbesked for at sikre, at appen kører
st.write("✅ Appen er startet og kører")

# 🔄 Hent data
try:
    tokens = get_pairs()
except Exception as e:
    st.error(f"Kunne ikke hente data: {e}")
    st.stop()

# 🐞 Debug: Vis rå data fra API
st.subheader("Debug: Rå data fra API")
st.write(tokens)

# 📊 Vis tokens eller fallback
if tokens:
    st.subheader("📈 Fundne tokens")
    for token in tokens:
        st.markdown(f"### {token['token0']} / {token['token1']}")
        st.write(f"💧 Likviditet: ${token['liquidity']}")
        st.write(f"🔗 Pair Address: `{token['pair']}`")
        st.markdown("---")
else:
    st.warning("Ingen tokens fundet lige nu. Prøv igen om lidt.")
