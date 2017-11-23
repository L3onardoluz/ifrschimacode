import flask
import sqlite3

DB = 'pessoa.sqlite'

app = flask.Flask("chimacode")

def select_all():
	conn = sqlite3.connect(DB)
	severino = conn.cursor()
	
	query = "SELECT * FROM usuario"
	
	resultado = severino.execute(query)
	
	usuarios = resultado.fetchall()
	
	conn.close()
	
	return usuarios

@app.route('/users', methods=['GET'])
def busca_usuarios():
	usuarios = select_all()
	return flask.jsonify(usuarios)
	
if __name__ == "__main__":
	app.run(debug=True)