# atbash
Programa sencillo para codificar texto con el sistema Atbash implementado en Python v3.0

Si bien es un cifrado sencillo de implementar, no tiene ninguna seguridad frente al análisis por frecuencia o cualquier otra técnica criptográfica moderna y no permite el uso de números, por lo que la aplicación práctica en la actualidad-recordemos que tiene una historia milenaria-es apenas como curiosidad o ejercicio de programación.

En esta versión particular se debe introducir la frase a encriptar eliminando los espacios, y en minúsculas. 

The Atbash cipher is a monoalphabetic substitution cipher, where the first letter of alphabet (A) is assigned to the last (Z). Following that procedure we can build a chart: a = z, b = y, and so on. After that, we take every character of the message and replace with the corresponding letter according to chart. Example: ATTACK would be encripted as ZGGZXP.
