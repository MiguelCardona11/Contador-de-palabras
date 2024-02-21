import os
from archivo import *

# C:/carpetapadre/subcarpeta/carpeta1

class Carpeta:
    def __init__(self, nombreCarpeta, ruta, palabra):
        self._nombreCarpeta = nombreCarpeta
        self._ruta = ruta
        self._palabra = palabra
                
    def obtenerArchivosLegibles(self, ruta):
        with os.scandir(ruta) as ficheros:
            ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and 
                        (fichero.name.endswith('.txt') or fichero.name.endswith('.json') or fichero.name.endswith('.xml') or fichero.name.endswith('.csv'))]
        return ficheros
    
    #def escanearArchivos(self, ruta):
        #archivos = self.obtenerArchivosLegibles(ruta)
        #for i in archivos:
            
            
            

    







# ZONA DE PRUEBAS

carpeta_test = Carpeta('carpeta1','C:/carpetapadre/subcarpeta/carpeta1', 'piojo')

carpeta_test.escanearArchivos(carpeta_test._ruta)
        


