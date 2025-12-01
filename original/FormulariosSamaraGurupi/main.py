from flask import Flask, render_template, request

app = Flask(__name__)


# Rota para a página de formulário GET
@app.route('/')
def form_get():    
    return render_template('form_get.html')

# Rota para processar o formulário GET
@app.route('/resultado_get', methods=['GET'])
def resultado_get():
    nome = request.args.get('nome') 
    email = request.args.get('email') 
    idade = request.args.get('idade') 
    comentario = request.args.get('comentario')
    aceita_regras = request.args.get('aceita_regras')
    aceita_regras_texto = 'Sim' if aceita_regras == 'on' else 'Não'
    return render_template('resultado_get.html', nome=nome, email=email, idade=idade, comentario=comentario, aceita_regras=aceita_regras_texto)

# Rota para a página de formulário POST 
@app.route('/form_post')  
def form_post():
    return render_template('form_post.html')

# Rota para processar o formulário POST    
@app.route('/resultado_post', methods=['POST']) 
def resultado_post():
    usuario = request.form['usuario']
    senha = request.form['senha']
    descricao = request.form['descricao']
    return render_template('resultado_post.html', usuario = usuario, senha = senha, descricao = descricao)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
