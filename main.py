from os import system
from funciones import *
while True:
    try:
        system("pause")
        system("cls")

        print("""
******** control de inventario automotriz *********
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
                tipo = input("ingrese tipo : ")
                anio = int(input("ingrese año (2015-2026) : "))
                precio = int(input("ingrese precio : "))
                agregar(patente,tipo,anio.precio)
            case 2: 
                patente = input("ingrese la patente : ").upper().strip()
                
            case 3: pass
            case 4: pass
            case 5: pass
            case 6: listarconiva()
            case 7: pass
            case _: print("no valido")
    except Exception as e:
        print(f"error {e}")