import sys

# Se ingresa en la terminal la ubicacion del archivo : py M10_manejodearchivos\\clase09_ej1.py Uno Dos Tres

if len(sys.argv) == 4:
    print("El primer parámetro es:",sys.argv[1])
    print("El segundo parámetro es:",sys.argv[2])
    print("El tercer parámetro es:",sys.argv[3])
else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py 1 2 3')