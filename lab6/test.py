import scapy.all as scapy
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Crear un DataFrame vacío para almacenar los datos en tiempo real
df_real_time = pd.DataFrame(columns=["src", "dst", "sport", "dport", "payload"])

# Función para procesar cada paquete
def process_packet(packet):
    global df_real_time
    if packet.haslayer(scapy.IP):
        packet_info = {
            "src": packet[scapy.IP].src,
            "dst": packet[scapy.IP].dst,
            "sport": packet[scapy.TCP].sport if packet.haslayer(scapy.TCP) else None,
            "dport": packet[scapy.TCP].dport if packet.haslayer(scapy.TCP) else None,
            "payload": len(packet.payload)
        }
        # Convertir el diccionario a un DataFrame
        new_packet_df = pd.DataFrame([packet_info])
        
        # Concatenar el nuevo DataFrame con el DataFrame original
        df_real_time = pd.concat([df_real_time, new_packet_df], ignore_index=True)
        
        # Limpiar la salida anterior
        clear_output(wait=True)
        
        # Mostrar el DataFrame actualizado
        display(df_real_time.tail(5))  # Mostrar solo las últimas 5 filas
        
        # Realizar análisis en tiempo real, por ejemplo, contar paquetes por IP origen
        df_real_time.groupby("src")["payload"].sum().sort_values().plot(kind='barh', title='Bytes enviados por IP origen')
        plt.show()

# Capturar en tiempo real
scapy.sniff(count=0, iface="wlp0s20f3", prn=process_packet, store=False)
