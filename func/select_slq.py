import database.db as data

def procura_cliente(tel):
    data.cursor.execute('SELECT * from user WHERE tel_cel like "%{}%"'.format(tel))
    num_row = data.cursor.fetchone()
    if num_row is None:
        return False
    else:
        return num_row[0]

def ultimos_pedidos():
    pass