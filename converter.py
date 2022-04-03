import os
import glob
import pandas as pd

def crearCSVs(nombreArchivo):
    """Recibe el nombre del archivo de excel y crea un archivo csv por cada hoja
        del archivo."""
    df = pd.read_excel(nombreArchivo, sheet_name=None)  

    for key in df.keys(): 
        df[key].to_csv('documentos/%s.csv' %key)

def combinarCSV(archivoIgnorar=None):
    """Combina todos los archivos .csv guardados en una carpeta."""
    os.chdir(r"C:\Users\Luis\Desktop\prueba_tecnica\documentos")
    extension = 'csv'
    todosNombres = [i for i in glob.glob('*.{}'.format(extension))]

    if archivoIgnorar != None:
        # Elimina de la lista el archivo deseado. En este caso, el documento en
        # Excel tiene una hoja al inicio llamado "Nota" que no tiene información
        # relevante, por lo que se elimina.
        todosNombres.remove(archivoIgnorar)

    # Combina todos los archivos en una lista.
    csvCombinado = pd.concat([pd.read_csv(n) for n in todosNombres])
    
    # Exporta a csv.
    csvCombinado.to_csv("csvCombinado.csv", index=False, encoding='utf-8-sig')

nombreArchivo = 'CPdescarga.xls'

crearCSVs(nombreArchivo)

combinarCSV('Nota.csv')
