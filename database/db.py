"""
Data.......: 17/05/2020
Projeto....: pizza
Arquivo....: main.py
Autor......: Samuel Mayer Rufino
"""
import sqlite3


path = "database/pizza.db"

db = sqlite3.connect(path)

cursor = db.cursor()
