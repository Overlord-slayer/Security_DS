## Proyecto: Modelo de Detección de Fraude con Perfiles Complejos

Este proyecto desarrolla un modelo de clasificación binaria para detección de fraudes financieros utilizando LightGBM, con énfasis en **reducir los falsos positivos** en perfiles de usuarios con comportamiento complejo pero legítimo.

---

## Objetivo General

* Detectar transacciones fraudulentas.
* Minimizar falsos positivos en transacciones legítimas, especialmente en clientes con comportamiento inusual.

---

## Principales Contribuciones

1. **Reglas híbridas de perfil complejo** combinando percentiles poblacionales y z-scores personalizados por cliente.
2. **Heurística de dispersión** para detectar variabilidad inusual en comportamiento de gasto y horarios.
3. **Ajustes personalizados en el modelo**:

   * Pesos diferenciados en el entrenamiento.
   * Umbrales personalizados en predicción.
   * Métricas de evaluación que penalizan más los falsos positivos complejos.

---

## Variables Clave

### a. **Regla de Negocio Híbrida**

Detecta clientes que:

* Gastan mucho comparado con el resto (percentil 90).
* O muestran cambios extremos en su gasto anual (z-score > 2).

Combinado con:

* Alta frecuencia con el mismo comercio.
* Múltiples compras online.

### b. **Heurística de Dispersión**

Detecta perfiles con:

* Alta desviación estándar en montos (`client_std_amt`).
* Alta variabilidad temporal (`client_std_time`).

### c. **Variable Final**: `is_complex_profile`

Marcada como `True` si cumple con al menos una de las dos condiciones anteriores.

---

## ⚖️ Peso y Umbral Diferenciado

* **Pesos en entrenamiento**:

  * Complejo: 1
  * No complejo: 3
* **Umbral de predicción**:

  * Complejo: 0.7
  * No complejo: 0.5

---

## ⚙️ Métricas de Evaluación Personalizadas

1. **`tp_over_penalized_fp`**: Penaliza falsos positivos en perfiles complejos.
2. **`f1_penalized`**: Penaliza F1 según cantidad de FP complejos.
3. **`precision_boosted`**: Reduce precisión proporcionalmente al número de FP complejos.

---

## Resultados Observados

* Se redujo la proporción de FP en perfiles complejos.
* El modelo mantuvo una alta precisión general (> 0.99) con recall conservador.
* El uso de heurísticas híbridas permitió capturar perfiles legítimos no convencionales que eran anteriormente mal clasificados como fraude.

---

## 🔗 Conclusión

Este enfoque demuestra que combinar reglas de negocio basadas en comportamiento con estadísticas robustas (z-score, dispersión) permite construir un sistema de detección de fraude **más justo**, sin castigar a clientes de alto valor o con comportamiento atípico.

El sistema es adaptable a otras industrias o segmentos donde los comportamientos extremos no deben confundirse con actividad fraudulenta.

---

## Requisitos Técnicos

* Python 3.8+
* Pandas, NumPy, LightGBM, Seaborn, Scikit-Learn, Scipy

---


## Referencias

* [LightGBM Docs](https://lightgbm.readthedocs.io)
* [Z-score Explanation](https://en.wikipedia.org/wiki/Standard_score)
* Trabajo inspirado en estrategias reales de detección de fraude bancario (papers y datasets públicos)



## 6. Instalación de dependencias y LightGBM con GPU

```bash
sudo apt-get install -y libboost-dev libboost-system-dev libboost-filesystem-dev
sudo apt-get install -y cmake build-essential libopencl-dev ocl-icd-opencl-dev

git clone --branch v3.3.5 --recursive https://github.com/microsoft/LightGBM.git
cd LightGBM
mkdir build
cd build
cmake -DUSE_GPU=1 ..
make -j4
cd ..
pip install ./python-package
