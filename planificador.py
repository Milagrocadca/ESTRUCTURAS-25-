
from collections import deque

# Tarea como tupla: (id, descripcion, prioridad)
# Lista de tareas (array)
tareas = []

# Diccionario para acceder rápido por ID
tareas_dict = {}

# Conjunto para evitar tareas duplicadas (por descripción)
tareas_set = set()

# Cola para tareas urgentes (FIFO)
cola_urgentes = deque()

# Pila para historial de completadas (LIFO)
historial_completadas = []

# --------------------- Funciones ---------------------

def agregar_tarea(id, descripcion, prioridad):
    if descripcion in tareas_set:
        raise ValueError ("La trea dse encuentra uplicada, no se puede agregar.")
    
    tarea = (id, descripcion, prioridad)
    tareas.append(tarea)
    tareas_dict[id] = tarea
    tareas_set.add(descripcion)
    
    if prioridad == "alta":
        cola_urgentes.append(tarea)
    
    print("Tarea agregada:", tarea)

def mostrar_tareas():
    print("\n Tareas pendientes:")
    for tarea in tareas:
        print(f"- {tarea}")
        
    if cola_urgentes:
        print("\n Tareas urgentes:")
        for t in cola_urgentes:
            print(f" {t}")

def completar_tarea(id):
    tarea = tareas_dict.pop(id, None)
    if tarea:
        tareas.remove(tarea)
        tareas_set.remove(tarea[1])
        if tarea in cola_urgentes:
            cola_urgentes.remove(tarea)
        historial_completadas.append(tarea)
        print("Tarea completada:", tarea)
    else:
        print("No se encontró la tarea con ese ID")

def mostrar_historial():
    print("\n Historial de tareas completadas:")
    for tarea in reversed(historial_completadas):
        print(f"- {tarea}")

# --------------------- Pruebas ---------------------

agregar_tarea(1, "Enviar informe", "media")
agregar_tarea(2, "Reunión con equipo", "alta")
agregar_tarea(3, "Actualizar software", "baja")
agregar_tarea(4, "Enviar informe", "alta")  # Duplicada

mostrar_tareas()

completar_tarea(2)
mostrar_historial()
mostrar_tareas()




