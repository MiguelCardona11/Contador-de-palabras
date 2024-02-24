from carpeta import Carpeta

def main():
    nombreCarpeta = input("Ingrese nombre de la carpeta: ")
    ruta = input("Ingrese la ruta de la carpeta: ")
    palabra = input("Ingrese la palabra a contar: ")

    carpeta = Carpeta(nombreCarpeta, ruta, palabra)
    carpeta.escanearArchivos()

if __name__ == "__main__":
    main()