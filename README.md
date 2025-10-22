Para correr el programa en la terminal coloque:
flask run


Si el microservicio necesitara comunicarse con otro que guarda el historial de cálculos en una base de datos, 
cambiaría el diseño para que, cada vez que se calcule un factorial, el servicio envíe esos datos al otro por medio de una petición HTTP POST. 
Podría usar la librería requests para mandar el número, su factorial y si es “par” o “impar”.
Así, cada microservicio tendría su propia tarea, uno hace los cálculos y el otro guarda la información.
Esto ayuda a que los servicios no dependan del otro, y puedan trabajar por separado.
