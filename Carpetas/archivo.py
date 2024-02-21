
class Archivo:
    def __init__(self, ruta, nombreArchivo, palabra):
        self._ruta = ruta
        self._nombreArchivo = nombreArchivo
        self._palabra = palabra
    
    def contarPalabra(self, ruta, nombreArchivo, palabra):
        """
        Se elije el método para buscar la cantidad de veces qye aparece la palabra según la extensión
        """
        nombre = nombreArchivo.split('.')
        extension = nombre[-1]
        
        if (extension == 'txt'):
            self.contarPalabraTxt(ruta, nombreArchivo, palabra)
            
    def contarPalabraTxt(self, ruta, nombreArchivo, palabra):
        """
        Buscar cantidad de veces que aparece una palabra en un archivo .txt
        """
        ruta = ruta+'/'+nombreArchivo
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

        contenido = contenido.lower()
        palabra = palabra.lower()

        cantidad = contenido.count(palabra)
        return cantidad


        




archivotest = Archivo('C:/carpetapadre/subcarpeta/carpeta1', 'Texto1.txt', 'arar')

#archivotest.contarPalabra(archivotest._ruta, archivotest._nombreArchivo, archivotest._palabra)
