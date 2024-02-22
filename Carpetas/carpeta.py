import os
from archivo import Archivo

# C:/carpetapadre/subcarpeta/carpeta1

class Carpeta:
    def __init__(self, nombreCarpeta, ruta, palabra):
        self._nombreCarpeta = nombreCarpeta
        self._ruta = ruta
        self._palabra = palabra
                
    def obtenerArchivosLegibles(self):
        """
        Recorrer carpeta de la ruta en busca de archivos de texto legibles por el programa.
        devuelve un arreglo de los archivos encontrados.
        """
        ruta_completa = self._ruta+'/'+self._nombreCarpeta
        with os.scandir(ruta_completa) as ficheros:
            ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and 
                        (fichero.name.endswith('.txt') or fichero.name.endswith('.json') or fichero.name.endswith('.xml') or fichero.name.endswith('.csv'))]
        return ficheros
    
    
    def escanearArchivos(self):
        """
        recorre un arreglo de archivos legibles y cuenta la cantidad de veces que se encuentra la palabra en cada archivo
        """
        total = 0
        ruta_completa = self._ruta+'/'+self._nombreCarpeta
        
        try:
            archivos = self.obtenerArchivosLegibles()
        except FileNotFoundError:
            print("La carpeta indicada no existe")
            return
        
        if archivos == []:
            print('No se encontraron archivos de texto en la carpeta "'+self._nombreCarpeta+'"')
            return
        
        for i in range(len(archivos)):
            archivo = Archivo(ruta_completa, archivos[i], self._palabra)
            cantidadRepetitas = archivo.contarPalabra()
            total = total + cantidadRepetitas 
            print(archivo._nombreArchivo+'  '+str(cantidadRepetitas)+' veces')
        print('Total:      '+str(total)+' veces')
        
            
            
            



# ZONA DE PRUEBAS

##carpeta_test = Carpeta('carpeta1','C:/carpetapadre/subcarpeta', 'arar')

##carpeta_test.escanearArchivos()

# carpeta_test.obtenerArchivosLegibles()
        


