
vehiculos = []

def buscar(patente):
    for i in range(len(vehiculos)):
        if vehiculos[i]["patente"]== patente:
            return i
    return -1    


def agregar(patente,tipo,anio,precio):
    if len(patente)!=6:
        print("numero de caracteres no valido")
        return
    if " " in patente:
        print("no puede tener espacio en blanco")
        return
    if buscar(patente)>=0:
        print("no se puede repetir la patente")
        return
    if tipo.lower() not in ("sedan","suv","camioneta"):
        print("tipo no valido")
        return
    if anio<2015 or anio>2026:
        print("año no valido")
        return
    if precio<=5000000:
        print("precio no valido")
        return
    
    auto = {"patente":patente,"tipo":tipo,"anio":anio,"precio":precio}
    vehiculos.append(auto)
    print("vehiculo agregado")

def mostrar(patente):
    posicion = buscar(patente)
    if posicion>=0:
        print(f"patente encontrada : {vehiculos[posicion]}")
    else:
        print("patente no encontrada")

def listarconiva():
    if len(vehiculos)>0:
        print(f"{"N°"}{"patente":<8} {"tipo":<10} {"año":<6} {"precio":<10}")
        for i in range(len(vehiculos)):
            print(f"{i+1} {vehiculos[i]["patente"]:<8} {vehiculos[i]["tipo"]:<10} {vehiculos[i]["anio"]:<6} ${round(vehiculos[i]["precio"]*1.19):<10}")
    else:
        print("no hay vehiculos registrados")
