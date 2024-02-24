import os
from archivo import Archivo

class Carpeta:
    """
    Clase para definir la Ubicacion de una carpeta dentro del equipo, junto con palabra a buscar
    """
    def __init__(self, nombreCarpeta, ruta, palabra):
        self._nombreCarpeta = nombreCarpeta
        self._ruta = ruta
        self._palabra = palabra
        self._rutaCompleta = self._ruta+'/'+self._nombreCarpeta
                
    def obtenerArchivosLegibles(self):
        """
        Recorro carpeta de la ruta en busca de archivos de texto legibles por el programa.\n
        Retorna un arreglo de los nombres de los archivos encontrados.
        """
        with os.scandir(self._rutaCompleta) as ficheros:
            ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and 
                        (fichero.name.endswith('.txt') or fichero.name.endswith('.json') or fichero.name.endswith('.xml') or fichero.name.endswith('.csv'))]
        return ficheros
    
    
    def escanearArchivos(self):
        """
        recorre un arreglo de archivos legibles y cuenta la cantidad de veces que se encuentra la palabra en cada archivo
        """
        total = 0
        try:
            archivos = self.obtenerArchivosLegibles()
        except FileNotFoundError:
            print("La carpeta indicada no existe")
            return
        
        if archivos == []:
            print('No se encontraron archivos de texto en la carpeta "'+self._nombreCarpeta+'"')
            return
        
        for i in range(len(archivos)):
            archivo = Archivo(self._rutaCompleta, archivos[i], self._palabra)
            cantidadRepetitas = archivo.contarPalabra()
            total = total + cantidadRepetitas 
            print(archivo._nombreArchivo+'  '+str(cantidadRepetitas)+' veces')
        print('Total:      '+str(total)+' veces')