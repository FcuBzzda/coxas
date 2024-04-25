import csv
from pathlib import Path

def toNo(rutaOriginal, rutaNueva):
   with open(rutaOriginal,'r',encoding='utf8') as archivo_Lectura:
    with open(rutaNueva,'w',encoding='utf8',newline='') as archivo_Escritura:
      csv_reader = csv.reader(archivo_Lectura)
      csv_writer = csv.writer(archivo_Escritura)
      header = next(csv_reader)
      header.append('posee_conectividad')
      csv_writer.writerow(header)
      for line in csv_reader:
         newLine = []
         for cell in line:
            if(cell == '--'):
               newLine.append('NO')
            else:
               newLine.append(cell)
         if('SI'not in line):
            newLine.append('NO')
         else:
            newLine.append('SI')
         csv_writer.writerow(newLine)




rutaOriginal = Path("datasets")/"Conectividad_Internet.csv"
rutaNueva = Path("datasets")/"datasetsModificados"/"Conectividad_Internet.csv"

toNo(rutaOriginal,rutaNueva)
