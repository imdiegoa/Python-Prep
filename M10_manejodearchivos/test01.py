import sys
import os

archivo = open("clase09_ej4.csv","x")

montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

for clave in montañas.keys():
    if (clave == 'altura'):
        archivo.write(clave+'\n')
    else:
        archivo.write(clave+',')

ind = 0
while (ind < 10):
    archivo.write(montañas['nombre'][ind]+',')
    archivo.write(str(montañas['orden'][ind])+',')
    archivo.write(montañas['cordillera'][ind]+',')
    archivo.write(montañas['pais'][ind]+',')
    archivo.write(str(montañas['altura'][ind])+'\n')
    ind += 1

archivo.close()