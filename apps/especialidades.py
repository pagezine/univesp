import streamlit as st
from PIL import Image

def app():
 st.title('Especialidades')

image = Image.open('especialidades.png')
st.sidebar.image(image, caption='ESPECIALIDADES', use_column_width=True)

