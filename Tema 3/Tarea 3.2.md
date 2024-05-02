# Tarea 3.2. Caso práctico Automata Finito

En la siguiente actividad veremos un caso de autómata finito en la vida cotidiana, como también su aplicación y la implementación del mismo.

Antes que nada, algo importante a tomar en consideración es:

## ¿Qué es un Autómata Finito?
Como su nombre indica, es una máquina con un **número finito** de estados que lee símbolos de una cinta de entrada infinita, el cual se puede representar por medio de un *grafo* dirigido, y un grafo es un conjunto de vértices o nodos unidos por conectores; si los conectores tienen tanto dirección como etiquetas, el grafo se denomina grafo etiquetado.

Como primer ejemplo de un autómata tenemos al semáforo.

### Comportamiento de un semáforo

![image](https://github.com/Chris-Vlad/MiRepositorio/assets/160756073/57ecde1c-01c2-4d7a-bca3-3186c6aeda27)

En esta primera parte podemos observar como sería el comportamiento de un semáforo común, teniendo 4 estados (contando q<sub>0</sub>), donde cada uno, dependiendo a cada condicional, cambiará a otro estado. Se puede observar los cambios en la siguiente tabla de transiciones.


| Estados | Condición  | Transición |
|---------|------------|------------|
| q<sub>0</sub> |   -   | q<sub>1</sub> |
| q<sub>1</sub> | m < 2 | q<sub>1</sub> |
| q<sub>1</sub> | m = 2 | q<sub>2</sub> |
| q<sub>2</sub> | m < 0.5 | q<sub>2</sub> |
| q<sub>2</sub> | m = 0.5 | q<sub>3</sub> |
| q<sub>3</sub> | m = 2 | q<sub>1</sub> |

En el ejemplo que investigué no existe como tal un estado de aceptación, sin embargo, dado que lo que uno busca es avanzar, q<sub>3</sub> es considerado el estado de aceptación (por mi).



Ahora bien, el anterior ejemplo está incompleto, ya que aún existen otros estados, muchos otros eventos en la vida real. Como lo es: ¿Qué sucede si alguna de las tres luces (tres estados) dura más de 2 minutos? Pues pasarían al estado de Rojo Suspendido (q<sub>4</sub>).

![image](https://github.com/Chris-Vlad/MiRepositorio/assets/160756073/f0b70b38-7131-47dc-a832-45ab915df06a)


(*Reitero, esto es un caso más real.*)

Si por alguna razón ocurriera esta anomalía, pasarían al estado "Rojo Suspendido" el cual sería arreglado por algún técnico, pero ahora sería enviado de vuelta al estado inicial, q<sub>0</sub>, quedando así la tabla de transición.

| Estados | Condición  | Transición |
|---------|------------|------------|
| q<sub>0</sub> |   -   | q<sub>1</sub> |
| q<sub>1</sub> | m < 2 | q<sub>1</sub> |
| q<sub>1</sub> | m = 2 | q<sub>2</sub> |
| q<sub>2</sub> | m < 0.5 | q<sub>2</sub> |
| q<sub>2</sub> | m = 0.5 | q<sub>3</sub> |
| q<sub>3</sub> | m = 2 | q<sub>1</sub> |
| q<sub>1</sub> | m > 2 | q<sub>4</sub> |
| q<sub>2</sub> | m > 2 | q<sub>4</sub> |
| q<sub>3</sub> | m > 2 | q<sub>4</sub> |
| q<sub>4</sub> | s = 1 | q<sub>0</sub> |

###

¿Eso ya es todo? Pues realmente no, aún existen más eventos, los cuales para no estar escribiendo y escribiendo solo anexaré los modelos.

#### Cuando llega la media noche cambia a Amarillo Suspendido, solo parpadea
![image](https://github.com/Chris-Vlad/MiRepositorio/assets/160756073/216c9b0a-c8f0-462b-a8f4-0875440b3368)

#### Cuando son las 05:00 pasa a q<sub>1</sub>. Inicia nuevo ciclo
![image](https://github.com/Chris-Vlad/MiRepositorio/assets/160756073/b447f0ca-cb8b-4dfa-b4f3-e6fc9f793868)

#### Cuando ocurre un apagón, y regresa la electricidad
![image](https://github.com/Chris-Vlad/MiRepositorio/assets/160756073/8cd9f7bd-e4d3-49eb-8fa3-c0a233efbb46)

### 

## Referencia
[YouTube](https://www.youtube.com/watch?v=zkSoBTjUBdU)

Ese sería mi ejemplo, algo engorroso, largo, y bastante diferente a los ejercicios vistos en clase. Pero muy real.
![image](https://github.com/Chris-Vlad/MiRepositorio/assets/160756073/ef900ff4-7edc-4f9a-a768-1c7589813f04)
