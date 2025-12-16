from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio

# Lista principal para almacenar las botellas
inventario_botellas = []

def menu_principal():
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTION DE BOTELLAS")
    print("=" * 50)
    print("1. Agregar botella al inventario")
    print("2. Mostrar todas las botellas")
    print("3. Buscar botella por marca")
    print("4. Modificar botella")
    print("5. Eliminar botella")
    print("6. Ordenar botellas por capacidad")
    print("7. Invertir orden del inventario")
    print("8. Contar botellas por tipo")
    print("9. Obtener capacidad total")
    print("10. Salir")
    print("=" * 50)

def agregar_botella():
    print("\n--- AGREGAR BOTELLA ---")
    print("1. Botella Normal")
    print("2. Botella de Plastico")
    print("3. Botella de Vidrio")
    
    tipo = input("Seleccione tipo: ")
    marca = input("Marca: ")
    capacidad = input("Capacidad (ej: 500ml, 1.5L): ")
    tapa = input("Tipo de tapa: ")
    
    if tipo == "1":
        botella = Botella(marca, capacidad, tapa)
        inventario_botellas.append(botella)
        print(f"\nBotella {marca} agregada correctamente!")
        
    elif tipo == "2":
        diseno = input("Diseño: ")
        botella = Botella_plastico(marca, capacidad, tapa, diseno)
        inventario_botellas.append(botella)
        print(f"\nBotella plastica {marca} agregada correctamente!")
        
    elif tipo == "3":
        color = input("Color del vidrio: ")
        grosor = float(input("Grosor (mm): "))
        botella = Botella_vidrio(marca, capacidad, tapa, color, grosor)
        inventario_botellas.append(botella)
        print(f"\nBotella de vidrio {marca} agregada correctamente!")

def mostrar_botellas():
    print("\n--- INVENTARIO DE BOTELLAS ---")
    if len(inventario_botellas) == 0:
        print("No hay botellas en el inventario.")
        return
    
    for i, botella in enumerate(inventario_botellas):
        print(f"\n[{i}] Botella:")
        botella.imprimir_info()
        if isinstance(botella, Botella_vidrio):
            print(f"   Tipo: Vidrio - Color: {botella.color_vidrio}, Grosor: {botella.grosor}mm")
        elif isinstance(botella, Botella_plastico):
            print(f"   Tipo: Plastico - Diseño: {botella.diseno}")

def buscar_botella():
    print("\n--- BUSCAR BOTELLA ---")
    marca_buscar = input("Ingrese marca a buscar: ")
    encontradas = []
    
    for i, botella in enumerate(inventario_botellas):
        if botella.marca.lower() == marca_buscar.lower():
            encontradas.append((i, botella))
    
    if len(encontradas) == 0:
        print(f"No se encontraron botellas de la marca {marca_buscar}")
    else:
        print(f"\nSe encontraron {len(encontradas)} botella(s):")
        for indice, botella in encontradas:
            print(f"\n[{indice}]")
            botella.imprimir_info()

def modificar_botella():
    print("\n--- MODIFICAR BOTELLA ---")
    mostrar_botellas()
    
    if len(inventario_botellas) == 0:
        return
    
    try:
        indice = int(input("\nIngrese el numero de botella a modificar: "))
        if indice < 0 or indice >= len(inventario_botellas):
            print("Indice no valido")
            return
        
        botella = inventario_botellas[indice]
        print("\nQue desea modificar?")
        print("1. Marca")
        print("2. Capacidad")
        print("3. Tipo de tapa")
        
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            nueva_marca = input("Nueva marca: ")
            botella.marca = nueva_marca
        elif opcion == "2":
            nueva_capacidad = input("Nueva capacidad: ")
            botella.capacidad = nueva_capacidad
        elif opcion == "3":
            nueva_tapa = input("Nuevo tipo de tapa: ")
            botella.tapa = nueva_tapa
        
        print("\nBotella modificada correctamente!")
        botella.imprimir_info()
        
    except ValueError:
        print("Entrada no valida")

