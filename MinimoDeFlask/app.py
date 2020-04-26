from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash:mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica


#Pasta para onde vai ficar armazenado o template
app = Flask(__name__, template_folder = './static')


#Titulo e Texto são objetos que o Jinja vai substituir na pagina HTML
@app.route('/')
def home():
	return render_template('./template.html',
						   titulo = 'Página Principal',
						   texto = 'Bem Vindo')