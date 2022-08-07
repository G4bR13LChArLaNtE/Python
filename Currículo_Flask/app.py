from flask import Flask, render_template, request, redirect, jsonify, session as flask_session

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as sql_session

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

engine = create_engine("sqlite:///mensagens.db?check_same_thread=False")
connection = engine.connect()


Base = declarative_base(engine)



connection.execute("""CREATE TABLE IF NOT EXISTS MSG (
                    ID INTEGER PRIMARY KEY,
                    NOME VARCHAR(255) NOT NULL,
                    END_EMAIL VARCHAR(255) NOT NULL,
                    ASSUNTO VARCHAR(255) NOT NULL,
                    MENSAGEM VARCHAR(500) NOT NULL,
                    DT DATE NOT NULL)""")

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
    session = sql_session()
    pessoas = []
    p = {}
    result = session.query(Msg)
    for i in result:
            p = { "nome": i.nome, "email": i.end_email, "assunto": i.assunto, "mensagem": i.mensagem, "dt": i.dt}
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
    session = sql_session()
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('end_email')
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')
        dt = datetime.today()

        if (nome == '') or (email == '') or (assunto == '') or (mensagem == ''):
            try:
                return redirect("/erro", code=302)
            except Exception as ex:
                return jsonify({"status":"ERRO", "msg":str(ex)})
        else:
           p = Msg(nome, email, assunto, mensagem, dt)
           session.add(p)
           session.commit()
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
