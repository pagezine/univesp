import streamlit as st


from data.create_data import create_table

def app():
    st.title('Dados Estatísticos')

    st.write("Estatisticas de Aproveitamento.")
    st.write("Lista as estatísticas de todos os atendimentos")

    st.markdown("### Gráfico")
    df = create_table()

    st.line_chart(df)

    # Valores ausentes
    fig = px.bar(x=[0, 0, 0, 0, 0, 177, 0, 0, 0, 0, 687, 2],
                 y=['PassengerId', 'Survived', 'Pclass', 'Name',
                    'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
                 orientation='h', title=" Valores faltantes ",
                 labels={'x': 'Quantidade', 'y': 'Dados'})
    st.plotly_chart(fig)