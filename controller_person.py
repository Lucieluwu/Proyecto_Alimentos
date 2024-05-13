from db import conexion

def create(ci, nombre, paterno, materno, celular, naci, direccion, sexo):
    conn = conexion()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO persona VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (ci, nombre, paterno, materno, celular, direccion, sexo, naci))
        conn.commit()
        conn.close()
        
def obtener_personas():
    conn = conexion()
    personas = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM persona')
        personas = cursor.fetchall()
    conn.close()
    return personas

def eliminar_persona(id):
    conexion = conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM persona WHERE ci = %s", (id,))
    conexion.commit()
    conexion.close()
    
def obtener_persona_por_id(id):
    conexion = conexion()
    persona = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM persona WHERE ci = %s", (id,))
        persona = cursor.fetchone()
    conexion.close()
    return persona

def actualizar_persona(id, nombre, paterno, materno, celular, naci, direccion, sexo):
    conexion = conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE persona SET ci = %s, nombre = %s, paterno = %s, materno = %s, celular = %s naci = %s, direccion = %s, sexo = %s WHERE ci = %s",
                       (id, nombre, paterno, materno, celular, naci, direccion, sexo))
    conexion.commit()
    conexion.close()