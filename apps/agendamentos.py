import streamlit as st
from PIL import Image
import sqlite3
import pandas as pd

conn = sqlite3.connect('apps/pi_cross.db', check_same_thread=False)
c = conn.cursor()

#verificar tabela
def selectTable():
    c.execute("SELECT * FROM Agendamento")

    data = c.fetchall()
    conn.commit()

    return data

#adicionar agendamento
def insertScheduling(tipo_agend, cpf_pac, nome_pac, cnpj_unid, sigla_unid, data_agend):
    conn.execute('''
        INSERT INTO Agendamento (Tipo_agend, cpf, nome_pac, cnpj, sigla, data)
        VALUES (
            ?, ?, ?, ?, ?, ?
        );
    ''', (tipo_agend, cpf_pac, nome_pac, cnpj_unid, sigla_unid, data_agend))

    conn.commit()

#excluir um agendamento
def deleteRow(tabela, chave, entidade):
    conn.execute("DELETE FROM " + tabela + " WHERE " + entidade + " = " + chave)

    conn.commit()

def app():
    st.title('Agendamentos')
    st.subheader("Últimos 5 Agendamentos Realizados")

    image = Image.open('agendamento.png')
    st.sidebar.image(image, caption='AGENDAMENTO', use_column_width=True)

    query_results = selectTable()
    st.write(pd.DataFrame(query_results, columns=['ID', 'Tipo', 'CPF', 'Paciente', 'CNPJ - Hospital', 'Sigla', 'Data']))

    st.subheader("Registro")
    tipo_agend = st.text_area("Qual é o tipo de agendamento (Consulta, Exame)?: ")
    cpf_pac = st.text_area("Digite o CPF deste paciente (Sem Pontos): ")
    nome_pac = st.text_area("Nome do paciente: ")
    cnpj_unid = st.text_area("CNPJ da unidade de atendimento (Sem Pontos): ")
    sigla_unid = st.text_area("Nome da unidade: ")
    data_agend = st.text_area("Digite a data de agendamento (no modelo Ano-Mês-Dia): ")

    with st.form(key='query_form'):
        submit_code = st.form_submit_button("Inserir")

        if submit_code:
            insertScheduling(tipo_agend, cpf_pac, nome_pac, cnpj_unid, sigla_unid, data_agend)
            st.write("Agendamento Realizado com Sucesso!")

    st.subheader("Remover")
    entidade = 'cpf'
    chave = st.text_area("Digite o CPF do paciente (Sem Pontos): ")
    tabela = 'Agendamento'

    with st.form(key='query_form_2'):
        chave = st.text_area("CPF (Sem Pontos)")
        submit_code = st.form_submit_button("Remover")

        if submit_code:
            deleteRow('Agendamento', chave, 'CPF')
            st.write("Agendamento Removido com Sucesso!")




