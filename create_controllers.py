from db import conexion
from werkzeug.security import generate_password_hash, check_password_hash

def crear_persona(ci, nombre, paterno, materno, celular, naci, direccion, sexo):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO persona VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (ci, nombre, paterno, materno, celular, direccion, sexo, naci))
        conn.commit()
        conn.close()
        
def crear_org(nombre, contacto, departamento, tipo):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO organizacion(nombre, contacto, departamento, tipo) VALUES(%s, %s, %s, %s, %s)", (nombre, contacto, departamento, tipo))
        conn.commit()
    conn.close()

def crear_voluntario(rol, nom_user, correo, password, r_password, horario, ci):
    text = 'Contraseña no coincide'
    conn = conexion()
    if password == r_password:
        hashed_ps = generate_password_hash(password)
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO usuario(rol, nom_user, correo, password, ci) VALUES(%s, %s, %s, %s, %s)", (rol, nom_user, correo, hashed_ps, ci))
            conn.commit()
            idus = cursor.lastrowid
            cursor.execute("INSERT INTO voluntario(iduser, horario) VALUES(%s, %s)", (idus, horario))
            conn.commit()
    else:
        conn.close()
        
        
def crear_usuario(rol, nom_user, correo, password, r_password, ci):
    text = 'Contraseña no coincide'
    conn = conexion()
    if password == r_password:
        hashed_ps = generate_password_hash(password)
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO usuario(rol, nom_user, correo, password, ci) VALUES(%s, %s, %s, %s, %s)", (rol, nom_user, correo, hashed_ps, ci))
            conn.commit()
            conn.close()
    else:
        conn.close()

def crear_alim_inv(nombre, descripcion, categoria, fecha_ven, tipo, peso, estado, stock):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO alimento(nombre, descripcion, categoria, fecha_ven, tipo, peso, estado, stock) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (nombre, descripcion, categoria, fecha_ven, tipo, peso, estado, stock))
        conn.commit()
        id = cursor.lastrowid
        conn.close()
    return id

def crear_contiene(iddona, idalim, cantidad):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO contiene(iddona, idalim, cantidad) VALUES(%s, %s, %s)", (iddona, idalim, cantidad))
        conn.commit()
        conn.close()

def crear_realiza(iduser, iddona, idact):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO realiza(iduser, iddona, idact, fecha, hora) VALUES(%s, %s, %s, CURDATE(), CURTIME())", (iduser, iddona, idact))
        conn.commit()
        conn.close()

def crear_donacion(tipo):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO donacion(tipo, fecha) VALUES(%s, NOW())", (tipo))
        conn.commit()
        id = cursor.lastrowid
        conn.close()
    return id

def crear_solicitud(iduser, iddona, idact):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO solicita(iduser, iddona, idact, fecha, hora) VALUES(%s, %s, %s,CURDATE(), CURTIME())", (iduser, iddona, idact))
        conn.commit()
        conn.close()

def crear_actividad(descripcion, tipo, estado):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO actividad(descripcion, tipo, estado, fecha_limite) VALUES(%s, %s, %s, DATE_ADD(CURRENT_DATE(), INTERVAL 4 DAY))", (descripcion, tipo, estado))
        conn.commit()
        id = cursor.lastrowid
        conn.close()
    return id