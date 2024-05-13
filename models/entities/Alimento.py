class Alimento():
    def __init__(self, idalim, nombre, descripcion, categoria, fecha_ven, tipo, peso, estado, stock):
        self.id = idalim
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.fecha_ven = fecha_ven
        self.tipo = tipo
        self.peso = peso
        self.estado = estado
        self.stock = stock