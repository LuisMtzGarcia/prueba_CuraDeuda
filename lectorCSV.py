import csv
import unidecode

nombreArchivo = "documentos/csvCombinado.csv"
"""with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Obtener los estados.
    estados = []
    # Obtener todos los codigos postales
    codigosPostales = []

    for row in reader:
        estado = row[5]
        cp = int(row[7])
        if cp not in codigosPostales:
            codigosPostales.append(cp)
        if estado not in estados:
            estados.append(estado)"""

archivo = open(nombreArchivo, encoding='utf-8')
lector = csv.reader(archivo)
header_row = next(lector)

estados = []
codigosPostales = []
 
for fila in lector:
    estado = fila[5]
    # Convierte los carácteres con acentos en uno legible por el sistema.
    estado = unidecode.unidecode(estado)
    cp = int(fila[7])
    if cp not in codigosPostales:
        codigosPostales.append(cp)
    if estado not in estados:
        estados.append(estado)

archivo.close()

print(estados)
print(codigosPostales)