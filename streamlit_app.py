import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Título
st.title("Mapa de Ocorrências de Invasão recebidos pelo SIAC 156 - 2025")

# Carregar o arquivo GeoJSON das Ocorrencias de Invasao
geojson_path = "Invasao_156_2025.geojson"

try:
    # Ler o GeoJSON
    gdf = gpd.read_file(geojson_path)

    # Exibe os dados do GeoDataFrame
    st.write("Dados do 156")
    #st.write(gdf.head())  #Tabela de Dados

    # Centro do mapa baseado nos pontos
    mean_lat = gdf.geometry.y.mean()
    mean_lon = gdf.geometry.x.mean()

    # Cria o mapa
    m = folium.Map(location=[mean_lat, mean_lon], zoom_start=12)

    # Adiciona os pontos ao mapa
    for idx, row in gdf.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row['name'],  # Ou outra coluna relevante, dependendo do seu arquivo
            tooltip="Clique aqui!"
        ).add_to(m)

    # Exibe o mapa no Streamlit
    st_folium(m, width=725, height=500)

except Exception as e:
    st.error(f"Erro ao carregar o GeoJSON: {e}")

# ---------------------------------------------
# Gerando o gráfico com os dados dos bairros

# Verifica se a coluna 'Bairro' existe
if 'Bairro' in gdf.columns:
    # Contando as ocorrências de invasão por bairro
    bairro_counts = gdf['Bairro'].value_counts().reset_index()
    bairro_counts.columns = ['Bairro', 'ocorrencias']

    # Exibe a tabela de contagem
    st.write("Número de ocorrências por bairro:")
    #st.write(bairro_counts)

    # Criando o gráfico de barras
    plt.figure(figsize=(12, 8))
    sns.barplot(y='Bairro', x='ocorrencias', data=bairro_counts, palette='plasma')
    plt.xlabel('Quantidade de Ocorrências')
    plt.ylabel('Bairros')
    plt.title('Ocorrências de Invasão por Bairro - SIAC 156 - 2025')

    # Exibe o gráfico no Streamlit
    st.pyplot(plt.gcf())

else:
    st.error("A coluna 'Bairro' não foi encontrada no arquivo GeoJSON.")

