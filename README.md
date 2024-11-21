

             



![alt text](image.png)


   # PROYECTO INDIVIDUAL 02
   # TELECOMUNICACIONES 


![alt text](image-1.png)



# Análisis de comportamiento de accesos a internet y KPIs



## Contexto

Bienvenidos a este repositorio, cuyo objetivo principal es la realización de un estudio para una destacada empresa de telecomunicaciones en Argentina. Dicha empresa nos solicitó elaborar un análisis completo para comprender el comportamiento de este sector a nivel nacional. En este repositorio encontrarás Un análisis exploratorio de datos (EDA). KPI's propuestos para medir el progreso y el éxito en áreas clave y un dashboard interactivo desarrollado en Power BI para visualizar los resultados de manera efectiva.


## Índice

- #### Contexto
- #### Introducción
- #### Repositorio  
- #### Instalación
- #### (EDA) Análisis Exploratorio de Datos 
- #### KPI's
- #### Dashboard 
- #### Conclusiones 
- #### Recomendaciones 
- #### Contacto 




## Introducción


Las telecomunicaciones son una piedra angular de la sociedad moderna, ya que permiten la transmisión de información a largas distancias mediante diversos medios, como cables, ondas de radio, fibra óptica y satélites. Estas no solo conectan a personas y comunidades, sino que también impulsa el desarrollo económico, la educación y la innovación tecnológica en todo el mundo. 

Este proyecto se centra en un análisis del comportamiento del internet a través de sus diferentes tecnologías en Argentina. Para ello, se utilizaron datos obtenidos de archivos de Excel, realizando un análisis exploratorio de datos (EDA). Además, se desarrollaron KPIs objetivos para el monitoreo de tendencias y, con base en los resultados, se creó un dashboard interactivo en Power BI que permite visualizaciones dinámicas
 

## Repositorio  

* Datos: Archivos utilizados para en analisis ( `<Internet.xlsx>`,  `<Telefonia_fija.xlsx>` y  `<Television.xlsx>`)
* Notebooks: contiene un script de Python donde se encuentra el EDA y los KPI's (**EDA.ipynb**). 
* Dashboards: 
* README.md: Es este archivo, que documenta el analisis realizado. 




## Instalación

#### 1. Clona el repositorio:

`$ git clone https://github.com/tu_usuario/nombre_repositorio.git` 

#### 2. Instala las dependencias de Python:

`$ pip install pandas matplotlib seaborn`

#### O tambien puedes hacer con el requirements.txt

`$ pip install Requirements.txt`


#### 3. *Abre el archivo con Power BI Desktop*





![alt text](image-3.png)

    

## (EDA) Análisis Exploratorio de Datos

Este EDA se realizo en **Python** utilizando las librerias *Pandas*, *seaborn* y *matplotlib*.

                
+ **Carga de datos**: Se utilizaron los archivos de excel Internet, telefonia fija y television. 
+ **Limpieza de datos**: identificacion de valores faltantes, duplicados, outliers con el metodo de IQR y boxplots  
+ **Visualizaciones**: 
    * *graficos de barras*: para ver ingresos, evolucion de accesos por tipo de tecnologia, velocidades, entre otros. 
    * *Graficos de dispersion*: para comparacion de Dial-BAF
    * *Graficos de lineas multiples*: para ver incrementos de acceso por provincias






Durante este proceso se establecieron las bases para comprender el comportamiento de los datos, identificar patrones y trazar el 
camino para el desarrollo de los **KPI's**. 


## KPI's

Los KPI´s que son **indicadores clave de desempeño**, utilizados para medir el progreso y el éxito en áreas clave. 


### KPI 1: .



   `*Calculo: KPI = ((nuevo acceso - acceso actual) / acceso actual)* 100*`

#### Donde: 

* Nuevo acceso: se refiere al número de hogares con acceso a Internet después del próximo trimestre.
* Acceso actual: se refiere al número de hogares con acceso a Internet en el trimestre actual.




### KPI 2: Participación de Fibra Óptica en el mercado total de accesos. 

* **Objetivo**: cuantificar qué porcentaje de los accesos totales en un país utiliza la tecnología de Fibra Óptica, en comparación con otras tecnologías 
* **Formula**: 
  
  ||`participacion de fibra optica (%) = (total de accesos con Fibra optica en el pais/total de accesos de todas las tecnologias en el pais) x 100`
        
### pasos para calcularlo:  

* **Sumar los accesos de fibra óptica en todo el país** : Esto implica sumar los valores de la columna Fibra óptica en todas las provincias y períodos disponibles.
* **Sumar los accesos totales en el país**: Esto se obtiene sumando los valores de la columna Total, que incluye todas las tecnologías.
* **Dividir los accesos de fibra óptica entre los accesos totales**: Este cociente se multiplica por 100 para expresar el resultado como un porcentaje.



### KPI 3: Crecimiento trimestral relativo de accesos a Cablemodem en comparación con Fibra Óptica y ADSL".

* **Objetivo**: Identifica si el crecimiento de Cablemodem es superior o si está siendo superado por otras tecnologías.
* **Formula**: 

   `*Accesos cablemodem actual - accesos Cablemodem anterior / accesos cablemodem anterior x 100*`

### pasos para calcularlo: 


* **calcular el crecimiento trimestral**: Utiliza la fórmula del crecimiento porcentual trimestral para cada tecnologia (Cablemodem, Fibra óptica, y ADSL)
* **Calcular la relación de crecimiento**: Comparar el crecimiento de Cablemodem con las otras tecnologías:
  `*Relación_cablemodem_fibra= Crecimiento cablemodem/ crecimiento fibra *`

  `*Relación_ADSL_fibra= Crecimiento cablemodem/ crecimiento ADSL *`

* **Calcular los periodos de interes**: (del 2020 al 2023)



![alt text](image-2.png)



## Dashboard 

Podras encontrar en el archivo de PowerBI Telecomunicaciones.pbix  visualizaciones para analizar tendencias y KPIs de manera interactiva. 




## Conclusiones 

En conclusión, la fibra óptica es claramente superior en términos de velocidad, fiabilidad, latencia y capacidad de ancho de banda, aunque el cablemodem puede ser una opción más económica y disponible, especialmente en áreas donde la infraestructura de fibra no está desplegada. Sin embargo, la tendencia es que la fibra óptica se está convirtiendo en el estándar debido a su capacidad para soportar la creciente demanda de datos y la transición hacia una mayor digitalización.


## Recomendaciones 

El análisis demuestra que la **fibra óptica** es claramente superior en términos de velocidad, fiabilidad, latencia y capacidad de ancho de banda. Sin embargo, el **cablemódem** puede ser una opción más económica y accesible, especialmente en áreas donde la infraestructura de fibra aún no está disponible. No obstante, la tendencia indica que la fibra óptica se está convirtiendo en el estándar debido a su capacidad para soportar la creciente demanda de datos y la transición hacia una mayor digitalización, por lo que se propone acelerar la migración hacia esta tecnología.

Finalmente, se sugiere enfocarse en **inversiones en infraestructura**, la adopción de nuevas tecnologías y la expansión de la televisión por suscripción. Con estas medidas, aseguraríamos un aumento en la velocidad, diversidad y calidad del servicio, destacándonos frente a la competencia, garantizando la comodidad de nuestros clientes actuales y proyectando un incremento en la captación de nuevos suscriptores.



## Contacto

Para cualquier duda, aclaración o recomendación, puedes escribirme a: martha.cvasq@gmail.com



























































