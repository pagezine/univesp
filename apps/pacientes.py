import streamlit as st
from PIL import Image
import sqlite3
import pandas as pd

conn = sqlite3.connect('apps/pi_cross.db', check_same_thread=False)
c = conn.cursor()


def selectTable():
  c.execute("SELECT * FROM Paciente LIMIT 10")

  data = c.fetchall()
  conn.commit()

  return data


def insertPac(cpf, nome, data_nasc, logradouro, cep, cidade_pac):
  conn.execute('''
        INSERT INTO Paciente 
        VALUES (
            ?, ?, ?, ?, ?, ?
        );
    ''', (cpf, nome, data_nasc, logradouro, cep, cidade_pac))

  conn.commit()


def deleteRow(tabela, chave, entidade):
  conn.execute("DELETE FROM " + tabela + " WHERE " + entidade + " = " + chave)

  conn.commit()


def app():
  st.title('Pacientes')

  image = Image.open('pacientes.png')
  st.sidebar.image(image, caption='PACIENTES', use_column_width=True)

  query_results = selectTable()
  st.write(pd.DataFrame(query_results, columns=['CPF', 'Nome', 'Nascimento', 'Endereço', 'CEP', 'Cidade']))

  st.subheader("Registro")
  cpf = st.text_area("CPF (Sem Pontos)")
  nome = st.text_area("Nome")
  data_nasc = st.text_area(
      "Data de Nascimento (Insira no formato ANO-MES-DIA)")
  logradouro = st.text_area("Logradouro")
  cep = st.text_area("CEP (Sem Pontos)")
  cidade_pac = st.text_area("Cidade do Paciente")

  with st.form(key='query_form'):
      submit_code = st.form_submit_button("Inserir")

      if submit_code:
        insertPac(cpf, nome, data_nasc, logradouro, cep, cidade_pac)
        st.write("Paciente Inserido com Sucesso!")

  st.subheader("Remover")
  st.write("Desculpe, mas ainda não é possível permitir que você remova esse campo!")

  # Utilizaçõa de colunas

  # Grafico do Sexo dos Pacientes
  # col1, col2 = st.beta_columns(2)

  # with col1:
  #   fig = px.histogram(train, x="Sex", nbins=50, title='Sexo dos Passageiros', labels={"Sex": 'Sexo'}, width=400,
  #                      height=400)
  #   st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

  # with col2:
  #   fig = px.bar(train, x="Sex", y="Survived", color="Sex", title=" Sobreviventes x Sexo ",
  #                labels={'Sex': 'Sexo', 'Survived': 'Sobreviventes'}, width=400, height=400)
  #   st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

  # Grafico Da Classe dos Pacientes

  # col1, col2 = st.beta_columns(2)

  # with col1:
  #   fig = px.histogram(train, x="Pclass", nbins=10, title='Classe dos Passageiros',
  #                      labels={"Pclass": 'Classe', 'count': 'Quantidade por Classe'}, width=400, height=400)
  #   st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

  # with col2:
  #   fig = px.bar(train, x="Pclass", y="Survived", color="Pclass", title="Sobreviventes x Classe",
  #                labels={"Pclass": 'Classe do Passageiro', 'Survived': 'Sobreviventes'}, width=400, height=400)
  #   st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
