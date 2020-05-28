"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
Descrição..: Esse arquivo faz conexão com o banco de dados
"""
import sqlite3


path = "database/pizza.db"

db = sqlite3.connect(path)

cursor = db.cursor()
