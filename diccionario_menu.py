class Diccionarios:
    def __init__(self):
        self.diccionarios = []

    def imprimirLlaves(self, diccionario):
        for key in diccionario:
            print(key)

    def imprimirValores(self, diccionario): 
        for key in diccionario:
            print(diccionario[key])

    def insertarValor(self, diccionario, key, value):
        diccionario[key] = value

    def modificarValor(self, diccionario, key, value):
        if key in diccionario:
            diccionario[key] = value
        else:
            print(f"La clave '{key}' no existe en el diccionario.")

    def modificarLlave(self, diccionario, old_key, new_key):
        if old_key in diccionario:
            diccionario[new_key] = diccionario.pop(old_key)
        else:
            print(f"La clave '{old_key}' no existe en el diccionario.")

    def quitarValor(self, diccionario, key):
        diccionario.pop(key, None)

    def eliminarDiccionario(self, indice):
        if 0 <= indice < len(self.diccionarios):
            self.diccionarios.pop(indice)
            print("Diccionario eliminado exitosamente.")
        else:
            print("Índice no válido.")

def menu():
    objeto = Diccionarios()
    
    while True:
        print("\nMenú Principal:")
        print("1. Crear nuevo diccionario")
        print("2. Seleccionar diccionario existente")
        print("3. Eliminar diccionario existente")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nuevo_diccionario = {}
            print("Introduce los valores iniciales:")
            while True:
                key = input("Clave (deja en blanco para terminar): ")
                if key == "":
                    break
                value = input("Valor: ")
                nuevo_diccionario[key] = value
            objeto.diccionarios.append(nuevo_diccionario)
            print("Diccionario añadido exitosamente.")
        elif opcion == "2":
            if not objeto.diccionarios:
                print("No hay diccionarios disponibles. Crea uno primero.")
                continue
            print("\nDiccionarios disponibles:")
            for i, dic in enumerate(objeto.diccionarios):
                print(f"{i + 1}. {dic}")
            indice = int(input("Selecciona un diccionario (número): ")) - 1
            if 0 <= indice < len(objeto.diccionarios):
                sub_menu(objeto, objeto.diccionarios[indice])
            else:
                print("Índice no válido.")
        elif opcion == "3":
            if not objeto.diccionarios:
                print("No hay diccionarios disponibles. Crea uno primero.")
                continue
            print("\nDiccionarios disponibles:")
            for i, dic in enumerate(objeto.diccionarios):
                print(f"{i + 1}. {dic}")
            indice = int(input("Selecciona el diccionario a eliminar (número): ")) - 1
            objeto.eliminarDiccionario(indice)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def sub_menu(objeto, diccionario):
    while True:
        print("\nSubmenú del Diccionario:")
        print("1. Imprimir llaves")
        print("2. Imprimir valores")
        print("3. Insertar valor")
        print("4. Modificar valor")
        print("5. Modificar llave")
        print("6. Quitar valor")
        print("0. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            objeto.imprimirLlaves(diccionario)
        elif opcion == "2":
            objeto.imprimirValores(diccionario)
        elif opcion == "3":
            key = input("Ingresa la clave: ")
            value = input("Ingresa el valor: ")
            objeto.insertarValor(diccionario, key, value)
        elif opcion == "4":
            key = input("Ingresa la clave a modificar: ")
            value = input("Ingresa el nuevo valor: ")
            objeto.modificarValor(diccionario, key, value)
        elif opcion == "5":
            old_key = input("Ingresa la clave a modificar: ")
            new_key = input("Ingresa la nueva clave: ")
            objeto.modificarLlave(diccionario, old_key, new_key)
        elif opcion == "6":
            key = input("Ingresa la clave a quitar: ")
            objeto.quitarValor(diccionario, key)
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == '__main__':
    menu()
