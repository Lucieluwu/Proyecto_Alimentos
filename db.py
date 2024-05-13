import pymysql

def conexion():
    return pymysql.connect(host = 'localhost',
                           user = 'root',
                           password = '123456',
                           db = 'donappetite')