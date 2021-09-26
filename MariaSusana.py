# -*- coding: utf-8 -*-
"""
Created on Mon May 17 20:26:49 2021

@author: MARIA SUSANA OCROSPOMA ANCALLI

"""

######################
SOLUCIÓN BÁSICO PYTHON
######################
import numpy as np
import pandas as pd

path='D:/REPASO PERSONAL/PYTHON/'
data=pd.read_csv(path+'data.csv',sep=',')
data.rename(columns={'nivel_educ':'grado'}, inplace=True)

############################################################################
1. ¿Cuál es el ingreso promedio de los clientes con formación universitaria?
############################################################################
np.mean(data[data.grado=='UNIVERSITARIA']['ingreso'])


############################################################################
2. ¿Qué porcentaje de missings tiene la variable exp_sf?
############################################################################
((data.exp_sf.isnull().sum(axis = 0))/(len(data.exp_sf)))*100


############################################################################
3. ¿Qué porcentaje de clientes tiene formación universitaria?
############################################################################
((np.sum(data.grado=='UNIVERSITARIA'))/len(data))*100


############################################################################
4. ¿Cuál es el promedio de la variable edad?
############################################################################
np.mean(data.edad)


############################################################################
5. ¿Qué porcentaje de clientes de Lima presentan missings en la variable exp_sf?
############################################################################
(np.sum(data[data.zona=='Lima'].exp_sf.isnull())/np.sum(data.zona=='Lima'))*100


############################################################################
6. ¿Cuál es la probabilidad de no tener atraso si tu edad es menor a 35 años?
############################################################################
np.mean((data.atraso==0)&(data.edad<35))

############################################################################
7. ¿Cuál es la probabilidad de no tener días de atraso e ingresos menores a 5000?
############################################################################
np.mean((data.atraso==0)&(data.ingreso<5000))


############################################################################
8. ¿Cuál es el nivel de ahorro promedio de los clientes con educación técnica y vivienda
propia?
############################################################################
np.mean(data[(data.grado=='TECNICA')&(data.vivienda=='PROPIA')]['nivel_ahorro'])


############################################################################
9. ¿Cuál es el promedio de la variable ingreso?
############################################################################
np.mean(data.ingreso)


############################################################################
10. ¿Cuál es la probabilidad de no tener atraso si tu edad es mayor a 45 años?
############################################################################
np.mean((data.atraso==0)&(data.edad>45))



############################################################################
11. ¿Qué porcentaje de clientes no tiene educación?
############################################################################
((np.sum(data.grado=='SIN EDUCACION'))/len(data))*100


############################################################################
12. ¿Cuál es el atraso promedio de los clientes que viven en vivienda familiar?
############################################################################
np.mean(data[data.vivienda=='FAMILIAR']['atraso'])


############################################################################
13. ¿Cuál es la mediana de la variable score?
############################################################################
np.median(data.score)


############################################################################
14. ¿Cuál es el percentil 25 de la variable ingreso?
############################################################################
np.percentile(data.ingreso,25)


############################################################################
15. ¿Cuál es el nivel de ahorro promedio de los clientes con educación secundaria y
vivienda familiar?
############################################################################
np.mean(data[(data.grado=='SECUNDARIA')&(data.vivienda=='FAMILIAR')]['nivel_ahorro'])


############################################################################
16. ¿Cuál es el atraso promedio de los clientes que viven en vivienda propia?
############################################################################
np.mean(data[data.vivienda=='PROPIA']['atraso'])


############################################################################
17. ¿Cuál es la probabilidad de no tener atraso si los ingresos son mayores a 5000?
############################################################################

np.mean((data.atraso==0)&(data.ingreso>5000))

############################################################################
18. ¿Cuál es la probabilidad de no tener días de atraso y ser menor a 25 años?
############################################################################
np.mean((data.atraso==0)&(data.edad<25))



############################################################################
19. ¿Qué porcentaje de clientes de Cajamarca presentan missings en la variable deuda_sf?
############################################################################
(np.sum(data[data.zona=='Cajamarca'].deuda_sf.isnull())/np.sum(data.zona=='Cajamarca'))*100



############################################################################
20. ¿Cuál es el nivel de ahorro promedio de los clientes sin educación y vivienda familiar?
############################################################################
np.mean(data[(data.grado=='SIN EDUCACION')&(data.vivienda=='FAMILIAR')]['nivel_ahorro'])

