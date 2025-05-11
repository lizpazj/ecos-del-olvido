import streamlit as st

st.set_page_config(page_title="Ecos del Olvido - 20 K-Dramas", layout="centered")

st.title("🌸 Ecos del Olvido")
st.markdown("Explora fragmentos de 20 K-Dramas que marcaron el alma...")

kdrama_opciones = {
    "Escalera al Cielo": "kdrama_1.png",
    "Goblin": "kdrama_2.png",
    "Boys Over Flowers": "kdrama_3.png",
    "My Love from the Star": "kdrama_4.png",
    "Crash Landing on You": "kdrama_5.png",
    "It's Okay to Not Be Okay": "kdrama_6.png",
    "True Beauty": "kdrama_7.png",
    "Start-Up": "kdrama_8.png",
    "The Heirs": "kdrama_9.png",
    "Hotel del Luna": "kdrama_10.png",
    "Extraordinary Attorney Woo": "kdrama_11.png",
    "Twenty-Five Twenty-One": "kdrama_12.png",
    "The Glory": "kdrama_13.png",
    "Business Proposal": "kdrama_14.png",
    "Hometown Cha-Cha-Cha": "kdrama_15.png",
    "Reborn Rich": "kdrama_16.png",
    "Moon Lovers: Scarlet Heart Ryeo": "kdrama_17.png",
    "Mr. Sunshine": "kdrama_18.png",
    "While You Were Sleeping": "kdrama_19.png",
    "Nevertheless": "kdrama_20.png",
}

opcion = st.selectbox("Elige un K-Drama para explorar su recuerdo:", list(kdrama_opciones.keys()))

if opcion:
    st.image(kdrama_opciones[opcion], use_column_width=True)
