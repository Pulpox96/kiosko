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

# Import Tabulate para imprimir los productos de forma mas ordenada
from tabulate import tabulate 

# dicc ahora es el diccionario a manejar adentro del programa
with open("productos.json") as f:
    
    dicc = json.load(f)


# Hay que usar la funcion "Dump" para actualizar el archivo json
#  json_object["d"] = 100 -> aca se actualiza el "D" al nuevo valor 100
#  a_file = open("sample_file.json", "w") -> se abre el archivo devuelta, pero ahora en modo "write"
#  json.dump(json_object, a_file) -> aca se usa dump, el primer argumento es el objecto json que ya teniamos, 
#                                   y el segundo argumento es el archivo que abrimos devuelta pero con write
#  a_file.close() -> se cierra el archivo despues de actualizar



# ---------------------------- Funciones Globales ----------------------------------------
def precio(dicc, producto):
    ''' Devuelve el precio del producto seleccionado
    '''

    try:
        #Checkeo si existe ese producto dentro de Comestibles
        if producto in dicc:
            return dicc[producto][1]

    except:
        print("Algo salio mal, pruebe devuelta")

def mostrarProductos(dicc):

    """ Muestra TODOS los productos dentro del archivo, incluidos los precios y stock
        Usamos el paquete "tabulate" para imprimir -> Documentacion en: https://pypi.org/project/tabulate/
    """

    listaTabular = []

    # listaTabular se guardaria asi -> [[chicle, 10, 50], [harina, 40, 41]] etc
    for producto in dicc:
        listaTabular.append([producto, dicc[producto][1], dicc[producto][2]])
    
    print(tabulate(listaTabular, headers=['Producto', 'Precio ($)', 'Stock'], tablefmt="github"))


def sacarStock(dicc, producto, cantidad):
    
    """ Saca Stock del producto seleccionado
    """  
   
    # Abrir para actualizarlo
    with open("productos.json", "w") as f:

        dicc[producto][2] = dicc[producto][2] - cantidad

        #actualizo el archivo json y lo cierro.
        try:
            json.dump(dicc, f)
        except:
            print("No se pudo actualizar archivo")

def productoExiste(dicc,producto):
    '''Returns True si existe el producto, False si no'''
    
    if producto in dicc:
        return True
    return False 

def saberStock(dicc,producto):
    '''Devuelve la cantidad de stock del producto seleccionado'''
    
    return dicc[producto][2] 

def espacio():
    '''Usar para dejar un espacio entre prints e inputs'''
    print()

def checkCeroNegativo(num):

    ''' Checkea que el usuario entre un numero correcto, y que sea mayor que 0
        Devuelve True solo si el valor es mayor que 0
    '''

    # aprovecho el error de intentar transformar string a int
    try:

        # solo devuelve True si es mayor que 0, cualquier otra cosa, devuelve false
        if int(num) > 0:
            return True
        else:
            print("Por favor ingrese un valor mayor a 0")
            espacio()
            return False

    except ValueError: # este es el error si no puede convertir el string a int
        print("Por favor ingrese un numero")
        espacio()
        return False

# ---------------------------- Funciones Usuario ------------------------------------------

