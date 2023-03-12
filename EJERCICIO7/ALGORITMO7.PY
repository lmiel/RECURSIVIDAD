"""Si el conjunto de fichas está vacío o solo tiene un color, ya está ordenado.
Si hay dos colores diferentes, se intercambian las fichas del primer color con las del segundo color. Esto se puede hacer de forma recursiva con el subconjunto de fichas de cada color.
Si hay tres colores diferentes, se intercambian las fichas del primer color con las del segundo color. Luego, se intercambian las fichas del segundo color con las del tercer color. Esto se puede hacer de forma recursiva con los subconjuntos de fichas de cada color.
Si hay más de tres colores diferentes, se aplica el algoritmo de forma recursiva a los subconjuntos de fichas de cada color hasta que solo hay dos o tres colores diferentes.
Una vez que todas las fichas de cada color están juntas, se concatenan los subconjuntos de fichas de cada color en el orden R-V-B (rojo, verde, azul)."""

Entrada:
    n : ENTERO
    fichas : TABLA[CARACTER]
    
