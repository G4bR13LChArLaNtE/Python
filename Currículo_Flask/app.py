# Arquivo adivindo de modificações para transformar uma aplicação sqlite em postgresql.

from flask import Flask, render_template, request, redirect, jsonify, session as flask_session

from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as sql_session

import psycopg2

from datetime import datetime


import os
from dotenv import load_dotenv


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get('APP_KEY')
user = os.environ.get('usuario')
password = os.environ.get('senha')


pessoa = {}

# Banco de dados:

def conectar_db():
    con = psycopg2.connect(host='localhost', database='mensagens', user='postgres', password='pgs2022')
    return con

Base = declarative_base(conectar_db())

def criar_tb(sql):
    con = conectar_db()
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

sql = '''CREATE TABLE IF NOT EXISTS MSG (
                ID INTEGER PRIMARY KEY,
                NOME VARCHAR(255) NOT NULL,
                END_EMAIL VARCHAR(255) NOT NULL,
                ASSUNTO VARCHAR(255) NOT NULL,
                MENSAGEM VARCHAR(500) NOT NULL,
                DT DATE NOT NULL)'''

class Msg(Base):
    __tablename__ = 'MSG'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME',String(255), nullable=False)
    end_email = Column('END_EMAIL', String(255), nullable=False)
    assunto = Column('ASSUNTO', String(255), nullable=False)
    mensagem = Column('MENSAGEM', Text)
    dt = Column('DT', DateTime(timezone=True), server_default=func.now())

    def __init__(self, nome, end_email, assunto, mensagem, dt):
        self.nome = nome
        self.end_email = end_email
        self.assunto = assunto
        self.mensagem = mensagem
        self.dt = dt


criar_tb(sql)


def inserir_db(sql):
    con = conectar_db()
    cur = con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

def consultar_db(sql):
  con = conectar_db()
  cur = con.cursor()
  cur.execute(sql)
  recset = cur.fetchall()
  registros = []
  for rec in recset:
    registros.append(rec)
  con.close()
  return registros


# Rotas da parte de login:

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg_erro1 = ''
    msg_erro2 = ''
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == user and senha == password:
            flask_session['usuario'] = usuario
            return redirect('tabela')
        else:
            msg_erro1 = "Usuário ou senha inválidos!"
            msg_erro2= "Tente novamente."
    return render_template('user/login.html', erro1=msg_erro1, erro2=msg_erro2)

@app.route('/tabela', methods=['GET'])
def tabela():
    sql = ''' select * from msg'''
    pessoas = []
    p = {}
    result = consultar_db(sql)
    print(result)
    for i in result:
            p = { "nome": i[1], "email": i[2], "assunto": i[3], "mensagem": i[4], "dt": i[5]}
            pessoas.append(p)
    if 'usuario' in flask_session and len(pessoas) != 0:
        nome_user = ''
        if flask_session['usuario'] == 'charlante':
            nome_user = 'Charlante'
        return render_template('user/tabela.html', nome=nome_user, dic=pessoas)
    elif 'usuario' in flask_session and len(pessoas) == 0:
        if flask_session['usuario'] == 'charlante':
            nome_user = 'Charlante'
        return render_template('user/tabela.html', nome=nome_user, dic='')
    else:
        return redirect('login')

# Deletando dados da tabela:

@app.route("/tabela", methods=['POST'])
def delete():
    session = sql_session()
    if 'usuario' in flask_session:
        session.query(Msg).delete()
        session.commit()
        if flask_session['usuario'] == "charlante":
            return redirect('tabela')
    else:
        return redirect('login')
        

@app.route('/logout')
def sair():
    flask_session.clear()
    return redirect('login')


# Rotas do site:

@app.route('/index.html')
@app.route('/sobre')
@app.route('/')
def index():
    return render_template('site/index.html')

@app.route('/experiencia.html')
@app.route('/experiencia')
def experiencia():
    return render_template('site/experiencia.html')

@app.route('/educacao.html')
@app.route('/educacao')
def educacao():
    return render_template('site/educacao.html')

@app.route('/habilidades.html')
@app.route('/habilidades')
def habilidades():
    return render_template('site/habilidades.html')

@app.route('/interesse.html')
@app.route('/interesses')
def interesse():
    return render_template('site/interesse.html')

@app.route('/contato.html')
@app.route('/contato')
def contato():
    return render_template('site/contato.html')

# Enviou dos dados do formulário:

@app.route('/contato', methods=['POST'])
def enviar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('end_email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')
        dt = str(datetime.today())

        if (nome == '') or (email == '') or (assunto == '') or (mensagem == ''):
            try:
                return redirect("/erro", code=302)
            except Exception as ex:
                return jsonify({"status":"ERRO", "msg":str(ex)})
        else:
           sql = ''' 
           INSERT into msg(nome, end_email, assunto, mensagem, dt)
           values('{}', '{}', '{}', '{}', '{}');
           '''.format( nome, email, assunto, mensagem, dt)
           inserir_db(sql)
           return redirect("/sucesso", code=302)


@app.route('/sucesso')
def get():
    return render_template("site/sucesso.html")

@app.route('/erro')
def erro():
     return render_template("site/erro.html")


# Rodando o aplicativo:

if __name__ == '__main__':
    app.run(host= 'localhost', port= 9000)

