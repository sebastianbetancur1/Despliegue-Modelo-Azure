# Despliegue-Modelo-Azure
En este proyecto se realiza el despliegue en AZURE del modelo de clasifiación del Titanic.


Elaborado por: Andrés Felipe Acevedo y Sebastián Betancur

ENDPOINT: http://e37444f5-fdad-4308-a698-99e30afc45d8.eastus2.azurecontainer.io/score


Paso a paso del despliegue:
1. Creación Workspace en azure ml
2. Entrenamiento del ejercicio clásico del TITANIC por medio de un RandomForest
3. Registro del modelo en AZURE
4. Despliegue del modelo en Azure Container Instance

Seguimos paso a paso el tutorial indicado por el profesor en las clases y desplegamos un modelo entrenado localmente en Azure ML. 
Posteriormente, realizamos un paso a producción implementando el API POSTMAN y finalmente se realiza la carga del repositorio a GITHUB y se adjunta un video donde se interactúa con la API ejecutando un ejemplo de clasificación del modelo.
