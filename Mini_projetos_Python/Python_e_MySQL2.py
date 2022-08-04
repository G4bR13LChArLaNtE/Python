import mysql.connector

try:
    #Criar uma conexão ao banco de dados:
    con = mysql.connector.connect(host = 'localhost', database = 'cadastro', user = 'root', password = '')

    #Declaração SQL a ser executada:
    criar_tabela_SQL = """create table professor(idprof int(11) not null, 
                                                nomeprof varchar(100) not null,
                                                telprof varchar(30) not null,
                                                enderprof varchar(50) not null,
                                                cpfprof varchar(30) not null,
                                                cursoprof varchar(30) not null,
                                                primary key (idprof))"""

    #Criar cursor e executar SQL no banco de dados:
    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela de professores criada com sucesso!")

except mysql.connector.Error as erro:
    print("Falha ao criar a tabela MySQL: {}".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada com sucesso!!! ")

print('\nPróxima aula: inserção de Registros na tabela criada.')