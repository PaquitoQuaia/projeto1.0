from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for
)

import mysql.connector
import os

from mysql.connector import Error

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


# =========================================================
# CONFIGURAÇÃO
# =========================================================

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = "truck_parts_chave"


# =========================================================
# CONEXÃO COM MYSQL
# =========================================================

def conectar_banco():

    return mysql.connector.connect(
       host=os.getenv("MYSQL_HOST", "127.0.0.1"),
       user=os.getenv("MYSQL_USER", "root"),
       password=os.getenv("MYSQL_PASSWORD", "senai105"),
       database=os.getenv("MYSQL_DATABASE", "DB_truck_prts")
    )


def fechar_banco(conexao, cursor):

    if cursor:
        cursor.close()

    if conexao:
        conexao.close()

