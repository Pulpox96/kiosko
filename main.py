productos = {
    "comestibles" : {
        "caramelo" : [1, 5, 100],
        "alfajor": [2, 15, 20],
        "vino": [3, 200, 10],
	    "agua": [7, 100, 60],
	    "mayonesa": [8, 55, 35],
	    "yogurt": [9, 25, 50],
 
    },
    "noComestibles": {
        "harina" : [4, 70, 100],
        "jabon": [5, 15, 20],
        "lavandina": [6, 120, 40],
        "detergente": [10, 100, 20],
	    "fosforos": [11, 50, 50],
	    "vela": [12, 10, 50],
    }
}

#Crear archivo con los productos


#Actualizar archivo de los productos

# Global functions 
def precio(dicc, nombre):

#Falta agregar que pasa si el producto no esta en el dicc
# o tal vez de eso se encarga otra funcion, lo que haria (creo) 
# que todo lo de abajo no sea necesario

    try:
        #Checkeo si existe ese producto dentro de Comestibles
        if nombre in dicc["comestibles"]:
            return dicc["comestibles"][nombre][1]

        #Checkeo si existe ese producto dentro de No Comestibles
        elif nombre in dicc["noComestibles"]:
            return dicc["noComestibles"][nombre][1]
    except:
        return "Algo salio mal, pruebe devuelta"

def mostrarProductos(dicc):

#probar haciendo una lista de las 2 keys, y despues con un for con la cantidad de items que tiene esa lista

    for tipo in dicc:

        for producto in tipo.keys():

            print(f"{producto}, precio: ${producto[1]}; hay en total: ${producto[2]}")

#mostrarProductos(productos)

# Usuario functions

def comprar(dicc):

    total = 0

    usuarioInput = input("Que queres comprar: ")

    total = precio(dicc, usuarioInput)

    print(f"Tu total es {total}")

comprar(productos) 