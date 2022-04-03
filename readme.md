# Explicación

### Converter.py

El archivo 'converter.py' toma el nombre de un archivo de excel descargado 
en SEPOMEX y genera un archivo csv por cada hoja de este (Ignorando la primera 
hoja, ya que solo es una nota y no contiene información relevante). 

Después, toma estos archivos generados y los combina en un solo archivo csv 
llamado "csvCombinado.csv" con el cual se podra trabajar.

### lectorCSV.py

Abre el archivo "csvCombinado.csv" generado por el script anterior y (por el momento) 
realiza la siguiente operación:

* Genera un arreglo bidimensional con el nombre de la colonia como key de tipo string 
y como valor se crea una lista con los codigos postales relacionados con la colonia.

# Instrucciones de uso.

## Converter.py

1. En caso de ejecutarse en otro sistema, modificar la línea 15 del archivo e introducir 
la dirección de la carpeta donde se desean almacenar los archivos CSV generados 
por el script.

2. Ejecutar el script en una sesión de Python e introducir el nombre del archivo 
descargado en SEPOMEX.

3. Ejecutar y esperar a que el script termina de ejecutarse.

4. Cuando el script declare que terminó, verificar que el archivo ha sido creado.

## lectorCSV.py

1. Ejecutar converter.py y tener el archivo "csvCombinado.csv" listo.

2. Ejecutar este script.

