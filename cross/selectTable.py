import sqlite3

# Conexão ao banco de dados;
conn = sqlite3.connect('pi_cross.db')

# Definindo um cursor, que irá executar as queries.
cursor = conn.cursor()

#Verificando dados das tabelas
def selectTable():

    ### Este trecho de código é para testes, deve ser substituído quando definidas as rotas
    tb_type = ['Especialidades', 'Paciente', 'Unidade', 'Agendamento']
    tbl_selected = int(input('''
        Qual tabela deseja selecionar?:\n

        1 - Especialidades
        2 - Paciente
        3 - Unidade
        4 - Agendamento 
    ''')) - 1 
    ###

    shown = conn.execute("SELECT * FROM " + tb_type[tbl_selected])

    ## A linha abaixo retorna no terminal o resultado das tabelas
    print(shown.fetchall())
    conn.commit()
    conn.close()

selectTable()

def deleteRow():
    ### Este trecho de código é para testes, deve ser substituído quando definidas as rotas
    tb_type = ['Especialidades', 'Paciente', 'Unidade', 'Agendamento']
    tbl_selected = int(input('''
        Qual tabela deseja excluir?:\n

        1 - Especialidades
        2 - Paciente
        3 - Unidade
        4 - Agendamento 
    ''')) - 1 

    if tb_type[tbl_selected] == tb_type[0]:
        entidade = 'id_espec'
        chave = str(input("Qual é o id desta especialidade?: "))
    
    elif tb_type[tbl_selected] == tb_type[1]:
        entidade = 'cpf'
        chave = str(input("Qual é o cpf?: "))

    elif tb_type[tbl_selected] == tb_type[2]:
        entidade = 'cnpj'
        chave = str(input("Qual é o cnpj?: "))

    elif tb_type[tbl_selected] == tb_type[3]:
        entidade = 'cpf'
        chave = str(input("Qual é o cpf do paciente?: "))
    ###

    conn.execute("DELETE FROM" + tb_type[tbl_selected] + "WHERE" + entidade + "=" + chave)

    conn.commit()
    conn.close()

# deleteRow()