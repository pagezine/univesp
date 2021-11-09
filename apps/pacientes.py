import streamlit as st
from PIL import Image

def app():
  st.title('Pacientes')

  image = Image.open('pacientes.png')
  st.sidebar.image(image, caption='PACIENTES', use_column_width=True)


  # Utilizaçõa de colunas

  # Grafico do Sexo dos Pacientes
  col1, col2 = st.beta_columns(2)

  with col1:
    fig = px.histogram(train, x="Sex", nbins=50, title='Sexo dos Passageiros', labels={"Sex": 'Sexo'}, width=400,
                       height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

  with col2:
    fig = px.bar(train, x="Sex", y="Survived", color="Sex", title=" Sobreviventes x Sexo ",
                 labels={'Sex': 'Sexo', 'Survived': 'Sobreviventes'}, width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

  # Grafico Da Classe dos Pacientes

  col1, col2 = st.beta_columns(2)

  with col1:
    fig = px.histogram(train, x="Pclass", nbins=10, title='Classe dos Passageiros',
                       labels={"Pclass": 'Classe', 'count': 'Quantidade por Classe'}, width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

  with col2:
    fig = px.bar(train, x="Pclass", y="Survived", color="Pclass", title="Sobreviventes x Classe",
                 labels={"Pclass": 'Classe do Passageiro', 'Survived': 'Sobreviventes'}, width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')