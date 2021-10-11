import sqlite3

# Conexão ao banco de dados;
conn = sqlite3.connect('pi_cross.db')

# Definindo um cursor, que irá executar as queries.
cursor = conn.cursor()

#SQL - Criação das Tabelas
def createTable():
    cursor.executescript(
        '''
            CREATE TABLE IF NOT EXISTS Paciente
            (
                cpf INTEGER PRIMARY KEY NOT NULL,
                nome VARCHAR(100) NOT NULL,
                nascimento DATETIME,
                endereco VARCHAR(150) NOT NULL,
                cep INTEGER NOT NULL,
                cidade VARCHAR(50) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Unidade
            (
                cnpj INTEGER PRIMARY KEY NOT NULL,
                sigla VARCHAR(20) NOT NULL,
                cidade VARCHAR(50) NOT NULL,
                perfil VARCHAR(100) NOT NULL,
                gestao VARCHAR(30) NOT NULL,
                unid_mov_disp INTEGER NOT NULL,
                endereco VARCHAR(150) NOT NULL,
                cep INTEGER NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Agendamento
            (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Tipo_agend VARCHAR(30) NOT NULL,
                cpf INTEGER NOT NULL,
                nome_pac VARCHAR(100) NOT NULL,
                cnpj INTEGER NOT NULL,
                sigla VARCHAR(20) NOT NULL,
                data DATETIME NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Especialidades 
            (
                id_espec INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_atend VARCHAR(50) NOT NULL,
                sigla VARCHAR(20) NOT NULL,
                espec_med VARCHAR(30) NOT NULL,
                cidade VARCHAR(100) NOT NULL
            );
        '''
    )

    conn.commit()
    conn.close()

createTable()