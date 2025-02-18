# **README - Actividad 3: Análisis Estático de Malware**

## **Introducción**
En esta actividad, se realizó un análisis estático para determinar si ciertos archivos contenían malware. **Ninguno de estos archivos debe ejecutarse**, ya que se ha confirmado que contienen código malicioso. El propósito de este ejercicio es únicamente el análisis.

El archivo **sample_qwrt_dk2_unpacked** es la versión desempaquetada del malware. Generalmente, cuando un archivo está empaquetado, su análisis es más complejo, ya que ciertas verificaciones, como la detección de **DLLs**, pueden no ser visibles.

Para más detalles, consulte el notebook **actividad3_f1.ipynb**, donde se comparan los archivos empaquetados y desempaquetados.

---

## **Verificación de Empaquetado: Archivo 1 - sample_vg655_25th.exe**

![Verificación de empaquetado - sample_vg655_25th.exe](https://github.com/user-attachments/assets/cf35f08c-6260-41b3-a978-5b575505ca5c)

### **Resultados de Análisis**
- **Fuente**: [Hybrid Analysis](https://www.hybrid-analysis.com/sample/ed01ebfbc9eb5bbea545af4d01bf5f1071661840480439c6e5babe8e080e41aa)

---

## **Verificación de Empaquetado: Archivo 2 - sample_qwrty_dk2**

![Verificación de empaquetado - sample_qwrty_dk2](https://github.com/user-attachments/assets/e6842043-37d6-4cbb-95c3-43bd0e44efa6)

### **Resultados de Análisis**
- **Fuente**: [Hybrid Analysis](https://www.hybrid-analysis.com/sample/7f33cae97917def9538de58d09a713d81ed92ca7ecc5e79a774e3e032e668d23)

---

## **Conclusión**
El análisis estático permitió identificar diferencias clave entre los archivos empaquetados y desempaquetados. Se recomienda utilizar herramientas avanzadas para inspeccionar **DLLs** y otras características que pueden indicar la presencia de malware.

**Recuerdordatorio:** Nunca ejecute archivos sospechosos en un entorno no controlado.

