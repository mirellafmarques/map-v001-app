import streamlit as st
from streamlit.components.v1 import html
import folium
from streamlit_folium import st_folium  # <-- corrigido aqui
import geographiclib as geo

# Título do app
st.title("Mapa de Rotas")
st.markdown("Este é um exemplo de mapa com Folium em Streamlit.")

# Entradas do usuário para o outro endereço
st.subheader("Insira as coordenadas:")
lat1 = st.number_input("Latitude do ponto 1", format="%.6f")
lon1 = st.number_input("Longitude do ponto 1", format="%.6f")

# Botão para gerar o mapa
if st.button("Gerar Mapa"):
    # Criar o mapa centralizado no primeiro ponto
    m = folium.Map(location=[lat1, lon1], tiles="cartodbpositron", zoom_start=8)

    # Adicionar marcadores
    folium.Marker([lat1, lon1], tooltip="Ponto 1").add_to(m)
    folium.Marker([lat2, lon2], tooltip="Ponto 2").add_to(m)
    

    # Renderizar o mapa
    map_html = m._repr_html_()
    html(map_html, height=500, width=750)


#2. 

m = folium.Map(location=[-25.4921657,-48.8096613], zoom_start=16)
folium.Marker(
    [-25.4921657,-48.8096613],
    popup="UFPR",
    tooltip="Liberty Bell"
).add_to(m)

st_data = st_folium(m, width = 725)
