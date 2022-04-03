import csv

filename = "CPdescarga.txt"

file = open(filename, "rt")

contents = file.read()

newcontents = contents.replace('|', ',')

print(newcontents)

file.close()