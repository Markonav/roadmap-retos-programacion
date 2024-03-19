#11 Manejo de ficheros
"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
"""
import os
abspath = os.path.abspath(__file__) #get the file directory
dname = os.path.dirname(abspath)
os.chdir(dname) #change to file directory

nameOfFile = "SaezMD"
extension = "." + "txt"
myName = "Name: Write your name here: **SMM**"
myAge = "Age: 12"
myFavouriteLanguage = "Language: Java" 

#write
with open(nameOfFile + extension, 'w') as file:
    file.write(myName + '\n' + myAge + '\n' + myFavouriteLanguage)

#read
with open(nameOfFile + extension, 'r') as file:
    myFile = file.read()
    print(myFile)

#delete file
#input("press enter key to delete the file...")
os.remove(nameOfFile + extension)


#EXTRA

file = open("shopFileRecords.txt",'w')
file.write("nails" + ", " + "12.33" + ", " + "6\n")
file.write("polish" + ", " + "22.55" + ", " + "10\n")
file.close()

file = open("shopFileRecords.txt",'r')
fileData = file.read().split('\n')
file.close()
print(fileData)


while True:
    inputUser = input("Select an option [add, search, update, delete, exit]: ").lower()
    if inputUser == "exit":
        file.close()
        os.remove("shopFileRecords.txt")
        break
    elif inputUser == "add":
        inputAdd = input("New item: ").lower()

        file = open("shopFileRecords.txt",'r')
        fileData = file.read()

        if inputAdd in fileData:
            print("Item already exist!")

        else: 
            inputAddPrice = input("New price: ")
            inputAddQty = input("New quantity: ")
            file = open("shopFileRecords.txt",'a')
            file.write( inputAdd + ", " + inputAddPrice + ", " + inputAddQty + "\n")
   
        file.close()

    elif inputUser == "search":
        with open("shopFileRecords.txt") as file:
            for line in file:
                print(line.rstrip())

    elif inputUser == "delete":
        inputDelete = input("Delete item: ").lower()

        try: 
            file = open("shopFileRecords.txt",'r')
            lines = file.readlines()
            file.close()
            
            with open("shopFileRecords.txt",'w') as file:
                for line in lines:
                    if line.find(inputDelete) != -1:  # find() returns -1 if no match is found
                        pass
                    else:
                        file.write(line)
        except:
            print("Item not found!")
    
    elif inputUser == "update":
        inputUpdate = input("Update item: ").lower()

        #Update1: delete line
        try: 
            file = open("shopFileRecords.txt",'r')
            lines = file.readlines()
            file.close()
            
            with open("shopFileRecords.txt",'w') as file:
                for line in lines:
                    if line.find(inputUpdate) != -1:  # find() returns -1 if no match is found
                        pass
                    else:
                        file.write(line)
        
            #Update2: add line
            inputAddPrice = input("New price: ")
            inputAddQty = input("New quantity: ")
            file = open("shopFileRecords.txt",'a')
            file.write( inputUpdate + ", " + inputAddPrice + ", " + inputAddQty + "\n")
    
            file.close()
        
        except:
            print("Item not found!")        







