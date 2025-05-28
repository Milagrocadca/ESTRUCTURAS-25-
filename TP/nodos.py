from conexion import Conexion

class Nodo:
    def __init__(self, nombre, modos):

        #nombre= Nombre de la ciudad
        #modos= modos de transporte habilitados (list o set)
        
        self.nombre = nombre
        self.modos = set(modos)
        self.conexiones = []

    def agregar_conexion(self, conexion):
        self.conexiones.append(conexion)

    def tiene_modo(self, modo):
        return modo in self.modos

    def __repr__(self):
        return f"Nodo({self.nombre}, modos={self.modos})"



class RedTransporte:
    def __init__(self):
        self.nodos: Dict[str, Nodo] = {}
        self.conexiones: List[Conexion] = []

    def agregar_nodo(self, nodo: Nodo):
        self.nodos[nodo.nombre] = nodo

    def agregar_conexion(self, conexion: Conexion):
        if conexion.origen not in self.nodos or conexion.destino not in self.nodos:
            raise ValueError("Nodo origen o destino no existe en la red.")
        self.conexiones.append(conexion)

    def obtener_conexiones_desde(self, ciudad: str, modo: str) -> List[Conexion]:
        return [
            c for c in self.conexiones
            if c.origen == ciudad and c.modo == modo
        ]