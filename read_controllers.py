from db import conexion

def obtener_personas():
    conn = conexion()
    personas = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM persona')
        personas = cursor.fetchall()
    conn.close()
    return personas

def obtener_orgs():
    conn = conexion()
    orgs = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM organizacion')
        orgs = cursor.fetchall()
    conn.close()
    return orgs

def obtener_users():
    conn = conexion()
    users = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM usuario')
        users = cursor.fetchall()
    conn.close()
    return users

def obtener_alimentos():
    conn = conexion()
    alims = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM alimento')
        alims = cursor.fetchall()
    conn.close()
    return alims


def obtener_realiza():
    conn = conexion()
    donas = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT iduser, iddona, idact, fecha, hora, obt_estado(idact), nom_user(iduser) FROM realiza')
        donas = cursor.fetchall()
    conn.close()
    return donas


def obtener_solicita():
    conn = conexion()
    sol = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT iduser, iddona, idact, fecha, hora, obt_estado(idact), nom_user(iduser) FROM solicita')
        sol = cursor.fetchall()
    conn.close()
    return sol

def obtener_actividad():
    conn = conexion()
    act = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM actividad')
        act = cursor.fetchall()
    conn.close()
    return act

def obtener_actividad_id(id):
    conn = conexion()
    act = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM actividad WHERE idvol = %s', (id))
        act = cursor.fetchall()
    conn.close()
    return act

def obtener_voluntario():
    conn = conexion()
    vols = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT iduser, nom_user(iduser) FROM voluntario')
        vols = cursor.fetchall()
    conn.close()
    return vols

def obtener_contenido_donacion(iddona):
    conn = conexion()
    contenido = []
    with conn.cursor() as cursor:
        cursor.execute("""SELECT A.idalim, A.nombre, A.stock, A.tipo
                        FROM Alimento A, Donacion D, Contiene C
                        WHERE A.idalim = C.idalim AND D.iddona = {} AND C.iddona = {}""".format(iddona, iddona))
        contenido = cursor.fetchall()
    conn.close()
    return contenido
