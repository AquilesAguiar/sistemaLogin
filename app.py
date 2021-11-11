from flask import Flask,render_template,redirect,request,flash
from controllers.controleUsuarios import *
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/logar',methods=["POST"])
def logar():
    email = request.form['Email']
    senha = request.form['Senha']
    ctrlUser = logarUsuario(email,senha)

    if ctrlUser == True:
        user = dadosUser(email,senha)
        return render_template('logado.html',user=user)

    flash('Email ou senha errados')
    return redirect("/")

@app.route('/registro')
def registro():
    return render_template('registro.html',)

@app.route('/cadastro',methods=['POST'])
def cadastro():
    nome = request.form['Nome']
    idade = request.form['Idade']
    email = request.form['Email']
    senha = request.form['Senha']
    ctrlUser = adicionarUser(nome,idade,email,senha)

    if ctrlUser == True:
        return redirect("/")

    flash('Este email já está sendo utilizado')
    return redirect("/registro")

if __name__ == '__main__':
    app.run(debug=True)



