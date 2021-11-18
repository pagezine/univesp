import streamlit as st
from PIL import Image
import sqlite3
import pandas as pd

conn = sqlite3.connect('apps/pi_cross.db', check_same_thread=False)
c = conn.cursor()


def selectTable():
    c.execute("SELECT * FROM Unidade LIMIT 5")

    data = c.fetchall()
    conn.commit()

    return data


def insertUnit(cnpj, sigla_unid, cidade_unid, tipo_unid, gerenc, ambulancia, endereco_unid, cep):
    conn.execute('''
                INSERT INTO Unidade
                    VALUES
                    (
                        ?, ?, ?, ?, ?, ?, ?, ?
                    );
            ''', (cnpj, sigla_unid, cidade_unid, tipo_unid, gerenc, ambulancia, endereco_unid, cep))

    conn.commit()


def app():
    st.title('Unidades')

    image = Image.open('unidades.png')
    st.sidebar.image(image, caption='UNIDADES', use_column_width=True)

    query_results = selectTable()
    st.write(pd.DataFrame(query_results, columns=[
        'CNPJ', 'Sigla', 'Cidade', 'Perfil', 'Gestão', 'Unidades Disponíveis', 'Endereço', 'CEP']))

    st.subheader("Registro")
    cnpj = st.text_area("CNPJ (Sem Pontos)")
    sigla_unid = st.text_area("Nome da unidade")
    cidade_unid = st.text_area("Cidade da unidade")
    tipo_unid = st.text_area("Tipo da unidade (hospital, UBS etc.): ")
    gerenc = st.text_area(
        "Tipo de gerenciamento (público ou privado): ")
    ambulancia = st.text_area(
        "Número de ambulâncias disponíveis (caso não haja, digite 0): ")
    endereco_unid = st.text_area(
        "Endereço desta unidade, com vírgula entre nome e número, e após, coloque o bairro: ")
    cep = st.text_area("CEP (Sem Pontos)")

    with st.form(key='query_form'):
        submit_code = st.form_submit_button("Inserir")

        if submit_code:
            insertUnit(cnpj, sigla_unid, cidade_unid, tipo_unid,
                        gerenc, ambulancia, endereco_unid, cep)
            st.write("Unidade Inserida com Sucesso!")


    st.subheader("Remover")
    st.write("Desculpe, mas ainda não é possível permitir que você remova esse campo!")

# pagina inicial
price_filter = st.slider('Raio de Localização de Emergências ',)
