"""
productos = {
        "caramelo" : [1, 5, 100],
        "alfajor": [2, 15, 20],
        "vino": [3, 200, 10],
	    "agua": [7, 100, 60],
	    "mayonesa": [8, 55, 35],
	    "yogurt": [9, 25, 50],
        "harina" : [4, 70, 100],
        "jabon": [5, 15, 20],
        "lavandina": [6, 120, 40],
        "detergente": [10, 100, 20],
	    "fosforos": [11, 50, 50],
	    "vela": [12, 10, 50]
}
"""
# Import json para leer el archivo
import json

# Data ahora es el diccionario a manejar adentro del programa
f = open("productos.json")
data = json.load(f)

#close el archivo original
f.close()

# Hay que usar la funcion "Dump" para actualizar el archivo json
#  json_object["d"] = 100 -> aca se actualiza el "D" al nuevo valor 100
#  a_file = open("sample_file.json", "w") -> se abre el archivo devuelta, pero ahora en modo "write"
#  json.dump(json_object, a_file) -> aca se usa dump, el primer argumento es el objecto json que ya teniamos, 
#                                   y el segundo argumento es el archivo que abrimos devuelta pero con write
#  a_file.close() -> se cierra el archivo despues de actualizar



# ---------------------------- Global functions ----------------------------------------
def precio(dicc, producto):
    ''' Devuelve el precio del producto seleccionado
    '''
 
 
 
 #Falta agregar que pasa si el producto no esta en el dicc
 # o tal vez de eso se encarga otra funcion, lo que haria (creo) 
 # que todo lo de abajo no sea necesario

    try:
        #Checkeo si existe ese producto dentro de Comestibles
        if producto in dicc:
            return dicc[producto][1]

    except:
        return "Algo salio mal, pruebe devuelta"

def mostrarProductos(dicc):

    """ Muestra TODOS los productos dentro del archivo, incluidos los precios y stock
    """



    for producto in dicc:

        print(f"{producto} - ${dicc[producto][1]}; hay en total: {dicc[producto][2]} en stock")
        print("------------")

def sacarStock(dicc, producto, cantidad):
    
    """ Saca Stock del producto seleccionado
    """
   
   
    # Abrir para actualizarlo
    f = open("productos.json", "w")

    dicc[producto][2] = dicc[producto][2] - cantidad

    #actualizo el archivo json y lo cierro.
    json.dump(dicc, f)

    f.close()



# ---------------------------- User functions ------------------------------------------

def comprar(dicc):
    ''' Pregunta al usuario si sabe lo que quiere comprar. En caso de que no sepa, muestra la lista de productos
        en caso de que sepa lo que quiere, se le pregunta el nombre del producto y se agrega al "carrito"
    '''
    
    
    #terminar variable para que siga el programa hasta que el usuario haga el "checkout"
    terminar = False
    total = 0
    ticket = []

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
            cantidad = int(input("Cuantos quiere comprar?: "))

            #agrego el producto y cantidad al "ticket" para despues sacar stock de cada 1
            # el ticket va a ser una "lista de listas", cada producto y cantidad su propia lista
            ticket.append([productoComprar,cantidad])

            total = precio(dicc, productoComprar) * cantidad + total
            
            print(f"su total actual es de ${total}") 

        continuarInput = input("Desea seguir comprando? (si/no): ").lower()

        if continuarInput == "si":
            continue
        else:
            terminar == True
            break

    #Loop para sacar stock de cada producto del ticket     
    for item in ticket:
        # 1 por ahora, mas adelante va a ser dependiendo cuantos compre de cada 1
        sacarStock(dicc, item[0], item[1])


    print(f"Tu total es ${total}")
    print("Gracias por comprar!")




# ---------------------------- Admin functions ------------------------------------------
def agregarStock(dicc, producto, cantidad):

    """ Solo cambia la cantidad de stock del producto seleccionado
    """

    # Abrir para actualizarlo
    f = open("productos.json", "w")

    dicc[producto][2] = dicc[producto][2] + cantidad

    #actualizo el archivo json y lo cierro.
    json.dump(dicc, f)

    f.close()

def agregarProducto(dicc, producto, precio, cantidad):
    
    ''' Se agrega un producto totalmente nuevo al json. El id es lo que seria el identificador de cada
    producto si fuera un kiosko real, por eso se necesita que cada id sea diferente. Como estamos 
    haciendo el diccionario/json de forma ordenada, basta con saber cual es el id del ultimo producto
    y sumarle 1
    '''



    # para agarrar el ultimo elemento del diccionario -> list(dicc)[-1]
    ultimoProducto = list(dicc)[-1]

    ultimoId = dicc[ultimoProducto][0] + 1 # necesitamos que sea un nuevo id, por eso agrego el +1

    # Abrir para actualizarlo
    f = open("productos.json", "w")

    # Agrego el nuevo producto al diccionario
    dicc[producto] = [ultimoId,precio,cantidad]

    #actualizo el archivo json y lo cierro.
    json.dump(dicc, f)

    f.close()

def sacarProducto(dicc, producto):
   
    """ borra el key-value completamente del archivo
    """
    
    # Abrir para actualizarlo
    f = open("productos.json", "w")

    # Borra el "objeto". En python el key-value es un objeto, y por eso se puede borrar con del
    # otra forma seria usando .pop -> dicc.pop(producto) 
    del dicc[producto]

    #actualizo el archivo json y lo cierro.
    json.dump(dicc, f)

    f.close() 

# ------------ Testing Program / Functions--------------------------

sacarProducto(data, "chicle")