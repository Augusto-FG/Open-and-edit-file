#Uso una lista para contener los datos del archivo por que se usar listas
#Es una ventaja que la lista este ordenada por vendedor/artivulo

#Prefiero usar una lista y no un diccionario por que los datos estan 
#en forma secuancial.
#creo que los diccionarios son mejores cuando buscamos datos en forma individual


def leer_archivo():
    #Funcion que lee el archivo VENTAS.TXT y lo devuelve en una lista
    lista = []
    
    #funcion lambda requerida para particionar la fecha
    #en DIA - MES - AÑO
    dma = lambda t: [t[:2],t[2:4],t[4:]]
    
    try:
        archivo = open("ventas.txt","r")
        for registro in archivo:
            vendedor = registro[:2]
            producto = registro[2:4]
            cantidad = registro[4:8]
            fecha = registro[8:-1]
            dia_mes_anio = dma(fecha)
            # cada registro leido es una lista
            dato = [vendedor, producto, cantidad, 
                    dia_mes_anio[0],dia_mes_anio[1],dia_mes_anio[2]]
            lista.append(dato)

        archivo.close()
    except:
        print("Falló al leer el archivo de datos")
    return lista
    


lista = leer_archivo()

mes = 1

while mes > 0 and len(lista)>0:
    vendedor = 0
    hay_alguno = False
    mes = int(input("\n\nIngrese el numero de mes a consultar (cero para finalizar): "))
    print("\nVendedor   Producto  Cantidad        fecha")
    for registro in lista:
        if int(registro[4]) == mes:
            hay_alguno=True
            if vendedor != int(registro[0]):
                print()
            #Para formatear la salida uso el metodo RJUST
            print(registro[0].rjust(8), 
                  registro[1].rjust(10),
                  registro[2].rjust(9),
                  registro[3].rjust(4)+"/"+registro[4]+"/"+registro[5])
            
            vendedor = int(registro[0])
    if hay_alguno == False:
        print("\nNo hay datos para el mes ingresado")
    
    
