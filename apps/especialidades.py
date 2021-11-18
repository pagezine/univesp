import streamlit as st
from PIL import Image
import sqlite3
import pandas as pd

conn = sqlite3.connect('apps/pi_cross.db', check_same_thread=False)
c = conn.cursor()


def selectTable():
    c.execute("SELECT * FROM Especialidades")

    data = c.fetchall()
    conn.commit()

    return data


def insertSpec(ch_atend, sigla_unid, especialid, cidade_unid):
    conn.execute('''
            INSERT INTO especialidades (tipo_atend, sigla, espec_med, cidade)
            VALUES
            (
                ?, ?, ?, ?
            );
        ''', (ch_atend, sigla_unid, especialid, cidade_unid))

    conn.commit()


def app():
    st.title('Especialidades')

    image = Image.open('especialidades.png')
    st.sidebar.image(image, caption='ESPECIALIDADES', use_column_width=True)

    query_results = selectTable()
    st.write(pd.DataFrame(query_results, columns=[
             'ID', 'Tipo', 'Sigla', 'Especialidade', 'Cidade']))

    st.subheader("Registro")
    ch_atend = st.text_area("Qual é o tipo de atendimento? (Consulta, Exame)")
    sigla_unid = st.text_area("Nome da Unidade")
    especialid = st.text_area("Especialidade")
    cidade_unid = st.text_area("Cidade da Unidade")

    with st.form(key='query_form'):
        submit_code = st.form_submit_button("Inserir")

        if submit_code:
            insertSpec(ch_atend, sigla_unid, especialid, cidade_unid)
            st.write("Especialidade Inserida com Sucesso!")

    st.subheader("Remover")
    st.write("Desculpe, mas ainda não é possível permitir que você remova esse campo!")
