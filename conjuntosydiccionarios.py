# ==========================================
# Programa: Registro y Gestión de Contactos
# Estructura utilizada: Diccionario
# ==========================================

def mostrar_menu():
    print("\n--- LIBRETA DE CONTACTOS ---")
    print("1. Agregar/Actualizar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar un contacto")
    print("4. Eliminar un contacto")
    print("5. Salir")

def gestionar_contactos():
    # Creación de la colección de datos (Diccionario vacío)
    contactos = {}

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()

        # 1. Funcionalidad para insertar/agregar datos
        if opcion == "1":
            nombre = input("Ingresa el nombre del contacto: ").strip().title()
            telefono = input("Ingresa el número telefónico: ").strip()
            contactos[nombre] = telefono
            print(f" Contacto '{nombre}' guardado exitosamente.")

        # 2. Mostrar de forma clara la información almacenada
        elif opcion == "2":
            if not contactos:
                print(" La libreta de contactos está vacía.")
            else:
                print("\n LISTA DE CONTACTOS:")
                print("-" * 30)
                for nombre, telefono in contactos.items():
                    print(f" Nombre: {nombre} |  Teléfono: {telefono}")
                print("-" * 30)

        # 3. Operación adicional: Buscar
        elif opcion == "3":
            nombre = input("Ingresa el nombre a buscar: ").strip().title()
            if nombre in contactos:
                print(f" Encontrado: {nombre} ->  {contactos[nombre]}")
            else:
                print(f" El contacto '{nombre}' no existe.")

        # 4. Operación adicional: Eliminar
        elif opcion == "4":
            nombre = input("Ingresa el nombre del contacto a eliminar: ").strip().title()
            if nombre in contactos:
                del contactos[nombre]
                print(f" Contacto '{nombre}' eliminado correctamente.")
            else:
                print(f" El contacto '{nombre}' no se encuentra en la lista.")

        # 5. Salir del programa
        elif opcion == "5":
            print(" ¡Gracias por usar la libreta de contactos!")
            break
        else:
            print(" Opción no válida. Por favor, intenta de nuevo.")

# Ejecución del programa
if __name__ =="__main__" :
    gestionar_contactos()