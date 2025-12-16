from vehiculo import Vehiculo
from autodeportivo import AutoDeportivo
from furgoneta import Furgoneta
from camion import Camion

# Array principal para el inventario de vehiculos
flota_vehiculos = []

def mostrar_menu():
    print("\n" + "=" * 55)
    print("SISTEMA DE GESTION DE VEHICULOS")
    print("=" * 55)
    print("1. Registrar nuevo vehiculo")
    print("2. Ver todos los vehiculos")
    print("3. Buscar vehiculo por modelo")
    print("4. Actualizar informacion de vehiculo")
    print("5. Eliminar vehiculo de la flota")
    print("6. Ordenar vehiculos por precio")
    print("7. Invertir orden de la lista")
    print("8. Estadisticas de la flota")
    print("9. Filtrar por tipo de combustible")
    print("10. Salir del sistema")
    print("=" * 55)

def registrar_vehiculo():
    print("\n--- REGISTRO DE VEHICULO ---")
    print("Tipo de vehiculo:")
    print("1. Vehiculo basico")
    print("2. Auto deportivo")
    print("3. Furgoneta")
    print("4. Camion")
    
    tipo = input("\nEscoja el tipo: ")
    
    modelo = input("Modelo: ")
    color = input("Color: ")
    motor = input("Motor: ")
    num_puertas = int(input("Numero de puertas: "))
    capacidad = int(input("Capacidad de pasajeros: "))
    combustible = input("Tipo de combustible: ")
    
    if tipo == "1":
        vehiculo = Vehiculo(modelo, color, motor, num_puertas, capacidad, combustible)
        flota_vehiculos.append(vehiculo)
        print(f"\nVehiculo {modelo} registrado con exito!")
        
    elif tipo == "2":
        vel_max = int(input("Velocidad maxima (km/h): "))
        acel = float(input("Aceleracion 0-100 (segundos): "))
        convertible = input("Es convertible? (si/no): ").lower() == "si"
        transmision = input("Tipo de transmision: ")
        
        deportivo = AutoDeportivo(modelo, color, motor, num_puertas, capacidad, 
                                  combustible, vel_max, acel, convertible, transmision)
        flota_vehiculos.append(deportivo)
        print(f"\nAuto deportivo {modelo} registrado!")
        
    elif tipo == "3":
        cap_carga = float(input("Capacidad de carga (kg): "))
        largo = float(input("Largo (m): "))
        ancho = float(input("Ancho (m): "))
        alto = float(input("Alto (m): "))
        
        furgon = Furgoneta(modelo, color, motor, num_puertas, capacidad, combustible,
                          cap_carga, largo, ancho, alto)
        flota_vehiculos.append(furgon)
        print(f"\nFurgoneta {modelo} registrada!")
        
    elif tipo == "4":
        tonelaje = float(input("Tonelaje maximo: "))
        ejes = int(input("Numero de ejes: "))
        remolque = input("Tiene remolque? (si/no): ").lower() == "si"
        tipo_carga = input("Tipo de carga: ")
        
        camion = Camion(modelo, color, motor, num_puertas, capacidad, combustible,
                       tonelaje, ejes, remolque, tipo_carga)
        flota_vehiculos.append(camion)
        print(f"\nCamion {modelo} registrado!")

