from .entities.Alimento import Alimento

class ModelAlimento():

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT * FROM usuario
            WHERE idalim = '{}'""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                alim = Alimento(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                return alim
            else:
                return None
        except Exception as ex:
            raise Exception(ex)