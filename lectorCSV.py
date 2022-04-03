import csv
import unidecode

nombreArchivo = "documentos/csvCombinado.csv"

archivo = open(nombreArchivo, encoding='utf-8')

lector = csv.reader(archivo)
header_row = next(lector)

# Relacion de colonias con sus codigos postales
col_CP = {}
 
"""for fila in lector:
    estado = fila[5]
    # Convierte los carácteres con acentos en uno legible por el sistema.
    estado = unidecode.unidecode(estado)
    cp = int(fila[7])
    if cp not in codigosPostales:
        codigosPostales.append(cp)
    if estado not in estados:
        estados.append(estado)"""

for fila in lector:
    colonia = fila[2]
    colonia = unidecode.unidecode(colonia)
    
    if colonia not in col_CP:
        col_CP[colonia] = []
    
    cp = int(fila[7])

    if cp not in col_CP[colonia]:
        col_CP[colonia].append(cp)

archivo.close()

print(col_CP)