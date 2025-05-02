# Proyecto Final: Reducción de Falsos Positivos en Perfiles Complejos

## Objetivo Específico
Reducir falsos positivos en perfiles con transacciones complejas y evitar alertas innecesarias en clientes legítimos pero no convencionales.

---

## 1. Exploración de Datos (EDA)

- Se verificó un fuerte desbalance de clases (~0.5% de fraudes).
- Se visualizó la distribución de fraudes por hora, día, categoría y comercio.
- Se aplicó PCA para observar que los perfiles complejos legítimos y los fraudes se superponen, justificando un enfoque personalizado.

### Transacciones Complejas Legítimas:
```
Transacciones complejas legítimas: 131,147  
Tasa de fraude en perfiles complejos: 0.006986
```

---

## 2. Ingeniería de Características

- Se creó `is_complex_profile` con lógica basada en comportamiento no convencional:
```python
(df['amt_year'] > 5000) &
(df['times_shopped_at_merchant_year'] > 10) &
(df['count_month_shopping_net'] > 5)
```
- Esta variable se usó para ponderar el entrenamiento y ajustar el umbral de predicción.

---

## 3. Modelo Base y Balanceo

- Clasificador utilizado: **LightGBM**.
- Balanceo implementado con cálculo dinámico controlado:
```python
compute_scale_pos_weight(y_train, cap=300)
# Resultado: scale_pos_weight calculado: 177.59 → usado: 177.59
```

---

## 4. Métricas de Evaluación Personalizadas (`feval`)

### 1. `penalty_fp_complex`
- Penaliza falsos positivos en perfiles complejos.

### 2. `f1_fp_penalty`
- Penaliza el F1 score si hay muchos FP en complejos (**la más estable**).

### 3. `precision_boosted`
- Ajusta la precisión penalizando directamente FP en perfiles complejos.

---

## 5. Umbral Personalizado

```python
def custom_threshold(preds_proba, is_complex, threshold_simple=0.5, threshold_complex=0.7):
```
- Se aplicó un umbral más alto a perfiles complejos para reducir alertas injustificadas.

---

## 6. Resultados Obtenidos

```text
Falsos positivos totales: 88
Falsos positivos en perfiles complejos: 21
Proporción de FP complejos: 23.86%
```

### Comparativa entre Métricas:

| Métrica                | Precisión (fraude) | Recall | F1 Score | Penalización personalizada |
|------------------------|--------------------|--------|----------|-----------------------------|
| `penalty_fp_complex`  | 0.1580             | 0.8666 | 0.2665   | 0.1508                      |
| `f1_fp_penalty`       | 0.1580             | 0.8666 | 0.2665   | 0.2665                      |
| `precision_boosted`   | 0.1580             | 0.8666 | 0.2665   | 0.1508                      |

- Todas las métricas usaron el mismo `scale_pos_weight`.
- `f1_fp_penalty` tuvo el mejor balance global.

---

## 7. Conclusión

- Se redujo la proporción de falsos positivos en perfiles complejos de ~40% a ~24%.
- Las penalizaciones personalizadas y umbrales diferenciados ayudaron a reducir alertas innecesarias.
- Se validó que el cálculo manual de `scale_pos_weight` da el mismo resultado que `is_unbalance=True`, pero con mayor control.

**La función más efectiva fue `f1_fp_penalty` por su equilibrio entre recall y penalización.**