def ver_vehiculos():
    print("\n--- FLOTA DE VEHICULOS ---")
    
    if len(flota_vehiculos) == 0:
        print("No hay vehiculos registrados en la flota.")
        return
    
    for idx, vehiculo in enumerate(flota_vehiculos):
        print(f"\n[{idx}] ====================")
        print(f"Modelo: {vehiculo.modelo}")
        print(f"Color: {vehiculo.color}")
        print(f"Motor: {vehiculo.motor}")
        print(f"Puertas: {vehiculo.num_puertas}")
        print(f"Pasajeros: {vehiculo.capacidad_pasajeros}")
        print(f"Combustible: {vehiculo.tipo_combustible}")
        
        if isinstance(vehiculo, AutoDeportivo):
            print(f"TIPO: Auto Deportivo")
            print(f"Velocidad max: {vehiculo.velocidad_maxima} km/h")
            print(f"Aceleracion: {vehiculo.aceleracion_0_100}s")
            print(f"Convertible: {'Si' if vehiculo.es_convertible else 'No'}")
            
        elif isinstance(vehiculo, Furgoneta):
            print(f"TIPO: Furgoneta")
            print(f"Capacidad carga: {vehiculo.capacidad_carga} kg")
            print(f"Dimensiones: {vehiculo.largo}x{vehiculo.ancho}x{vehiculo.alto} m")
            
        elif isinstance(vehiculo, Camion):
            print(f"TIPO: Camion")
            print(f"Tonelaje: {vehiculo.tonelaje_max} ton")
            print(f"Ejes: {vehiculo.num_ejes}")
            print(f"Tipo carga: {vehiculo.tipo_carga}")

def buscar_vehiculo():
    print("\n--- BUSCAR VEHICULO ---")
    busqueda = input("Ingrese modelo a buscar: ").lower()
    
    resultados = []
    for i, vehiculo in enumerate(flota_vehiculos):
        if busqueda in vehiculo.modelo.lower():
            resultados.append((i, vehiculo))
    
    if len(resultados) == 0:
        print(f"No se encontraron vehiculos con '{busqueda}' en el modelo")
    else:
        print(f"\nSe encontraron {len(resultados)} vehiculo(s):")
        for indice, vehiculo in resultados:
            print(f"\n[{indice}] {vehiculo.modelo} - {vehiculo.color} - {vehiculo.motor}")

def actualizar_vehiculo():
    print("\n--- ACTUALIZAR VEHICULO ---")
    ver_vehiculos()
    
    if len(flota_vehiculos) == 0:
        return
    
    try:
        indice = int(input("\nIndice del vehiculo a actualizar: "))
        
        if indice < 0 or indice >= len(flota_vehiculos):
            print("Indice fuera de rango")
            return
        
        vehiculo = flota_vehiculos[indice]
        
        print("\nQue desea actualizar?")
        print("1. Color")
        print("2. Motor")
        print("3. Tipo de combustible")
        print("4. Capacidad de pasajeros")
        
        opcion = input("Seleccione: ")
        
        if opcion == "1":
            nuevo_color = input("Nuevo color: ")
            vehiculo.color = nuevo_color
            print(f"Color actualizado a {nuevo_color}")
            
        elif opcion == "2":
            nuevo_motor = input("Nuevo motor: ")
            vehiculo.motor = nuevo_motor
            print(f"Motor actualizado a {nuevo_motor}")
            
        elif opcion == "3":
            nuevo_combustible = input("Nuevo tipo de combustible: ")
            vehiculo.tipo_combustible = nuevo_combustible
            print(f"Combustible actualizado a {nuevo_combustible}")
            
        elif opcion == "4":
            nueva_capacidad = int(input("Nueva capacidad: "))
            vehiculo.capacidad_pasajeros = nueva_capacidad
            print(f"Capacidad actualizada a {nueva_capacidad} pasajeros")
            
    except ValueError:
        print("Entrada invalida")

def eliminar_vehiculo():
    print("\n--- ELIMINAR VEHICULO ---")
    ver_vehiculos()
    
    if len(flota_vehiculos) == 0:
        return
    
    print("\nOpciones de eliminacion:")
    print("1. Eliminar por indice")
    print("2. Eliminar el ultimo vehiculo")
    print("3. Eliminar el primer vehiculo")
    
    opcion = input("Seleccione: ")
    
    try:
        if opcion == "1":
            indice = int(input("Indice a eliminar: "))
            eliminado = flota_vehiculos.pop(indice)
            print(f"\n{eliminado.modelo} eliminado de la flota!")
            
        elif opcion == "2":
            eliminado = flota_vehiculos.pop()
            print(f"\nUltimo vehiculo ({eliminado.modelo}) eliminado!")
            
        elif opcion == "3":
            eliminado = flota_vehiculos.pop(0)
            print(f"\nPrimer vehiculo ({eliminado.modelo}) eliminado!")
            
    except (ValueError, IndexError):
        print("Error en la eliminacion")

