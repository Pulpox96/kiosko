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
def precio(dicc, tipo, nombre):

    try:
        return dicc[tipo][nombre][1]
    except:
        return "Algo salio mal, pruebe devuelta"

def mostrarProductos(dicc):

#probar haciendo una lista de las 2 keys, y despues con un for con la cantidad de items que tiene esa lista

    for tipo in dicc:

        for producto in tipo.keys():

            print(f"{producto}, precio: ${producto[1]}; hay en total: ${producto[2]}")

mostrarProductos(productos)

# Usuario functions
