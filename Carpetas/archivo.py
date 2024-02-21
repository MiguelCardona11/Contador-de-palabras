import re

class Archivo:
    def __init__(self, ruta, nombreArchivo, palabra):
        self._ruta = ruta
        self._nombreArchivo = nombreArchivo
        self._palabra = palabra
    
    def contarPalabra(self):
        """
        Se elije el método para buscar la cantidad de veces qye aparece la palabra según la extensión
        """
        nombre = self._nombreArchivo.split('.')
        extension = nombre[-1]
        
        if (extension == 'txt'):
            return self.contarPalabraTxt()
            
    def contarPalabraTxt(self):
        """
        Buscar cantidad de veces que aparece una palabra en un archivo .txt
        """
        ruta = self._ruta+'/'+self._nombreArchivo
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower()

        # Convertir el contenido en una lista de palabras
        palabras = re.findall(r'\b\w+\b', contenido)
        cantidad = palabras.count(self._palabra.lower())
        
        return self._nombreArchivo+'  '+str(cantidad)+' veces'


        




#archivotest = Archivo('C:/carpetapadre/subcarpeta/carpeta1', 'Texto1.txt', 'arar')

#print(archivotest.contarPalabra())
