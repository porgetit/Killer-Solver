Killer Sudoku Solver
====================

**Killer Sudoku** es una variante del Sudoku en la que, además de los bloques regulares de 9 celdas, también existen "jaulas" adicionales que limitan aún más las combinaciones de números que pueden ir en cada celda. Estas jaulas son la única diferencia con el Sudoku tradicional. Mientras que en el Sudoku clásico los números del 1 al 9 deben aparecer una sola vez en cada fila, columna y bloque, en Killer Sudoku se añade una restricción extra: el mismo número no puede repetirse dentro de una jaula, y además, la suma de los números en cada jaula debe coincidir con un valor específico.

En Sudoku, las limitaciones adicionales suelen ser beneficiosas para el jugador, ya que reducen considerablemente las combinaciones posibles. En Killer Sudoku, sin embargo, hay menos celdas iniciales llenas (si es que alguna lo está).

**Cómo funciona**
El algoritmo trabaja llenando el tablero con números, probando si la combinación es válida y, si no lo es, intenta con una combinación diferente. Aunque esta es una explicación simplificada, el proceso básico consiste en ir rellenando las celdas una por una hasta completar todo el tablero. Una vez lleno, se valida la solución, y si no es válida, el valor de la última celda se elimina y se prueba otro número, repitiendo la validación. Este proceso continúa hasta que se hayan probado todas las posibles combinaciones para la última celda. Si ninguna es válida, el valor de la celda anterior se reemplaza por otro valor y el proceso comienza nuevamente.

Probar todas las combinaciones posibles no es una opción viable, ya que el número de combinaciones es extremadamente alto: 6,670,903,752,021,072,936,960 combinaciones posibles para ser exactos. Por esta razón, es esencial limitar las combinaciones que se prueban, eliminando primero aquellas que son inválidas, como los duplicados o los valores en jaulas que exceden la suma requerida. Para cada celda, se calculan un valor mínimo y un valor máximo, los cuales indican el rango de posibles valores que puede tener esa celda.

Por ejemplo, si una jaula tiene una suma de 17 y está formada por dos celdas, el valor mínimo sería 8, ya que ningún número menor que 8 sumaría 17 con otro número. El valor máximo sería 9. Por lo tanto, las celdas solo pueden tener 8 o 9, y no tiene sentido probar otros números en esa jaula. Si los valores posibles ya están ocupados, entonces la combinación es inválida y se detiene la búsqueda en esa rama.

Otra restricción sencilla ocurre en las jaulas de tamaño 2 con un número par. En estos casos, no se puede usar un valor que sea la mitad de ese número. Por ejemplo, si una jaula tiene el valor 10 y contiene dos celdas, no se puede usar el número 5, ya que ambas celdas tendrían que tener el mismo valor, lo cual no es permitido. Esto también ayuda a reducir las combinaciones a probar.

Cada vez que una jaula tiene valores asignados, se resta el total de esa jaula y se recalculan los valores mínimos y máximos para las celdas restantes, optimizando aún más el proceso.

**Cómo usarlo**
El código se puede ejecutar desde Python creando una estructura de tablero y una lista de jaulas. El tablero es simplemente una lista bidimensional que representa los valores de las celdas. Un 0 indica que una celda está vacía. En los rompecabezas de nivel experto, todas las celdas estarán inicialmente vacías. La lista de jaulas está formada por tuplas, donde cada tupla representa una jaula. El primer valor de la tupla es la suma que debe alcanzar la jaula, y el segundo valor es una lista de coordenadas que indican las celdas dentro de esa jaula. Las coordenadas son indexadas desde 0.

Para resolver un rompecabezas de Sudoku desde Python, se llama al método `solve`, con la firma: `def solve(board: Board, cages: Cages) -> bool:` La solución se reflejará en el tablero proporcionado como parámetro.

El solucionador también se puede ejecutar desde la línea de comandos utilizando el archivo `solve.py` y proporcionando el nombre del archivo del rompecabezas a resolver. Por ejemplo, para resolver el rompecabezas `expert-1.json`, se puede usar el siguiente comando:

`$ python solve.py expert-1.json`




