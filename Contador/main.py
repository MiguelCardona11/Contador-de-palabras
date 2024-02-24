from carpeta import Carpeta

def main():
    fin = False

    while not fin:
        try:
            nombreCarpeta = input("Ingrese nombre de la carpeta: ")
            ruta = input("Ingrese la ruta de la carpeta: ")
            palabra = input("Ingrese la palabra a contar: ")

            carpeta = Carpeta(nombreCarpeta, ruta, palabra)
            carpeta.escanearArchivos()
            
            fin = True
        except FileNotFoundError:
            print("La carpeta indicada no existe, intente nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()
