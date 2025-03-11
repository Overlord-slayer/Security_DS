# [Home](../README.md)

# Conclusiones

**Para ambos algoritmos, ¿para qué número de clústeres se obtiene el coeficiente de Silhouette más alto?**
- Según el gráfico de análisis de Silhouette, el coeficiente más alto se obtiene alrededor de 9 o 10 clusters para K-Means.
- Para DBSCAN, pareciera haber un menor número de clusters efectivos.

**¿En qué medida coincide el coeficiente de Silhouette con el método del codo?**
- En el método del codo, se observa un cambio de pendiente significativo alrededor de 4 a 5 clusters.
- Sin embargo, el coeficiente de Silhouette sigue aumentando hasta 9-10 clusters, lo que sugiere que aunque el método del codo indica un número óptimo menor, la cohesión de      los clusters mejora con más grupos.

**Según los resultados obtenidos de ambos algoritmos, ¿Cuántas familias cree que existen entre los ejemplares de malware proporcionados?**
- K-Means sugiere alrededor de 9-10 clusters, según el coeficiente de Silhouette.
- DBSCAN parece encontrar menos clusters, posiblemente debido a la presencia de ruido o datos dispersos.
Al final, segun en el conjunto de datos que se genero, se determinaron 9. Algo que da cosa, es el tema del desempaquetado, posiblemente no se realizo bien, pero esa es la conclusion a la que se llega.

**¿En qué medida coincide el análisis de similitud con las familias encontradas utilizando los algoritmos de partición, para ambas características (strings, llamadas a funciones)?**
- Los grafos de similitud muestran agrupaciones basadas en llamadas a funciones API y en strings.
- Se pueden observar familias bien definidas que coinciden en gran medida con los clusters obtenidos por K-Means.
- Sin embargo, puede haber diferencias en DBSCAN debido a su tratamiento de ruido y outliers, lo que puede hacer que algunos ejemplares sean clasificados de manera diferente.

En conclusión, K-Means y DBSCAN muestran agrupaciones similares, aunque DBSCAN puede ser más sensible a la estructura de los datos. El análisis de similitud también refuerza la existencia de múltiples familias, con una fuerte coincidencia entre los métodos. 
# UMBRAL DE 3
![Umbral de 3](image.png)

# UMBRAL DE 6
![Umbral de 6](image-1.png)

# UMBRAL DE 9
![Umbral de 9](image-2.png)

Se observo que entre mas grande el umbral, mayor cercanica tenian los elementos. En este caso, para String se nota mucho antes, pues estan mas dispersos
los valores. Aun asi, el de funciones da a entneder que los elementos tiene valores muy similares, y entre menor unbral, se hace mas especifico para cada
uno de los casos.
