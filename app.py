import streamlit as stl
import requests

stl.set_page_config(page_title="Juegos Gratis", layout="wide")

stl.title("Juegos Free To Play")

plataforma = stl.selectbox(
    "Selecciona una plataforma:",
    ("all", "pc", "browser"),
    format_func=lambda x: "Todas" if x == "all" else ("PC" if x == "pc" else "Web")
)

url = f"https://www.freetogame.com/api/games?platform={plataforma}"
response = requests.get(url)

if response.status_code == 200:
    juegos = response.json()
    
    stl.write(f"**{len(juegos)} juegos** encontrados.")
    
    cols = stl.columns(3)
    for i, juego in enumerate(juegos[:30]):
        with cols[i % 3]:
            stl.image(juego["thumbnail"], use_container_width=True)
            stl.subheader(juego["title"])
            stl.caption(f"**Género:** {juego['genre']} | **Editor:** {juego['publisher']}")
            stl.markdown(f"[Ver más]({juego['game_url']})")
else:
    stl.error("No se encontraron juegos")
