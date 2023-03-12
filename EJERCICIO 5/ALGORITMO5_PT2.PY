"""2.	Promoción para los clientes del 45 con edades de 40 a 50 años"""

buscar_provincia(provincia : CADENA ; edad_min : ENTERO; edad_max : ENTERO; clientes : TABLA[CLIENTE]) : ENTERO

Precondición
    clientes ≠ NULO
    cp ≠ NULO
    edad_min ≠ NULO
    edad_max ≠ NULO
    edad_min ≤ edad_max

constante
    I_MIN : ENTERO ← índice_min(clientes)
    I_MAX : ENTERO ← índice_max(clientes)

variable
    i : ENTERO

inicialización
    i ← I_MIN
    Resultado ← AUSENTE

realización
    si i = I_MAX
        entonces
            Resultado ← AUSENTE    
    sino si clientes[0].p.dirección.código_postal.provincia = provincia y clientes[0].p.edad >= edad_min y clientes[0].p.edad <= edad_max
        entonces
            Resultado ← i
    sino
        entonces
            buscar_provincia(provincia, edad_min, edad_max, clientes [1:], i+1)
    fin si

postcondición
        Resultado = AUSENTE 
    o si no
        (
            clientes[Resultado].número ≠ VACIO
          y entonces
            clientes[Resultado].número ≠ BORRADO
          y entonces
            clientes[Resultado].p.dirección.código_postal.provincia = provincia 
            y clientes[Resultado].p.edad >= edad_min 
            y clientes[Resultado].p.edad <= edad_max
          y entonces
            (∀k ∈ ℤ)(índice_min(clientes) ≤ k < Resultado =>
                clientes[Resultado].p.dirección.código_postal.provincia ≠ provincia 
                y clientes[Resultado].p.edad < edad_min 
                y clientes[Resultado].p.edad > edad_max)
        )

fin buscar_provincia
