import streamlit as st
from PIL import Image

def app():
 st.title('Agendamentos')

 image = Image.open('agendamento.png')
 st.sidebar.image(image, caption='AGENDAMENTO', use_column_width=True)
