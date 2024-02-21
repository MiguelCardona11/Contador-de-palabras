import os

# C:\carpetapadre\subcarpeta\carpeta1

class Carpeta:
    def __init__(self, nombreCarpeta, ruta, palabra):
        self._nombreCarpeta = nombreCarpeta
        self._ruta = ruta
        self._palabra = palabra
        
    def contenidoCarpeta(self, ruta):
        with os.scandir(ruta) as ficheros:
            for fichero in ficheros:
                print(fichero.name)

    









# ZONA DE PRUEBAS

carpeta_test = Carpeta('carpeta1','C:\carpetapadre\subcarpeta\carpeta1', 'piojo')

carpeta_test.contenidoCarpeta(carpeta_test._ruta)
        


