"""1.	Determinar todos los clientes que viven en 'TOLEDO'"""
vive_en(ciudad : CADENA ; clientes : TABLA[CLIENTE]) : ENTERO
    # El índice del primer cliente que vive en `ciudad' o AUSENTE.

Precondición
    ciudad ≠ NULO
    clientes ≠ NULO

constante
    I_MIN : ENTERO ← índice_min(clientes)
    I_MAX : ENTERO ← índice_max(clientes)

variable
    i : ENTERO # Índice del siguiente cliente que vive en `ciudad'

inicialización
    i ← I_MIN
    Resultado ← AUSENTE

realización
    si i = I_MAX
        entonces
            Resultado ← AUSENTE    
    sino si clientes[0].p.dirección.ciudad = ciudad
        entonces
            Resultado ← i
    sino
        entonces
            vive_en(ciudad, clientes [1:], i+1)
    fin si

postcondición
        Resultado = AUSENTE 
    o si no
        (
          # El cliente existe
            clientes[Resultado].número ≠ VACIO
          y entonces
            clientes[Resultado].número ≠ BORRADO
          y entonces
          # Él vive en `ciudad'
            clientes[Resultado].p.dirección.ciudad = ciudad
          y entonces
          # Es el primero de la tabla `clientes'
            (∀k ∈ ℤ)(índice_min(clientes) ≤ k < Resultado =>
                     clientes[k].p.dirección.ciudad ≠ ciudad)
        )

fin vive_en
