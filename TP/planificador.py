
from collections import deque
from math import ceil

class Planificador:
    def __init__(self):
        self.nodos = {}

    # tiene todas los y vehiculos
    # me fijo si existe la conexion unica y sino intermediario
    # llamar las def que creemos en nodo

    def crearRutas(self, origen, destino, tipo):
        pass  # TODO: implementar

    def buscar_rutas(self, solicitud):
        pass  # TODO: implementar

def evaluar_ruta(ruta, vehiculo, peso, nodos):
    tiempo_total = 0
    costo_total = 0
    for tramo in ruta:
        if not (nodos[tramo.origen].tiene_modo(vehiculo.modo) and
                nodos[tramo.destino].tiene_modo(vehiculo.modo)):
            return None

        if not vehiculo.puede_recorrer(tramo, peso):
            return None

        # Velocidad efectiva
        velocidad = tramo.vel_max if tramo.vel_max else vehiculo.velocidad

        # Cantidad de vehículos necesarios
        cantidad = ceil(peso / vehiculo.capacidad)

        # Calcular tiempo y costo
        tiempo_tramo = tramo.distancia / velocidad
        costo_tramo = vehiculo.calcular_costo_total(tramo.distancia, peso)

        tiempo_total += tiempo_tramo
        costo_total += costo_tramo * cantidad

    return {
        "ruta": ruta,
        "vehiculo": vehiculo,
        "modo": vehiculo.modo,
        "tiempo_total": round(tiempo_total, 2),
        "costo_total": round(costo_total, 2)
    }