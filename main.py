import streamlit as st
from PIL import Image

from multiapp import MultiApp
from apps import home, data_stats, agendamentos, especialidades, pacientes, unidades,sandbox  # import your app modules here
#from apps import home, data_stats, agendamentos

app = MultiApp()

# adicionar aplicações aqui - pasta APPS
app.add_app("Home", home.app) # app.add_app("Home", home.app)
app.add_app("Agendamentos", agendamentos.app)
app.add_app("Unidades", unidades.app)
app.add_app("Especialidades", especialidades.app)
app.add_app("Pacientes", pacientes.app)
app.add_app("Estatisticas", data_stats.app)
app.add_app("SandBox", sandbox.app)

# Roda principal
app.run()
# -- parar aqui






#PAGES = {
 #   "Agendamentos": agendamentos,
 #  "Especialidades": especialidades,
 #   "Pacientes":pacientes,
 #   "Unidades":unidades
#}

#st.title('SAMU - Controle de remoções v0.10')

# menu - lateral - v.002
#st.sidebar.header("Cadastros")
#st.sidebar.header(" - Especialidades")
#st.sidebar.header(" - Pacientes")
#st.sidebar.header(" - Unidades")
#st.sidebar.header(" - Agendamentos")

# menu lateral
#st.sidebar.title('Menu Principal')
#selection = st.sidebar.selectbox(
 #   "Escolha Página",list(PAGES.keys()))
 # page = PAGES[selection]
 # page.app()




