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

# ---------------------------- Global functions ----------------------------------------
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


    for tipo in dicc:

        for producto in dicc[tipo]:

            print(f"{producto} - ${dicc[tipo][producto][1]}; hay en total: {dicc[tipo][producto][2]} en stock")
            print("------------")



# ---------------------------- User functions ----------------------------------------


# Pregunta al usuario si sabe lo que quiere comprar. En caso de que no sepa, muestra la lista de productos
# en caso de que sepa lo que quiere, se le pregunta el nombre del producto y se agrega al "carrito"
def comprar(dicc):
    
    #terminar variable para que siga el programa hasta que el usuario haga el "checkout"
    terminar = False
    total = 0

    while terminar == False:
        

        usuarioInput = input("Sabe lo que quiere comprar (si/no): ").lower()

        #Fijar que haya escrito si o no
        #if usuarioInput != "no" or usuarioInput != "si":
         #   continue

        #No sabe lo que quiere comprar
        #elif usuarioInput == "no":
        if usuarioInput == "no":
            mostrarProductos(dicc)
            continue

        #Si sabe lo que quiere comprar    
        else:
            productoComprar = input("Ingrese el nombre del producto: ").lower()

            total = precio(dicc, productoComprar) + total
            print(f"su total actual es de ${total}") 

        continuarInput = input("Desea seguir comprando? (si/no): ").lower()

        if continuarInput == "si":
            continue
        else:
            terminar == True
            break

    

    print(f"Tu total es ${total}")
    print("Gracias por comprar!")


comprar(productos)