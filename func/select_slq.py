import database.db as data

def procura_cliente(tel):
    data.cursor.execute("SELECT * from user WHERE tel_cel like '%?%';", (tel))
    num_row = data.cursor.fetchone()
    if num_row is None:
        return False
    else:
        return True
