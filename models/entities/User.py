from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, rol, nom_user, correo, password) -> None:
        self.id = id
        self.rol = rol
        self.nom_user = nom_user
        self.correo = correo
        self.password = password

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)