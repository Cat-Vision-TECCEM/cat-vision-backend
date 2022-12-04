# CatVision: Modelos de Inteligencia Artificial Implementados

**Integrantes:** *David Rodríguez Fragoso, Diego Armando Ulibarri Hernández, Eduardo Rodríguez López, Erick Hernández Silva, Israel Sánchez Miranda, Liam Garay Monroy, María Fernanda Ramírez Barragán, Octavio Andrick Sánchez Perusquia, Raúl Youthan Irigoyen Osorio,  Renata de Luna Flores, Roberto Valdez Jasso.*

05 de noviembre de 2022

*Inteligencia artificial avanzada para la ciencia de datos II*


## Problema a resolver
En este documento se tiene el propósito de informar los detalles relacionados con los modelos de Inteligencia Artificial implementados para el proyecto CatVision, así como la relación que cada uno tiene con los demás modelos, sus propósitos específicos y el orden en el que fueron utilizados. Estos modelos en conjunto buscan lograr identificar dentro de un refrigerador con especificaciones controladas los productos pertenecientes a cada una de las distribuidoras que han contratado el servicio con el fin de proveer esta información a los servidores de CatVision.

## Pipeline
El esquema de trabajo que se sigue para ensamblar los resultados de los modelos entre sí es el siguiente:

<img src="https://imgur.com/a/2RT1FTA" alt="Diagrama de pipeline de modelos de CatVision">

La forma en la que cada uno de los cuatro modelos presentados en el diagrama trabaja es la siguiente:
- **MS1** ***(Modelo de Segmentación 1)***: Este modelo se encarga de detectar el contorno del refrigerador y recortar la imagen de tal manera que únicamente esté presente el objeto con los productos en su interior.
- **MS2** ***(Modelo de Segmentación 2)***: Este modelo recibe la imagen del refrigerador y procede a detectar formar los contornos de los productos que podrían pertenecer a la distribuidora en cuestión, una vez que los encuentra, recorta únicamente el producto encontrado, si se detecta que hay un espacio potencialmente vacío, se envía al MC2.
- **MC1** ***(Modelo de Clasificación 1)***: Este modelo recibe las imágenes que contiene exclusivamente al producto y realiza una clasificación para lograr identificar cuál es el producto en cuestión. Si el nivel de certeza máximo es relativamente bajo en comparación con los niveles máximos estándar, se enviará al MC2.
- **MC2** ***(Modelo de Clasificación 2)***: Este modelo recibe aquellos espacios potencialmente vacíos o imágenes de aquellos productos que no arrojaron un nivel de certeza relativamente normal, por lo que estas imágenes serán clasificadas entre espacios vacíos u objetos no reconocibles. 

Una vez que el pipeline ha sido ejecutado completamente, la información de ambos modelos de clasificación es enviada al servidor para su posterior procesamiento.

### Especificaciones de los modelos
- **MS1 (Modelo de Segmentación 1):** 
    + ***Tecnología implementada:*** Teachable Machine.
- **MS2 (Modelo de Segmentación 2):**
    + ***Tecnología implementada:*** OpenCV.
- **MC1 (Modelo de Clasificación 1):**
    + ***Tecnología implementada:*** Tensorflow.
    + ***Estructura implementada:*** VGG 16 (Modelo pre-entrenado para clasificación multi-categórica).
    + ***Técnicas de ensamble:*** Random Forest de 3 modelos.
- **MC2 (Modelo de Clasificación 2):** Este modelo recibe aquellos espacios potencialmente vacíos o imágenes de aquellos productos que no arrojaron un nivel de certeza relativamente normal, por lo que estas imágenes serán clasificadas entre espacios vacíos u objetos no reconocibles. 
    + ***Tecnología implementada:*** Tensorflow.
    + ***Estructura implementada:*** Clasificación binaria.
    + ***Técnicas de ensamble:*** N/A.

### Tratamiento de los datos
Dado que se trata de un ambiente controlado, puesto que la mayor parte de las variables en juego son predominantemente constantes, el tratamiento de datos no requirió de una gran cantidad de data augmentation, ya que lo único que realmente tiene el potencial de ser variable es el brillo y el contraste de las imágenes. 

Así mismo, el tamaño del dataset se mantuvo en aproximadamente 20 imágenes por producto, sin embargo la porción de datos correspondientes a la validación de resultados se mantuvo en 20%. Después, se añadió una capa de regularización de tamaño de imágenes, que en keras tiene el nombre de rescaling, esto se hizo con el fin de mantener los datos en una escala homogénea, permitiendo identificar más rápidamente el mínimo local durante el entrenamiento del modelo y que los resultados de los modelos de clasificación no se vean afectados. Así mismo, se añadió una capa de data augmentation que alteran el brillo, el contraste y el zoom de las imágenes en un rango de 20%.
