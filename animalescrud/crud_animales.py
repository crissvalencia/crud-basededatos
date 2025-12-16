from caballo import Caballo
from cocodrilo import Cocodrilo
from pezdeaguastempladas import pezdeaguastempladas
from insecto import insecto
from pato import pato

# Array principal para el inventario de animales
lista_animales = []

def mostrar_menu():
    print("\n" + "=" * 55)
    print("SISTEMA DE GESTION DE ANIMALES")
    print("=" * 55)
    print("1. Registrar nuevo animal")
    print("2. Ver todos los animales")
    print("3. Buscar animal por nombre")
    print("4. Actualizar informacion de animal")
    print("5. Eliminar animal de la lista")
    print("6. Ordenar animales por peso")
    print("7. Invertir orden de la lista")
    print("8. Estadisticas de la lista")
    print("9. Filtrar por habitat")
    print("10. Salir del sistema")
    print("=" * 55)

def registrar_animal():
    print("\n--- REGISTRO DE ANIMAL ---")
    print("Tipo de animal:")
    print("1. Caballo")
    print("2. Cocodrilo")
    print("3. Pez de aguas templadas")
    print("4. Insecto")
    print("5. Pato")
    
    tipo = input("\nEscoja el tipo: ")
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    habitat = input("Habitat: ")
    dieta = input("Dieta: ")
    tamano = input("Tamaño: ")
    color = input("Color: ")
    peso = float(input("Peso (kg): "))
    
    if tipo == "1":
        pelaje = input("Pelaje: ")
        domesticado = input("Es domesticado? (si/no): ").lower() == "si"
        animal = Caballo(nombre, edad, habitat, dieta, tamano, color, peso, pelaje, domesticado)
        lista_animales.append(animal)
        print(f"\nCaballo {nombre} registrado con exito!")
        
    elif tipo == "2":
        venenoso = input("Es venenoso? (si/no): ").lower() == "si"
        longitud = float(input("Longitud (m): "))
        animal = Cocodrilo(nombre, edad, habitat, dieta, tamano, color, peso, venenoso, longitud)
        lista_animales.append(animal)
        print(f"\nCocodrilo {nombre} registrado!")
        
    elif tipo == "3":
        forma_escama = input("Forma de escama: ")
        venenoso = input("Es venenoso? (si/no): ").lower() == "si"
        animal = pezdeaguastempladas(nombre, edad, habitat, dieta, tamano, color, peso, forma_escama, venenoso)
        lista_animales.append(animal)
        print(f"\nPez de aguas templadas {nombre} registrado!")
        
    elif tipo == "4":
        textura = input("Textura: ")
        num_patas = int(input("Numero de patas: "))
        animal = insecto(nombre, edad, habitat, dieta, tamano, color, peso, textura, num_patas)
        lista_animales.append(animal)
        print(f"\nInsecto {nombre} registrado!")
        
    elif tipo == "5":
        puede_volar = input("Puede volar? (si/no): ").lower() == "si"
        tipo_plumaje = input("Tipo de plumaje: ")
        animal = pato(nombre, edad, habitat, dieta, tamano, color, peso, puede_volar, tipo_plumaje)
        lista_animales.append(animal)
        print(f"\nPato {nombre} registrado!")

