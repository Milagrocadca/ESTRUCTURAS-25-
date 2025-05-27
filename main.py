from collections import deque


def main():
    resultado = Itinerario()

    seguir=True
    while seguir:
        print("\n===== MENÚ PLANIFICADOR =====")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("ID de la tarea: "))
                descripcion = input("Descripción: ")
                prioridad = input("Prioridad (alta/media/baja): ").lower()
                resultado.agregar(id, descripcion, prioridad)
            except ValueError:
                print("ID debe ser un número entero.")

        elif opcion == "2":
            resultado.mostrar()

        elif opcion == "3":
            try:
                id = int(input("ID de la tarea a completar: "))
                resultado.completar(id)
            except ValueError:
                print("ID inválido.")
        
        elif opcion == "4":
            resultado.historial()

        elif opcion == "5":
            print("Saliendo del planificador.")
            seguir=False

        else:
            print("Opción inválida. Intente de nuevo.")

# -------------------- EJECUCIÓN --------------------

if __name__ == "__main__":
    main()