def eliminar_botella():
    print("\n--- ELIMINAR BOTELLA ---")
    mostrar_botellas()
    
    if len(inventario_botellas) == 0:
        return
    
    print("\n1. Eliminar por indice")
    print("2. Eliminar ultima botella")
    print("3. Eliminar primera botella")
    
    opcion = input("Seleccione: ")
    
    try:
        if opcion == "1":
            indice = int(input("Ingrese indice a eliminar: "))
            botella_eliminada = inventario_botellas.pop(indice)
            print(f"\nBotella {botella_eliminada.marca} eliminada correctamente!")
            
        elif opcion == "2":
            botella_eliminada = inventario_botellas.pop()
            print(f"\nUltima botella ({botella_eliminada.marca}) eliminada!")
            
        elif opcion == "3":
            botella_eliminada = inventario_botellas.pop(0)
            print(f"\nPrimera botella ({botella_eliminada.marca}) eliminada!")
            
    except (ValueError, IndexError):
        print("Error al eliminar la botella")

def ordenar_botellas():
    print("\n--- ORDENAR BOTELLAS ---")
    
    # Convertir capacidades a numeros para ordenar
    def obtener_valor_capacidad(botella):
        cap = botella.capacidad.lower()
        if 'ml' in cap:
            return float(cap.replace('ml', ''))
        elif 'l' in cap:
            return float(cap.replace('l', '')) * 1000
        return 0
    
    inventario_botellas.sort(key=obtener_valor_capacidad)
    print("Botellas ordenadas por capacidad!")
    mostrar_botellas()

def invertir_orden():
    print("\n--- INVERTIR ORDEN ---")
    inventario_botellas.reverse()
    print("Orden del inventario invertido!")
    mostrar_botellas()

def contar_botellas():
    print("\n--- CONTAR BOTELLAS POR TIPO ---")
    
    total = len(inventario_botellas)
    plastico = sum(1 for b in inventario_botellas if isinstance(b, Botella_plastico))
    vidrio = sum(1 for b in inventario_botellas if isinstance(b, Botella_vidrio))
    normales = total - plastico - vidrio
    
    print(f"Total de botellas: {total}")
    print(f"Botellas normales: {normales}")
    print(f"Botellas de plastico: {plastico}")
    print(f"Botellas de vidrio: {vidrio}")

def capacidad_total():
    print("\n--- CAPACIDAD TOTAL ---")
    
    def obtener_ml(capacidad):
        cap = capacidad.lower()
        if 'ml' in cap:
            return float(cap.replace('ml', ''))
        elif 'l' in cap:
            return float(cap.replace('l', '')) * 1000
        return 0
    
    total_ml = sum(obtener_ml(b.capacidad) for b in inventario_botellas)
    total_litros = total_ml / 1000
    
    print(f"Capacidad total: {total_ml}ml ({total_litros}L)")

def ejecutar_sistema():
    # Agregar algunas botellas de ejemplo
    inventario_botellas.append(Botella("Coca-Cola", "1.5L", "Rosca"))
    inventario_botellas.append(Botella_plastico("Pepsi", "500ml", "Presion", "Redondo"))
    inventario_botellas.append(Botella_vidrio("Corona", "355ml", "Corona", "Ambar", 3.5))
    
    while True:
        menu_principal()
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            agregar_botella()
        elif opcion == "2":
            mostrar_botellas()
        elif opcion == "3":
            buscar_botella()
        elif opcion == "4":
            modificar_botella()
        elif opcion == "5":
            eliminar_botella()
        elif opcion == "6":
            ordenar_botellas()
        elif opcion == "7":
            invertir_orden()
        elif opcion == "8":
            contar_botellas()
        elif opcion == "9":
            capacidad_total()
        elif opcion == "10":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpcion no valida")
        
        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    ejecutar_sistema()