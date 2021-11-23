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
    
    """ Saca Stock del producto seleccionado. El 'stock' esta en el 3er lugar de la lista
    """  
   
    # Abrir para actualizarlo
    with open("productos.json", "w") as f:

        dicc[producto][2] = dicc[producto][2] - cantidad

        # Actualizo el archivo json.
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
    try:
        return dicc[producto][2]
    except:
        print("Algo salio mal en saberStock()") 

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
    ''' Function principal para el usuario. Pregunta que producto, cuanto, y calcula el final.
        Usa todas las funciones definidas anteriormente.
    ''' 

    # Total es variable para calcular el precio final
    total = 0
    ticket = []

    # loop principal para permitir la compra de varios productos
    while True:

        usuarioInput = input("Sabe lo que quiere comprar (si/no): ").lower()
        espacio()

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

            # Si no hay stock
            if stockDelProducto == 0:
                print(f"Disculpe, no hay stock disponible de {productoComprar}")
                espacio()

            # Si hay stock
            else:
                cantidad = input("Cuantos quiere comprar?: ")
                espacio()

                # Checkeo que haya ingresado un int y que sea mayor que 0
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
            
        
        # Si se equivoca en escribir si o no (Sabe lo que quiere comprar (si/no): )
        else: 
            print("Escriba si o no")
            continue

        if total != 0: # Si compro al menos 1 cosa, entra aca

            continuarInput = input("Desea seguir comprando? (si/no): ").lower()

            while continuarInput != "si" and continuarInput  != "no":
                print("Solo escribir Si o No")
                espacio()
                continuarInput = input("Desea seguir comprando? (si/no): ").lower() 

            if continuarInput == "si":
                continue
            elif continuarInput == "no":
                espacio()

                # Solo muestra el ticket y el resto, si compro algo
                if total != 0:

                    print("Su compra final es: ")
                    for item in ticket:
                        print(f"{item[1]} {item[0]}(s)")

                    espacio()

                    print(f"Precio final: ${total}")
                    espacio()

                    cancelar = input("Escriba 'Fin' si esta seguro de la compra o 'Cancelar' para borrar la compra (fin/cancelar): ").lower()
                    
                    while cancelar != "fin" and cancelar != "cancelar":
                        cancelar = input("Ingrese 'Fin' o 'Cancelar': ").lower()

                    # Este break termina con el loop de seguir comprando
                    break
        else:
            break # Si no compro nada, salgo directamente del loop principal.

    # Si compró algo entra al if    
    if total != 0:
        if cancelar == "fin":
            #Loop para sacar stock de cada producto del ticket
            for item in ticket:
                sacarStock(dicc, item[0], item[1])

            print(f"Su total es ${total}")
            print("Gracias por comprar!")

        else:
            print("Se cancelo la compra.")
    
    #si no compró nada
    else:
        print("Vuelva Pronto")


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
            print("No se pudo actualizar el archivo. Error en agregarStock()")

def agregarProducto(dicc, producto, precio, cantidad):
    
    ''' Se agrega un producto totalmente nuevo al json. El id es lo que seria el identificador de cada
    producto si fuera un kiosko real, por eso se necesita que cada id sea diferente. Como estamos 
    haciendo el diccionario/json de forma ordenada, es suficiente saber cual es el id del ultimo producto
    y sumarle 1.
    '''

    # Si el archivo tuviera miles de productos, probablemente hacer una lista de todos llevaria tiempo y habria
    # que buscar una forma mejor.

    # para agarrar el ultimo elemento del diccionario hacer una lista de todo el diccionario
    # y agarrar el ultimo -> list(dicc)[-1]
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
   
    """ Borra el key-value completamente del archivo
    """
    
    # Abrir para actualizarlo
    # f = open("productos.json", "w") -> Es preferible "with open" porque tiene mejor error handling y cierra solo
    with open("productos.json", "w") as f:

    # Borra el "objeto". En python el key-value es un objeto, y por eso se puede borrar con "del"
    # otra forma seria usando .pop -> dicc.pop(producto) 
        try:
            del dicc[producto]

    # Actualizo el archivo json.
            json.dump(dicc, f)
        except:
            print("No se pudo actualizar archivo")
            
    #f.close()  -> no es necesario con "with open..."

def validarAdmin():
    ''' Checkea que el administrador sepa la contraseña, y le da acceso si la sabe
        Devuelve True si ingresa bien la contraseña, False en caso contrario
    '''
    
    password = "123"

    num = input("Ingrese contraseña: ").lower()
    espacio()

    try:
        if num == password:
            return True
        else:
            # Counter = la cantidad de intentos de ingresar la contraseña
            counter = 3
            espacio()

            while not num == password:
                
                print(f"Contraseña incorrecta, tiene {counter} intento(s) restantes")
                espacio()
                num = input("Ingrese contraseña: ").lower()
                espacio()
                counter -= 1
                
                if num == password:
                    return True
                if counter == 0:
                    return False
    except:
        print("Algo salio mal en validarAdmin()")



def adminRun():
    ''' Function principal para el administrador. Pregunta que quiere hacer,
        Y usa las funciones definidas anteriormente
    '''

    # Loop principal para permitir seguir usando el programa, despues de terminar.
    while True:
        print("(1) Agregar producto nuevo")
        print("(2) Agregar Stock")
        print("(3) Eliminar producto")
        print("(4) Ver lista de productos")
        espacio()

        userInput = input("Que desea hacer: ")
        espacio()

        while userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4":
            userInput = input("Elija 1, 2, 3 o 4: ")
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

            # Checkeo que sea int, mayor que 0 y un numero positivo
            while not checkCeroNegativo(stockNuevo):
                stockNuevo = input(f"Escriba la cantidad a agregar de {productoNuevo}: ")
                espacio()
           
            
            precioNuevo = input(f"Escriba el precio de {productoNuevo}: $")
            espacio()

            # Checkeo que sea int, mayor que 0 y un numero positivo
            while not checkCeroNegativo(precioNuevo):       
                espacio()
                precioNuevo = input(f"Escriba el precio de {productoNuevo}: $")

        
            # Una vez listo, se agrega el producto; hay que usar int porque sino agrega el stock y precio como 
            # strings, y sabemos que son numeros, porque fueron checkeados por checkCeroNegativo()
            agregarProducto(dicc, productoNuevo, int(precioNuevo), int(stockNuevo))
            print(f"{productoNuevo} se agrego correctamente")

        
        # Agregar stock
        elif userInput == "2":

            producto = input("Ingrese el producto a agregar stock: ").lower()

            # Checkeo que exista el producto
            while not productoExiste(dicc, producto): 
                producto = input(f"{producto} no existe. Ingrese un producto que si este: ").lower()
            
            stockNuevo = input(f"Ingrese la cantidad a agregar de {producto}: ")
            
            # Checkeo que sea int, mayor que 0 y un numero positivo
            while not checkCeroNegativo(stockNuevo):
                stockNuevo = input(f"Ingrese la cantidad a agregar de {producto}: ")
            
            
            agregarStock(dicc, producto, int(stockNuevo))
            print(f"Ahora hay {saberStock(dicc, producto)} {producto}(s) en stock")

        
        # Eliminar Producto
        elif userInput == "3":

            while True: # Este while esta para que el admin pueda escribir cancelar y salir de esta funcion
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
        elif userInput == "4": # no es necesario poner usar elif, con un else bastaria, pero si queremos agregar otra funcion, ya tenemos elif

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
    # Fijarse si sabe la contraseña
    if validarAdmin():
        adminRun()
    else:
        print("No ingreso la contraseña correcta, se cerrara el programa")
