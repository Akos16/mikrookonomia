import streamlit as st

st.set_page_config(
    page_title="Mikroökonómiai labor",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Interaktív mikroökonómiai labor")

st.write(
    "Válassz témakört, és vizsgáld meg "
    "a közgazdasági összefüggéseket!"
)

tema = st.sidebar.selectbox(
    "Témakörök",
    [
        "Keresleti függvény",
        "Kínálati függvény",
        "Piaci egyensúly",
        "Árrugalmasság",
        "Fogyasztói optimum",
        "Költségfüggvények"
    ]
)

if tema == "Keresleti függvény":
    from kereslet import megjelenites
    megjelenites()

else:
    st.info("Ez a témakör hamarosan elkészül.")
