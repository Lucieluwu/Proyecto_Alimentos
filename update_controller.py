from db import conexion
from werkzeug.security import generate_password_hash

def actualizar_pass(password, correo):
    conn = conexion()
    with conn.cursor() as cursor:
        hashed_ps = generate_password_hash(password)
        cursor.execute("UPDATE usuario WHERE correo = %s SET password = %s", (correo, hashed_ps))
    conn.commit()
    conn.close()

def actualizar_actividad(idact, idadmin, idvol, estado):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE actividad SET idadmin = %s, idvol = %s, estado = %s WHERE idact = %s", (idadmin, idvol, estado, idact))
    conn.commit()
    conn.close()
    
def actualizar_estado_actividad(idact, estado):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE actividad SET estado = %s WHERE idact = %s", (estado, idact))
    conn.commit()
    conn.close()
