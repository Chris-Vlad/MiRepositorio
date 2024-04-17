# Expresiones regulares

## Password
Crea una expresión regular que valide un **Password "fuerte"** que cumpla los siguientes requerimientos *mínimos*.
1. 1 minúscula
2. 1 mayúscula
3. 1 numero
4. 1 carácter especial
5. 8 caracteres de longitud

Para esta validación usé la siguiente expresión regular
~~~
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@_ !-*?])[a-zA-Z\d@_!- *?]{8}$
~~~
Donde decimos que forzosamente tiene que iniciar con cualquiera de las cuatro condiciones:
. Inicie, o no con una minúscula
. Inicie, o no con una mayúscula
. Inicie, o no con un número
. Inicie, o no con un caracter especial

-

Con el símbolo '^' indicamos que inicia con esa expresión.
Con '?=.*' indicamos que si, forzosamente tiene que estar esa expresión, pero en toda la password, no necesariamente en el inicio de la misma.
El resto es sencillo.
1. Con 'a-z' indicamos que abarcará de la 'a' minúscula a la 'z' minúscula.
2. Con 'A-Z' indicamos que abarcará de la 'A' mayúscula a la 'Z' mayúscula.
3. Con '\d' indicamos que será un dígito. Esta expresión se refiere a que será cualquier dígito.
4. Con '@_ !-*?' indicamos que solo abarcará esos caracteres especiales. Porque así lo quise yo.

Puede entrar para comprobar que funcione dando click [aquí](https://regex101.com/r/jTs10z/).

-
-

## Usuario
Crea una expresión regular que valide un **Nombre de usuario** que cumpla los siguientes requerimientos.
1. Longitud de 3 a 16 caracteres
2. Letra o numero o guion medio o bajo

Para esta validación usé la siguiente expresión regular
~~~
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@|?!-]?)[a-zA-Z\d_@|?!-]{3,16}$
~~~
Donde decimos que forzosamente tiene que iniciar con cualquiera de las cuatro condiciones:
. Inicie, o no con una minúscula
. Inicie, o no con una mayúscula
. Inicie, o no con un número
. Inicie, o no con un caracter especial

-

La explicación es la misma que la anterior, solo que se agrega una cosa. El número y el caracter es opcional, por lo que, en este caso, no es necesario un número y caracter en el nombre de usuario.
(En el texto
1. Con 'a-z' indicamos que abarcará de la 'a' minúscula a la 'z' minúscula.
2. Con 'A-Z' indicamos que abarcará de la 'A' mayúscula a la 'Z' mayúscula.
3. Con '\d' indicamos que será un dígito. Esta expresión se refiere a que será cualquier dígito.
4. Con '@_ !-*?' indicamos que solo abarcará esos caracteres especiales. Porque así lo quise yo.

Puede entrar para comprobar que funcione dando click [aquí](https://regex101.com/r/XIVG5V/2).
