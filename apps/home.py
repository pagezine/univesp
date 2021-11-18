import streamlit as st
from PIL import Image
import sqlite3
import pandas as pd

conn = sqlite3.connect('apps/pi_cross.db', check_same_thread=False)
c = conn.cursor()

def selectTable():
    c.execute("SELECT * FROM Agendamento LIMIT 5")

    data = c.fetchall()
    conn.commit()

    return data

def app():
  #  st.title('SAMU - Controle de remoções v0.10')

  image = Image.open('banner.png')
  st.image(image, caption='SAMU', use_column_width=True)

  query_results = selectTable()

  st.write(pd.DataFrame(query_results, columns=['ID', 'Tipo', 'CPF', 'Paciente', 'CNPJ - Hospital', 'Sigla', 'Data']))

  



