"""
CONVERTIMOS TODO A CARACTERES ALFANUMERICOS
QUITAMOS ACENTOS SUSTITUYENDO POR SU EQUIVALENTE SIN ACENTO
TODAS LAS LETRAS A MAYUSCULAS
SABER SI ES PALINDROMO (IGUAL DE IZQUIERDA A DERECHA QUE DE DERECHA A IZQUIERDA)
DE MANERA RECURSIVA

comparamos los elementos de los dos extremos de la cadena, si son iguales seguimos la recursion y quitamos la primera y la ultima letra
caso base es cuando la cadena es de longitud 1 o 0
otro caso base es cuando los extremos no son iguales

como se hacia el slicing, cuando escribes -1 te da la ultima letra, -2 la penultima, etc
para comparar el primer y ultimo elemento se compara cadena[0] con cadena[-1]"""

palindromo(cadena : CADENA) : BOOLEANO

Precondición
    cadena ≠ NULO

inicialización
    Resultado ← VERDADERO
    cadena ← cadena caracteres alfanumericos
    cadena ← cadena sin acentos
    cadena ← cadena en mayusculas

realización
    si longitud(cadena) = 0 o longitud(cadena) = 1
        entonces
            Resultado ← VERDADERO
    sino si cadena[0] = cadena[-1]
        entonces
            palindromo(cadena[1:-1])
    sino
        entonces
            Resultado ← FALSO

postcondición
    Resultado = VERDADERO o Resultado = FALSO

fin palindromo
