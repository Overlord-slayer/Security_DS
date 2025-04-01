# PARTE 1 y 2 Análisis de Tráfico de Red

## **Análisis del tráfico**

1. **IP de origen dominante**: La mayoría del tráfico proviene de **10.1.10.53**, lo que sugiere que esta máquina está generando una cantidad significativa de solicitudes.
2. **IP de destino más frecuente**: La máquina **10.1.10.53** se comunica principalmente con **84.54.22.33**.
3. **Puerto de destino más utilizado**: El puerto **53** es el más utilizado, lo que indica tráfico DNS.
4. **Tráfico constante**: Se observa un flujo estable de bytes enviados, característico de sistemas que realizan consultas DNS continuas.
5. **Cantidad de paquetes enviados**: La IP **10.1.10.53** es la que más paquetes ha enviado en comparación con otras IPs analizadas.
6. **Puertos de origen usados**: Además del puerto **53**, se han identificado los puertos **15812** y **23903**, lo que sugiere posibles conexiones adicionales.

## **¿Es común este comportamiento?**
El tráfico hacia el puerto **53** es común en redes con alto uso de consultas DNS, sin embargo, 
si **10.1.10.53** no es un servidor DNS oficial y está generando un volumen inusual de tráfico, podría indicar:
- **Un posible ataque DNS flood** (intento de sobrecargar un servidor DNS).
- **Comportamiento sospechoso o actividad maliciosa**, como exfiltración de datos mediante túneles DNS.

# PARTE 3 Análisis de Datos Enviados al Puerto Destino
A continuación, se presentan algunos ejemplos de payloads capturados:

**Payload 1:** `b'\xef\xbf\xbdPNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00'`

**Payload 2:** `b':\xef\xbf\xbdle:\xc7\xa9\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\x0c\xef'`

**Payload 3:** `b"\xef\xbf\xbd\xef\xbf\xbd^n\xef\xbf\xbd''\xef\xbf\xbd\xef\xbf\xbd\xef"`

**Payload 4:** `b'\xe4\x8e\x91Bj_\xef\xbf\xbda\r\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd'`

**Payload 5:** `b'\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xcb\xb4\xef\xbf\xbd\x16\xef\xbf\xbd\xef\xbf'`

Estos provienen del analisis_paquetes.pcap

## Análisis
Se identificaron los siguientes problemas en los datos capturados:

1. **Presencia de datos binarios de una imagen PNG:**  
   - En el Payload 1, los primeros bytes sugieren que el contenido es de un archivo PNG.
   - Si el puerto destino no espera archivos de imagen, este dato podría ser sospechoso.

2. **Uso del carácter de reemplazo (U+FFFD):**  
   - En los Payloads 2-5, aparecen varias instancias del byte `b'\xef\xbf\xbd'`, que representa un carácter no válido en UTF-8.
   - Esto podría indicar datos corruptos, una codificación incorrecta o intentos de evasión de detección.

