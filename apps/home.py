import streamlit as st
from PIL import Image

def app():
  #  st.title('SAMU - Controle de remoções v0.10')

  image = Image.open('banner.png')
  st.image(image, caption='SAMU', use_column_width=True)



