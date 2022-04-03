import csv

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
 
for row in reader:
    estado = row[5]
    cp = int(row[7])
    if cp not in codigosPostales:
        codigosPostales.append(cp)
    if estado not in estados:
        estados.append(estado)

file.close()

print(estados)
print(codigosPostales)