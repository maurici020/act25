from os import system
from funciones  import *
while True:
    try:
        system("pause")
        system("cls")

        print("""
========== CONTROL DE INVENTARIO AUTOMOTRIZ ==========
1. Ingresar Nuevo Vehículo
2. Verificar Existencia de Patente
3. Actualizar Datos de un Vehículo (Precio y Año)
4. Aplicar Descuento Masivo por Año
5. Exportar Inventario Filtrado por Tipo
6. Listar Catálogo Completo con IVA Incluido
7. Finalizar Programa
======================================================""")
        opcion = int(input("seleccione : "))

        match opcion:
            case 1: 
                patente = input("ingrese la patente : ").upper().strip()
                tipo = input("ingrese tipo (sedan/suv/camioneta): ")
                anio = int(input("ingrese año (2015-2026) : "))
                precio = int(input("ingrese el precio : "))
                agregar(patente,tipo,anio,precio)
            case 2: 
                patente = input("ingrese la patente : ").upper().strip()
                mostrar(patente)
            case 3: 
                patente = input("Ingrese la patente del vehículo : ").upper().strip()
                nuevo_anio = int(input("Ingrese el nuevo año (2015-2026): "))
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                actualizar(patente, nuevo_anio, nuevo_precio)
            case 4: pass
            case 5: pass
            case 6: listarconiva()
            case 7: break
            case _: print("no valido")
    except Exception as e:
        print(f"error {e}")