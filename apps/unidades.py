import streamlit as st
from PIL import Image

def app():
 st.title('Unidades')

 image = Image.open('unidades.png')
 st.sidebar.image(image, caption='UNIDADES', use_column_width=True)

#pagina inicial
price_filter = st.slider('Raio de Localização de Emergências ',)