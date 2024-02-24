import re
import json
import csv
import xml.etree.ElementTree as ET

class Archivo:
    """
    Clase para definir la ubicacion de un archivo de texto dentro del equipo, junto con una palabra a buscar
    """
    def __init__(self, ruta, nombreArchivo, palabra):
        self._ruta = ruta
        self._nombreArchivo = nombreArchivo
        self._palabra = palabra
        self._rutaCompleta = self._ruta+'/'+self._nombreArchivo
    
    def contarPalabra(self):
        """
        Devuelve la cantidad de veces que aparece una palabra en un archivo de extension .txt, .json, .csv o .xml
        """
        nombre = self._nombreArchivo.split('.')
        extension = nombre[-1]
        
        if (extension == 'txt'):
            return self.contarPalabraTxt()
        
        elif (extension == 'json'):
            return self.contarPalabraJson()
        
        elif (extension == 'csv'):
            return self.contarPalabraCsv()
        
        elif (extension == 'xml'):
            return self.contarPalabraXml()
            
    
    def contarCantidad(self, contenido):
        """
        Convierto el contenido recibido a una lista de palabras completas definidas por límites de palabra (para solo contar palabras individuales).\n
        Retorna la cuenta total de palabras encontradas en el texto del contenido.
        """
        palabras = re.findall(r'\b\w+\b', str(contenido).lower())
        cantidad = palabras.count(self._palabra.lower())
        return cantidad
    
    def contarPalabraTxt(self):
        """
        Lee el archivo y devuelve la cantidad de veces que aparece una palabra en un archivo .txt
        """
        with open(self._rutaCompleta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()

        return self.contarCantidad(contenido)
    
    def contarPalabraJson(self):
        """
        Lee el archivo y devuelve la cantidad de veces que aparece una palabra en un archivo .json
        """
        with open(self._rutaCompleta, 'r', encoding='utf-8') as archivo:
            contenido = json.load(archivo)
        
        return self.contarCantidad(contenido)
    
    def contarPalabraCsv(self):
        """
        Lee el archivo y devuelve la cantidad de veces que aparece una palabra en un archivo .csv
        """
        contenido = []
        with open(self._rutaCompleta, newline='') as csvfile:
            lector = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for fila in lector:
                contenido.append(fila)
                
        return self.contarCantidad(contenido)
    
    def contarPalabraXml(self):
        """
        Lee el archivo y devuelve la cantidad de veces que aparece una palabra en un archivo .xml
        """
        contenido = []
        tree = ET.parse(self._rutaCompleta)
        root = tree.getroot()
        for elemento in root:
            contenido.append(elemento.text)
                   
        return self.contarCantidad(contenido)