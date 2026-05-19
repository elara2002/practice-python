# Complejidad: O(n)
def funcion_a(arr: list) -> int:
    total = 0
    for n in arr:
        total += n
    return total
   
# Complejidad: O(n^2)
def funcion_b(arr: list) -> list:
    result = []
    for n in arr:
        for m in arr:
            result.append(n * m)
    return result
   
# Complejidad: O(n)
def funcion_c(arr: list, target: int) -> bool:
    return target in arr

# O(1) espacio - solo variables fijas
def suma(arr: list) -> int:
    total = 0
    for x in arr:
        total += x
    return total

# O(n) espacio - creas una lista nueva de tamaño n
def duplica(arr: list) -> list:
    result = []
    for x in arr:
        result.append(x * 2)
    return result

# O(n²) espacio - tu funcion_b de antes
def producto_cartesiano(arr: list) -> list:
    result = []
    for n in arr:
        for m in arr:
            result.append(n * m)
    return result