def usuarioRun():
    ''' Main function para el usuario
    ''' 

    # Total es variable para calcular el precio final
    total = 0
    ticket = []

    while True:

        usuarioInput = input("Sabe lo que quiere comprar (si/no): ").lower()
        espacio()
        #Fijar que haya escrito si o no
        #if usuarioInput != "no" or usuarioInput != "si":
        #   continue

        #No sabe lo que quiere comprar
        if usuarioInput == "no":
            mostrarProductos(dicc)
            espacio()
            continue

        #Si sabe lo que quiere comprar    
        elif usuarioInput == "si":
            # contador de errores 
            errorNombreProducto = 0

            productoComprar = input("Ingrese el nombre del producto: ").lower()
        
            # Si el usuario no escribe el nombre del producto correctamente, 
            # le mostramos los disponibles devuelta
            while not productoExiste(dicc, productoComprar):
                productoComprar = input('Fijese de escribir bien el nombre del producto: ').lower()

                errorNombreProducto += 1
                if errorNombreProducto >= 3:
                    espacio()
                    print("Por favor ingrese uno de los productos disponibles: ")
                    espacio()
                    mostrarProductos(dicc)
                    espacio()
                    errorNombreProducto = 0
                    continue
            
            # guardar el stock, asi tengo que llamar a la funcion 1 sola vez
            stockDelProducto = saberStock(dicc,productoComprar)

            cantidad = input("Cuantos quiere comprar?: ")
            espacio()

            while not checkCeroNegativo(cantidad):
                    cantidad = input(f"Por favor ingrese un numero menor o igual a {stockDelProducto}: ")

            # ahora que estoy seguro que ingreso un integer, lo convierto
            cantidad = int(cantidad)
            espacio()
                
            # Si el usuario entra un numero mayor al stock disponible
            
            while stockDelProducto < cantidad:

                print(f"Solo hay {stockDelProducto} {productoComprar}(s) en stock")
                espacio()
                cantidad = input(f"Por favor ingrese un numero menor o igual a {stockDelProducto}: ")
                espacio()

                # si lo que el usuario pone no es un numero
                while not checkCeroNegativo(cantidad):
                    cantidad = input(f"Por favor ingrese un numero menor o igual a {stockDelProducto}: ")        
                
                # Necesito transformarlo a int devuelta, por si se equivoco y tuvo que ingresar el valor devuelta
                cantidad = int(cantidad)    
                
                espacio()
            

            # agrego el producto y cantidad al "ticket" para despues sacar stock de cada 1
            # el ticket va a ser una "lista de listas", cada producto y cantidad su propia lista
            ticket.append([productoComprar,cantidad])

            total = precio(dicc, productoComprar) * cantidad + total
            
            print(f"Su total actual es de ${total}") 
            
        else: 
            print("escriba si o no")
            continue

        continuarInput = input("Desea seguir comprando? (si/no): ").lower()

        while continuarInput != "si" and continuarInput  != "no":
            print("Solo escribir Si o No")
            espacio()
            continuarInput = input("Desea seguir comprando? (si/no): ").lower() 

        if continuarInput == "si":
            continue
        elif continuarInput == "no":
            espacio()

            print("Su compra final es: ")
            for item in ticket:
                print(f"{item[1]} {item[0]}(s)")

            print(f"Precio final: ${total}")
            
            cancelar = input("Escriba 'Fin' si esta seguro de la compra o 'Cancelar' para borrar la compra (fin/cancelar): ").lower()
            
            while cancelar != "fin" and cancelar != "cancelar":
                cancelar = input("Ingrese 'Fin' o 'Cancelar': ").lower()

            # Este break termina con el loop de seguir comprando
            break
            
    if cancelar == "fin":
        #Loop para sacar stock de cada producto del ticket     
        for item in ticket:
            sacarStock(dicc, item[0], item[1])

        print(f"Su total es ${total}")
        print("Gracias por comprar!")

    else:
        print("Se cancelo la compra.")


# ---------------------------- Funciones Administrador ------------------------------------------
def agregarStock(dicc, producto, cantidad):

    """ Solo aumenta la cantidad de stock del producto seleccionado
    """

    # Abrir para actualizarlo
    with open("productos.json", "w") as f:

        dicc[producto][2] = dicc[producto][2] + cantidad

        #actualizo el archivo json.
        try:
            json.dump(dicc, f)
        except:
            print("No se pudo actualizar el archivo")


def agregarProducto(dicc, producto, precio, cantidad):
    
    ''' Se agrega un producto totalmente nuevo al json. El id es lo que seria el identificador de cada
    producto si fuera un kiosko real, por eso se necesita que cada id sea diferente. Como estamos 
    haciendo el diccionario/json de forma ordenada, es suficiente saber cual es el id del ultimo producto
    y sumarle 1.
    '''

    # Si el archivo tuviera miles de productos, probablemente hacer una lista de todos, llevaria tiempo y habria
    # que buscar una forma mejor.

    # para agarrar el ultimo elemento del diccionario hacer una lista de todo el diccionario -> list(dicc)[-1]
    ultimoProducto = list(dicc)[-1]

    ultimoId = dicc[ultimoProducto][0] + 1 # necesitamos que sea un nuevo id, por eso agrego el +1

    # Abrir para actualizarlo
    with open("productos.json", "w") as f:

        # Agrego el nuevo producto al diccionario
        dicc[producto] = [ultimoId,precio,cantidad]

        #actualizo el archivo json y lo cierro.
        try:
            json.dump(dicc, f)
        except:
            print("No se pudo actualizar archivo")

def eliminarProducto(dicc, producto):
   
    """ borra el key-value completamente del archivo
    """
    
    # Abrir para actualizarlo
    # f = open("productos.json", "w") -> Es preferible "with open" porque tiene mejor error handling y cierra solo
    with open("productos.json", "w") as f:

    # Borra el "objeto". En python el key-value es un objeto, y por eso se puede borrar con "del"
    # otra forma seria usando .pop -> dicc.pop(producto) 
        del dicc[producto]

    # Actualizo el archivo json.
        try:
            json.dump(dicc, f)
        except:
            print("No se pudo actualizar archivo")
            
    #f.close()  -> no es necesario con "with"

