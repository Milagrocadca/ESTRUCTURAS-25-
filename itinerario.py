from validaciones import *

from collections import deque

class Itinerario:
    def __init__(self):
        self.tareas = []  # Lista de tuplas (id, descripcion, prioridad)
        self.tareas_dict = {}  # Diccionario para acceso rápido
        self.tareas_set = set()  # Conjunto para evitar duplicados por descripción
        self.cola_urgentes = deque()  # Cola para tareas con prioridad alta
        self.historial_completadas = []  # Pila para tareas completadas

    def agregar(self, id, descripcion, prioridad):
        if descripcion in self.tareas_set:
            print(" Tarea duplicada. No se agregó.")
            return

        tarea = (id, descripcion, prioridad)
        self.tareas.append(tarea)
        self.tareas_dict[id] = tarea
        self.tareas_set.add(descripcion)

        if prioridad == "alta":
            self.cola_urgentes.append(tarea)

        print(f"Tarea agregada: {tarea}")

    def mostrar(self):
        print("\nTareas pendientes:")
        for tarea in self.tareas:
            print(f"- ID {tarea[0]}: {tarea[1]} ({tarea[2]})")

        if self.cola_urgentes:
            print("\nTareas urgentes:")
            for t in self.cola_urgentes:
                print(f"‼ID {t[0]}: {t[1]}")

    def completar(self, id):
        tarea = self.tareas_dict.pop(id, None)
        if not tarea:
            print("No se encontró la tarea con ese ID")
            return

        self.tareas.remove(tarea)
        self.tareas_set.remove(tarea[1])
        if tarea in self.cola_urgentes:
            self.cola_urgentes.remove(tarea)

        self.historial_completadas.append(tarea)
        print(f"Tarea completada: {tarea}")

    def historial(self):
        print("\nHistorial de tareas completadas:")
        for tarea in reversed(self.historial_completadas):
            print(f"- ID {tarea[0]}: {tarea[1]} ({tarea[2]})")
