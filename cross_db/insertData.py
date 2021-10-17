import sqlite3

# Conexão ao banco de dados;
conn = sqlite3.connect('pi_cross.db')

# Definindo um cursor, que irá executar as queries.
cursor = conn.cursor()

#Este bloco ficou para teste durante a montagem das tabelas e backend
tb_type = ['Especialidades', 'Paciente', 'Unidade', 'Agendamentos']
tb_chosen = int(input('''
    Escolha uma das opções para inserir os dados:\n
    1 - Especialidades
    2 - Paciente
    3 - Unidade
    4 - Agendamentos
''')) - 1
#

# SQL - Persistência dos dados no banco para novas especialides, pacientes e unidades, e também marcação de agendamentos

def insertSpec():
    ### Este trecho de código é para testes, deve ser substituído quando definidas as rotas
    ch_atend = str(input("Qual é o tipo de atendimento?: "))
    sigla_unid = str(input("Qual é a sigla da unidade?: "))
    especialid = str(input("Qual é a especialidade?: "))
    cidade_unid = str(input("Qual é a cidade da unidade?: "))
    ###

    conn.execute('''
            INSERT INTO especialidades (tipo_atend, sigla, espec_med, cidade)
            VALUES
            (
                ?, ?, ?, ?
            );
        ''', (ch_atend, sigla_unid, especialid, cidade_unid))
    

    conn.commit()
    conn.close()


def insertPac():
    ### Este trecho de código é para testes, deve ser substituído quando definidas as rotas
    cpf = int(input("CPF do paciente: "))
    nome = str(input("Nome do paciente: "))
    data_nasc = str(
        input("Digite a data de nascimento (no modelo Ano-Mês-Dia): "))
    logradouro = str(
        input("Endereço do paciente, com número separado por vírgula: "))
    cep = int(input("Digite o cep: "))
    cidade_pac = str(input("Cidade onde reside: "))
    ###

    conn.execute('''
            INSERT INTO Paciente 
            VALUES (
                ?, ?, ?, ?, ?, ?
            );
        ''', (cpf, nome, data_nasc, logradouro, cep, cidade_pac))

    conn.commit()
    conn.close()


def insertUnit():
    ### Este trecho de código é para testes, deve ser substituído quando definidas as rotas
    cnpj = int(input("Digite o CNPJ da unidade: "))
    sigla_unid = str(input("Digite a sigla da unidade: "))
    cidade_unid = str(input("Digite a cidade da unidade: "))
    tipo_unid = str(input("Digite o tipo da unidade (hospital, UBS etc.): "))
    gerenc = str(
        input("Digite o tipo de gerenciamento (público ou privado): "))
    ambulancia = int(input("Digite o número de ambulâncias disponíveis (caso não haja, digite 0): "))
    endereco_unid = str(input(
        "Digite o endereço desta unidade, com vírgula entre nome e número, e após, coloque o bairro: "))
    cep = str(input("CEP desta unidade: "))
    ###

    conn.execute('''
                INSERT INTO Unidade 
                    VALUES
                    (
                        ?, ?, ?, ?, ?, ?, ?, ?
                    );
            ''', (cnpj, sigla_unid, cidade_unid, tipo_unid, gerenc, ambulancia, endereco_unid, cep))

    conn.commit()
    conn.close()

#SQL - Criação de novos agendamentos
def insertScheduling(): 
    ### Este trecho de código é para testes, deve ser substituído quando definidas as rotas
    tipo_agend = str(input("Qual é o tipo de agendamento?: "))
    cpf_pac = int(input("Digite o CPF deste paciente: "))
    nome_pac = str(input("Nome do paciente: "))
    cnpj_unid = int(input("CNPJ da unidade de atendimento: "))
    sigla_unid = str(input("Sigla da unidade: "))
    data_agend = str(input("Digite a data de agendamento (no modelo Ano-Mês-Dia): "))
    ###

    conn.execute('''
        INSERT INTO Agendamento (Tipo_agend, cpf, nome_pac, cnpj, sigla, data)
        VALUES (
            ?, ?, ?, ?, ?, ?
        );
    ''', (tipo_agend, cpf_pac, nome_pac, cnpj_unid, sigla_unid, data_agend))

    conn.commit()
    conn.close()

### Este trecho de código é para testes, deve ser substituído quando definidas as rotas   
if tb_type[tb_chosen] == 'Unidade':
    insertUnit()

if tb_type[tb_chosen] == 'Paciente':
    insertPac()

if tb_type[tb_chosen] == 'Especialidades':
    insertSpec()

if tb_type[tb_chosen] == 'Agendamentos':
    insertScheduling()
