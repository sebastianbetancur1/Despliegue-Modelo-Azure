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

Los datos a ingresar al POSTMAN son:

1. Pclass: Variable ordinal -> corresponde al tiquete adquirido por el pasajero dentro del titanic (ejm: 1 es tiquete de primera clase)
2. Age: variable discreta -> corresponde a la edad del pasajero
3. Fare: variable continua -> corresponde al valor del tiquete del pasajero
4. Sex_female: variable binaria -> indica si el pasajero es de genero femenino
5. Sex_male: variable binaria -> indica si el pasajero es de genero masculino
6. Family_size: variable discreta -> indica el número de familiares que tiene abordo que tiene el pasajero

Hacer uso de esta estructura de datos para realizar pruebas.