def ordenar_vehiculos():
    print("\n--- ORDENAR VEHICULOS ---")
    print("1. Por modelo (alfabeticamente)")
    print("2. Por numero de puertas")
    print("3. Por capacidad de pasajeros")
    
    opcion = input("Ordenar por: ")
    
    if opcion == "1":
        flota_vehiculos.sort(key=lambda v: v.modelo)
        print("Vehiculos ordenados por modelo!")
        
    elif opcion == "2":
        flota_vehiculos.sort(key=lambda v: v.num_puertas)
        print("Vehiculos ordenados por numero de puertas!")
        
    elif opcion == "3":
        flota_vehiculos.sort(key=lambda v: v.capacidad_pasajeros)
        print("Vehiculos ordenados por capacidad!")
        
    ver_vehiculos()

def invertir_lista():
    print("\n--- INVERTIR ORDEN ---")
    flota_vehiculos.reverse()
    print("El orden de la flota ha sido invertido!")
    ver_vehiculos()

def estadisticas():
    print("\n--- ESTADISTICAS DE LA FLOTA ---")
    
    total = len(flota_vehiculos)
    
    if total == 0:
        print("No hay vehiculos para mostrar estadisticas")
        return
    
    deportivos = sum(1 for v in flota_vehiculos if isinstance(v, AutoDeportivo))
    furgonetas = sum(1 for v in flota_vehiculos if isinstance(v, Furgoneta))
    camiones = sum(1 for v in flota_vehiculos if isinstance(v, Camion))
    basicos = total - deportivos - furgonetas - camiones
    
    print(f"Total de vehiculos: {total}")
    print(f"Vehiculos basicos: {basicos}")
    print(f"Autos deportivos: {deportivos}")
    print(f"Furgonetas: {furgonetas}")
    print(f"Camiones: {camiones}")
    
    # Capacidad total
    cap_total = sum(v.capacidad_pasajeros for v in flota_vehiculos)
    print(f"\nCapacidad total de pasajeros: {cap_total}")

def filtrar_combustible():
    print("\n--- FILTRAR POR COMBUSTIBLE ---")
    tipo = input("Tipo de combustible a buscar: ").lower()
    
    filtrados = [v for v in flota_vehiculos if tipo in v.tipo_combustible.lower()]
    
    if len(filtrados) == 0:
        print(f"No hay vehiculos con combustible '{tipo}'")
    else:
        print(f"\nVehiculos con {tipo}: {len(filtrados)}")
        for vehiculo in filtrados:
            print(f"- {vehiculo.modelo} ({vehiculo.color})")

def iniciar_sistema():
    # Agregar vehiculos de ejemplo
    flota_vehiculos.append(AutoDeportivo("BMW Z4", "Negro", "3.0L Turbo", 2, 2, 
                                         "Gasolina", 250, 4.5, True, "Automatica"))
    flota_vehiculos.append(Furgoneta("Ford Transit", "Blanco", "2.0L Diesel", 4, 3, 
                                     "Diesel", 1200, 5.34, 2.05, 2.52))
    flota_vehiculos.append(Camion("Freightliner M2", "Blanco", "6.7L Diesel", 2, 3, 
                                  "Diesel", 12, 2, False, "Construccion"))
    
    while True:
        mostrar_menu()
        seleccion = input("\nIngrese una opcion: ")
        
        if seleccion == "1":
            registrar_vehiculo()
        elif seleccion == "2":
            ver_vehiculos()
        elif seleccion == "3":
            buscar_vehiculo()
        elif seleccion == "4":
            actualizar_vehiculo()
        elif seleccion == "5":
            eliminar_vehiculo()
        elif seleccion == "6":
            ordenar_vehiculos()
        elif seleccion == "7":
            invertir_lista()
        elif seleccion == "8":
            estadisticas()
        elif seleccion == "9":
            filtrar_combustible()
        elif seleccion == "10":
            print("\nCerrando sistema...")
            break
        else:
            print("\nOpcion no valida, intente de nuevo")
        
        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    iniciar_sistema()