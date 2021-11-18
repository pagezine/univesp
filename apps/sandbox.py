import streamlit as st

from PIL import Image

def app():
 st.title('SandBox')

 image = Image.open('localizacao.png')
 st.sidebar.image(image, caption='SAMU', use_column_width=True)