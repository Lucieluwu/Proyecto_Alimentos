from db import conexion

def crear_org(nombre, ubicacion, departamento, tipo):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO organizacion VALUES(%s, %s, %s, %s)", (nombre, ubicacion, departamento, tipo,))
        conn.commit()
        conn.close()
        
def mostrar_org():
    conn = conexion()
    orgs = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM organizacion')
        orgs = cursor.fetchall()
    conn.close()
    return orgs

def mostrar_user():
    conn = conexion()
    users = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM usuario')
        users = cursor.fetchall()
    conn.close()
    return users