def adminRun():
    ''' Main function para el administrador
    '''

    seguir = True

    while seguir:
        print("(1) Agregar producto nuevo")
        print("(2) Agregar Stock")
        print("(3) Eliminar producto")
        print("(4) Ver lista de productos")
        espacio()

        userInput = input("Que desea hacer: ").lower()
        espacio()

        while userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4":
            userInput =  input("Elija 1, 2, 3 o 4: ").lower()
            espacio()

        # Agregar producto nuevo
        if userInput == "1":
            
            productoNuevo = input("Escriba el nombre del producto: ").lower()
            espacio()

            # Si el producto ya esta agregado, entra a este while y le pregunta devuelta
            while productoExiste(dicc, productoNuevo):
                print("Ese producto ya existe, escriba uno que no este")
                espacio()
                productoNuevo = input("Escriba el nombre del producto: ").lower()
                espacio()
        

            stockNuevo = input(f"Escriba la cantidad a agregar de {productoNuevo}: ")
            espacio()

            while not checkCeroNegativo(stockNuevo):
                stockNuevo = input(f"Escriba la cantidad a agregar de {productoNuevo}: ")
                espacio()
           
            
            precioNuevo = input(f"Escriba el precio de {productoNuevo}: $")
            espacio()

            while not checkCeroNegativo(precioNuevo):       
                espacio()
                precioNuevo = input(f"Escriba el precio de {productoNuevo}: $")

        
            # Una vez listo, se agrega el producto; hay que usar int porque sino agrega el stock y precio como strings
            agregarProducto(dicc, productoNuevo, int(precioNuevo), int(stockNuevo))
            print(f"{productoNuevo} se agrego correctamente")

        
        # Agregar stock
        elif userInput == "2":

            producto = input("Ingrese el producto a agregar stock: ").lower()

            while not productoExiste(dicc, producto): 
                producto = input(f"{producto} no existe. Ingrese un producto que si este: ").lower()
            
            stockNuevo = input(f"Ingrese la cantidad a agregar de {producto}: ")

            while not checkCeroNegativo(stockNuevo):
                stockNuevo = input(f"Ingrese la cantidad a agregar de {producto}: ")
            
            
            agregarStock(dicc, producto, int(stockNuevo))
            print(f"Ahora hay {saberStock(dicc, producto)} {producto}(s) en stock")

        
        # Eliminar Producto
        elif userInput == "3":

            while True: # Este while esta para que el usuario pueda escribir cancelar y salir de esta funcion
                producto = input("Escriba el nombre del producto a eliminar: ").lower()
                espacio()

                while not productoExiste(dicc, producto):
                    producto = input("Ese producto no existe, escriba uno que si este o escriba 'cancelar' para salir: ").lower()
                    espacio()
                    if producto == "cancelar":
                        break
                
                # necesito 2 cancelar -> break, porque sale de 2 while diferentes
                if producto == "cancelar":
                        break
                
                seguro = input(f"{producto} va a ser eliminado definitivamente, esta seguro (si/no): ").lower()
                
                while seguro != "si" and seguro != "no":

                    seguro = input("Solo escriba 'si' o 'no': ").lower()
                    espacio()

                if seguro == "si":
                    eliminarProducto(dicc, producto)
                    print(f"{producto} se elimino correctamente")
                    espacio()
                    break
                else:
                    print(f"{producto} no se eliminara")
                    espacio()
                    break

        # Mostrar Productos        
        elif userInput == "4": # no es necesario poner este elif, con un else bastaria, pero si queremos agregar otra funcion, ya tenemos elif

            mostrarProductos(dicc)
        
        espacio()
        seguir = input("Desea seguir usando el programa? (si/no): ").lower()
        espacio()

        while seguir != "si" and seguir != "no":
            print("Solo escriba 'Si' o 'No'")
            espacio()
            seguir = input("Desea seguir usando el programa? (si/no): ").lower()
        
        if seguir == "no":
            print("Gracias por usar este programa!")
            break # este break termina el programa


#----------------------------- Programa Principal ----------------------------------------


print("Bienvenido")
espacio()
userInput = input("Es un Usuario o un Administrador? (user/admin): ").lower()
espacio()

# Checkear que solo ingrese User / Admin
while userInput != "user" and  userInput != "admin":
    userInput = input("Escriba 'user' o 'admin': ").lower()

if userInput == "user":
    usuarioRun()
else:
    adminRun()

