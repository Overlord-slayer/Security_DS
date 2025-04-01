'''
    Prologo del lab.
'''

import scapy.all as scapy

# a. Capturar 25 paquetes de la red doméstica
packets_live = scapy.sniff(count=25, iface="wlp0s20f3")

# b. Imprimir el tipo de variable, la longitud y el contenido de la variable
print("Tipo de variable:", type(packets_live))
print("Longitud de la variable:", len(packets_live))
print("Contenido de la variable:")
print(packets_live)

# c. Imprimir el tipo de dato del primer paquete capturado
print("Tipo de dato del primer paquete:", type(packets_live[0]))

# d. Imprimir el contenido de 5 paquetes
print("Contenido de 5 paquetes:")
for pkt in packets_live[:5]:
    print(pkt.summary())
