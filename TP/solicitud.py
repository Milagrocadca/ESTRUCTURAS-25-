import csv
from validaciones import *

class Solicitud:
    def __init__(self, idSolicitud:str, peso:float, origen:str, destino:str):
        if idSolicitud in Solicitud.dic_solicitud.id:
            raise ValueError('Ya una solicitud con ese ID')
        
        elif not validarPositivo(peso):
            raise ValueError ("El peso del vehiculo ingresado no se encentra dentro de las opciones disponibles")

        self.idSolicitud = str(idSolicitud)
        self.peso = float(peso)
        self.origen = origen
        self.destino = destino

    

    def __repr__(self):
        return (f"Solicitud(ID={self.idSolicitud}, "
                f"Peso={self.peso} kg, "
                f"{self.origen} → {self.destino})")

    def dic_solicitud(self):
       
        return {
            "id": self.idSolicitud,
            "peso": self.peso,
            "origen": self.origen,
            "destino": self.destino
        }


    
    def cargar_solicitudes(path):
        solicitudes = []
        with open(path, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                solicitudes.append(Solicitud(
                    row['id'], row['peso'], row['origen'], row['destino']
                ))
        return solicitudes
