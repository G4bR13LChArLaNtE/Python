#Aqui temos a conexão entre Python e o MySQL utilizando o conector mysql.connector: 
import mysql.connector
from mysql.connector import Error

''' A seguir temos a variável utilizada para conectar o Pycharm ao MySQL:'''
con = mysql.connector.connect(host = 'localhost', database = 'cadastro', user = 'root', password = '')

if con.is_connected(): #Se a conexão estiver correta: Buscasse as informações do banco de dados.
    db_info = con.get_server_info()
    print("Conectou ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)


try:
    consulta_sql = "select * from cursos;"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando as informações dos nossos cursos""\n")
    for linha in linhas:
        print("idcurso:", linha[0])
        print("nome:", linha[1])
        print("descriução:", linha[2])
        print("carga:", linha[3])
        print("totaulas:", linha[4])
        print("ano:", linha[5], "\n")

except Error as e:
    print('Erro ao acessar tabela MySQL', e)
finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")