def ver_animales():
    print("\n--- LISTA DE ANIMALES ---")
    
    if len(lista_animales) == 0:
        print("No hay animales registrados en la lista.")
        return
    
    for idx, animal in enumerate(lista_animales):
        print(f"\n[{idx}] ====================")
        print(f"Nombre: {animal.nombre}")
        print(f"Edad: {animal.edad}")
        print(f"Habitat: {animal.habitat}")
        print(f"Dieta: {animal.dieta}")
        print(f"Tamaño: {animal.tamano}")
        print(f"Color: {animal.color}")
        print(f"Peso: {animal.peso} kg")
        
        if isinstance(animal, Caballo):
            print(f"TIPO: Caballo")
            print(f"Pelaje: {animal.pelaje}")
            print(f"Domesticado: {'Si' if animal.domesticado else 'No'}")
            
        elif isinstance(animal, Cocodrilo):
            print(f"TIPO: Cocodrilo")
            print(f"Venenoso: {'Si' if animal.venenoso else 'No'}")
            print(f"Longitud: {animal.longitud} m")
            
        elif isinstance(animal, pezdeaguastempladas):
            print(f"TIPO: Pez de aguas templadas")
            print(f"Forma de escama: {animal.forma_escama}")
            print(f"Venenoso: {'Si' if animal.venenoso else 'No'}")
            
        elif isinstance(animal, insecto):
            print(f"TIPO: Insecto")
            print(f"Textura: {animal.textura}")
            print(f"Numero de patas: {animal.num_patas}")
            
        elif isinstance(animal, pato):
            print(f"TIPO: Pato")
            print(f"Puede volar: {'Si' if animal.puede_volar else 'No'}")
            print(f"Tipo de plumaje: {animal.tipo_plumaje}")

def buscar_animal():
    print("\n--- BUSCAR ANIMAL ---")
    busqueda = input("Ingrese nombre a buscar: ").lower()
    
    resultados = []
    for i, animal in enumerate(lista_animales):
        if busqueda in animal.nombre.lower():
            resultados.append((i, animal))
    
    if len(resultados) == 0:
        print(f"No se encontraron animales con '{busqueda}' en el nombre")
    else:
        print(f"\nSe encontraron {len(resultados)} animal(es):")
        for indice, animal in resultados:
            print(f"\n[{indice}] {animal.nombre} - {animal.color} - {animal.habitat}")

def actualizar_animal():
    print("\n--- ACTUALIZAR ANIMAL ---")
    ver_animales()
    
    if len(lista_animales) == 0:
        return
    
    try:
        indice = int(input("\nIndice del animal a actualizar: "))
        
        if indice < 0 or indice >= len(lista_animales):
            print("Indice fuera de rango")
            return
        
        animal = lista_animales[indice]
        
        print("\nQue desea actualizar?")
        print("1. Color")
        print("2. Habitat")
        print("3. Dieta")
        print("4. Peso")
        
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            nuevo_color = input("Nuevo color: ")
            animal.color = nuevo_color
            print(f"Color actualizado a {nuevo_color}")
            
        elif opcion == "2":
            nuevo_habitat = input("Nuevo habitat: ")
            animal.habitat = nuevo_habitat
            print(f"Habitat actualizado a {nuevo_habitat}")
            
        elif opcion == "3":
            nueva_dieta = input("Nueva dieta: ")
            animal.dieta = nueva_dieta
            print(f"Dieta actualizada a {nueva_dieta}")
            
        elif opcion == "4":
            nuevo_peso = float(input("Nuevo peso (kg): "))
            animal.peso = nuevo_peso
            print(f"Peso actualizado a {nuevo_peso} kg")
            
    except ValueError:
        print("Entrada invalida")

def eliminar_animal():
    print("\n--- ELIMINAR ANIMAL ---")
    ver_animales()
    
    if len(lista_animales) == 0:
        return
    
    print("\nOpciones de eliminacion:")
    print("1. Eliminar por indice")
    print("2. Eliminar el ultimo animal")
    print("3. Eliminar el primer animal")
    
    opcion = input("Seleccione: ")
    
    try:
        if opcion == "1":
            indice = int(input("Indice a eliminar: "))
            eliminado = lista_animales.pop(indice)
            print(f"\n{eliminado.nombre} eliminado de la lista!")
            
        elif opcion == "2":
            eliminado = lista_animales.pop()
            print(f"\nUltimo animal ({eliminado.nombre}) eliminado!")
            
        elif opcion == "3":
            eliminado = lista_animales.pop(0)
            print(f"\nPrimer animal ({eliminado.nombre}) eliminado!")
            
    except (ValueError, IndexError):
        print("Error en la eliminacion")

