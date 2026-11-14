import sqlite3

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # Parâmetros via placeholders, nunca concatenação
    query = "SELECT * FROM usuarios WHERE username = ? AND senha = ?"

    cursor.execute(query, (usuario, senha))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return "Acesso Permitido"
    else:
        return "Acesso Negado"
