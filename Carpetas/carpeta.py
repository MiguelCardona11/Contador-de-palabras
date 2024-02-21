import os
from archivo import Archivo

# C:/carpetapadre/subcarpeta/carpeta1

class Carpeta:
    def __init__(self, nombreCarpeta, ruta, palabra):
        self._nombreCarpeta = nombreCarpeta
        self._ruta = ruta
        self._palabra = palabra
                
    def obtenerArchivosLegibles(self):
        with os.scandir(self._ruta) as ficheros:
            ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and 
                        (fichero.name.endswith('.txt') or fichero.name.endswith('.json') or fichero.name.endswith('.xml') or fichero.name.endswith('.csv'))]
        return ficheros
    
    
    def escanearArchivos(self):
        archivos = self.obtenerArchivosLegibles()
        for i in range(len(archivos)):
            archivo = Archivo(self._ruta, archivos[i], self._palabra)
            print (archivo.contarPalabra())

        
            
            
            

    







# ZONA DE PRUEBAS

carpeta_test = Carpeta('carpeta1','C:/carpetapadre/subcarpeta/carpeta1', 'arar')

carpeta_test.escanearArchivos()

# carpeta_test.obtenerArchivosLegibles()
        


