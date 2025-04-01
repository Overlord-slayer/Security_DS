"""
Módulo de captura y análisis de paquetes en tiempo real

Este script utiliza Scapy para capturar paquetes de red en tiempo real, almacena los datos en un DataFrame de Pandas y genera gráficos dinámicos para el análisis del tráfico de red.
"""

import scapy.all as scapy
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Crear un DataFrame vacío para almacenar los datos en tiempo real
df_real_time = pd.DataFrame(columns=["src", "dst", "sport", "dport", "payload"])


def process_packet(packet):
    """
    Procesa cada paquete capturado, extrae información relevante y actualiza el DataFrame en tiempo real.
    
    Args:
        packet (scapy.packet.Packet): Paquete capturado de la red.
    """
    global df_real_time
    if packet.haslayer(scapy.IP):
        packet_info = {
            "src": packet[scapy.IP].src,
            "dst": packet[scapy.IP].dst,
            "sport": packet[scapy.TCP].sport if packet.haslayer(scapy.TCP) else None,
            "dport": packet[scapy.TCP].dport if packet.haslayer(scapy.TCP) else None,
            "payload": len(packet.payload)
        }
        
        # Convertir el diccionario en un DataFrame
        new_packet_df = pd.DataFrame([packet_info])
        
        # Concatenar el nuevo DataFrame con el DataFrame global
        df_real_time = pd.concat([df_real_time, new_packet_df], ignore_index=True)
        
        # Limpiar la salida anterior para actualización en tiempo real
        clear_output(wait=True)
        
        # Mostrar las últimas 5 filas del DataFrame actualizado
        display(df_real_time.tail(5))
        
        # Generar gráfico de bytes enviados por IP de origen
        df_real_time.groupby("src")["payload"].sum().sort_values().plot(kind='barh', title='Bytes enviados por IP origen')
        plt.show()


if __name__ == "__main__":
    """
    Captura paquetes en tiempo real utilizando Scapy y ejecuta el análisis.
    """
    scapy.sniff(count=0, iface="wlp0s20f3", prn=process_packet, store=False)
