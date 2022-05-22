# Proyecto-1
# Data cleaning &amp; wrangling

El objetivo de este proyecto es limpiar un archivo de Kaggle sobre el ataque de tiburones 🦈

## Hipótesis
Se ha trabajado sobre la hipótesis: ¿El estado New South Wales (Australia) es el que mayor número de ataques sufre?

## Cleaning
Para ello se ha relaizado una primera exploración de los datos, fijándonos sobre todo en los missing values y su distribución así como las correlaciones entre ellos a lo largo del dataframe.
A continuación se han relaizado las tareas propias de data clenaning: eliminar datos duplicados y nulos tanto en columnas como en filas, se han formateado los valores para obtener un resultado homogéneo, se han borrado aquellas columnas que no son relevantes para este estudio y se han cruzado datos de diferentes columnas para deducir el número de NaN.

## Estudio
Se ha realizado el mismo estudio en dos periodos de tiempo, 1998-2018 y 1918-2018, para comparar los resultados y ver si se han producido variaciones. El estudio se ha realizado con el fin de contabilizar el número de víctimas en lugar del número de ataques.

## Conclusiones
Se han obtenido los mismos resultados para los dos periodos de tiempo.
Se observan diferencias en cuanto a los resultados estudiados según el ratio calculado debido a la influencia del qiulometraje de algunos estados.
