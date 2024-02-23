import pymongo

# Función para establecer la conexión a MongoDB
def conectar_a_mongodb():
    cliente = pymongo.MongoClient("mongodb://localhost:27017/")
    base_de_datos = cliente["colegio"]
    return base_de_datos

# Función para crear una colección en la base de datos
def crear_coleccion(db, nombre_coleccion):
    return db.create_collection(nombre_coleccion)

# Función para insertar un documento en una colección
def insertar_documento(coleccion, documento):
    return coleccion.insert_one(documento)

# Función para buscar documentos en una colección
def buscar_documentos(coleccion, filtro):
    return coleccion.find(filtro)

# Función para actualizar documentos en una colección
def actualizar_documento(coleccion, filtro, actualizacion):
    return coleccion.update_many(filtro, actualizacion)

# Menú principal
def menu():
    db = None
    coleccion = None

    while True:
        print("\n------ Menú Principal ------")
        print("1. Conexión a la base de datos")
        print("2. Crear una colección")
        print("3. Insertar documento")
        print("4. Buscar documentos")
        print("5. Actualizar documentos")
        print("6. Buscar documentos de otra coleccion")
        print("0. Salir")

        opcion = input("Ingrese la opción deseada: ")
     #apartado a
        if opcion == "1":
            db = conectar_a_mongodb()
            print("Conexión exitosa a la base de datos.")

        #apartado b
        elif opcion == "2":
            if db==conectar_a_mongodb():
                nombre_coleccion = input("Ingrese el nombre de la colección: ")
                coleccion = crear_coleccion(db, nombre_coleccion)
                print(f"Colección '{nombre_coleccion}' creada exitosamente.")
            else:
                print("Primero debes conectar a la base de datos.")
        
        #apartado c
        elif opcion == "3":
            if coleccion is not None:
                documento = {
                 "nombre": input("Nombre del estudiante: "),
                 "edad": int(input("Edad del estudiante: ")),
                 "grado": int(input("Grado del estudiante: ")),
                 "materias": input("Materias del estudiante (separadas por comas): ").split(",")
                 }
                insertar_documento(coleccion, documento)
                print("Documento insertado exitosamente.")
            else:
                print("Primero debes crear una colección.")

        #apartado d
        elif opcion == "4":
             if coleccion is not None:
                 nombre: input("Ingrese el nombre para la búsqueda: ")
                 resultados = buscar_documentos(coleccion, nombre)
                 print("\nResultados de la búsqueda:")
                 for resultado in resultados:
                      print(resultado)
             else:
                 print("Primero debes crear una colección.")
        #apartado e
        elif opcion == "5":
            if coleccion is not None:       
                    nombre: input("Ingrese el nombre del estudiante a actualizar: ")
                    actualizacion = {
                    "$set": {
                        "edad": int(input("Nueva edad del estudiante: ")),
                        "grado": int(input("Nuevo grado del estudiante: "))
                    }
                }
                    actualizar_documento(coleccion, nombre, actualizacion)
                    print("Documentos actualizados exitosamente.")
            else:
                print("Primero debes crear una colección.")

       

if __name__ == "__main__":
    menu()