def ordenar_animales():
    print("\n--- ORDENAR ANIMALES ---")
    print("1. Por nombre (alfabeticamente)")
    print("2. Por edad")
    print("3. Por peso")
    
    opcion = input("Ordenar por: ")
    
    if opcion == "1":
        lista_animales.sort(key=lambda a: a.nombre)
        print("Animales ordenados por nombre!")
        
    elif opcion == "2":
        lista_animales.sort(key=lambda a: a.edad)
        print("Animales ordenados por edad!")
        
    elif opcion == "3":
        lista_animales.sort(key=lambda a: a.peso)
        print("Animales ordenados por peso!")
        
    ver_animales()

def invertir_lista():
    print("\n--- INVERTIR ORDEN ---")
    lista_animales.reverse()
    print("El orden de la lista ha sido invertido!")
    ver_animales()

def estadisticas():
    print("\n--- ESTADISTICAS DE LA LISTA ---")
    
    total = len(lista_animales)
    
    if total == 0:
        print("No hay animales para mostrar estadisticas")
        return
    
    caballos = sum(1 for a in lista_animales if isinstance(a, Caballo))
    cocodrilos = sum(1 for a in lista_animales if isinstance(a, Cocodrilo))
    peces = sum(1 for a in lista_animales if isinstance(a, pezdeaguastempladas))
    insectos = sum(1 for a in lista_animales if isinstance(a, insecto))
    patos = sum(1 for a in lista_animales if isinstance(a, pato))
    
    print(f"Total de animales: {total}")
    print(f"Caballos: {caballos}")
    print(f"Cocodrilos: {cocodrilos}")
    print(f"Peces de aguas templadas: {peces}")
    print(f"Insectos: {insectos}")
    print(f"Patos: {patos}")
    
    # Peso total
    peso_total = sum(a.peso for a in lista_animales)
    print(f"\nPeso total: {peso_total} kg")

def filtrar_habitat():
    print("\n--- FILTRAR POR HABITAT ---")
    tipo = input("Habitat a buscar: ").lower()
    
    filtrados = [a for a in lista_animales if tipo in a.habitat.lower()]
    
    if len(filtrados) == 0:
        print(f"No hay animales con habitat '{tipo}'")
    else:
        print(f"\nAnimales con {tipo}: {len(filtrados)}")
        for animal in filtrados:
            print(f"- {animal.nombre} ({animal.color})")

def iniciar_sistema():
    # Agregar animales de ejemplo
    lista_animales.append(Caballo("Trueno", 7, "montaña", "hierba", "mediano", "blanco", 55, "ondulado", False))
    lista_animales.append(Cocodrilo("Mordisco", 15, "pantano", "carnívoro", "enorme", "gris verdoso", 2500, False, 5.2))
    lista_animales.append(pezdeaguastempladas("Nemo", 2, "coral", "algas", "diminuto", "naranja", 28, "ovalada", False))
    lista_animales.append(insecto("Hércules", 1, "bosque tropical", "fruta podrida", "mediano", "café oscuro", 920, "rugoso", 4))
    lista_animales.append(pato("Cuac", 2, "laguna", "omnívoro", "pequeño", "gris", 0.65, False, "impermeable"))
    
    while True:
        mostrar_menu()
        seleccion = input("\nIngrese una opcion: ")
        
        if seleccion == "1":
            registrar_animal()
        elif seleccion == "2":
            ver_animales()
        elif seleccion == "3":
            buscar_animal()
        elif seleccion == "4":
            actualizar_animal()
        elif seleccion == "5":
            eliminar_animal()
        elif seleccion == "6":
            ordenar_animales()
        elif seleccion == "7":
            invertir_lista()
        elif seleccion == "8":
            estadisticas()
        elif seleccion == "9":
            filtrar_habitat()
        elif seleccion == "10":
            print("\nCerrando sistema...")
            break
        else:
            print("\nOpcion no valida, intente de nuevo")
        
        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    iniciar_sistema()