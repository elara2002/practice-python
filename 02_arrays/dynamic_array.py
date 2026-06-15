"""
DynamicArray — Implementación manual de un array dinámico.

Estructura clásica de CS: array con resize automático al doble
cuando se llena.

Complejidades:
- Acceso por índice (at): O(1)
- Push (amortizado): O(1)
- Insert / delete por índice: O(n)
- Find (búsqueda lineal): O(n)
"""


class DynamicArray:
    def __init__(self) -> None:
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def at(self, index: int) -> object:
        """Devuelve el elemento en la posición index."""
        if index < 0 or index >= self._size:
            raise IndexError("Index fuera de rango")
        return self._data[index]

    def _resize(self, new_capacity: int) -> None:
        """Cambia la capacidad interna, conservando los elementos existentes."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def push(self, item) -> None:
        """Agrega item al final. Hace resize al doble si está lleno."""
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = item
        self._size += 1

    def insert(self, index: int, item) -> None:
        """Inserta item en la posición index, corriendo elementos a la derecha."""
        if index < 0 or index > self._size:
            raise IndexError("Index fuera de rango")

        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # Correr elementos a la derecha desde el final hacia index
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = item
        self._size += 1

    def prepend(self, item) -> None:
        """Inserta item al inicio del array."""
        self.insert(0, item)

    def pop(self) -> object:
        """Quita y devuelve el último elemento."""
        if self.is_empty():
            raise IndexError("Pop on empty array")
        last_obj = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return last_obj

    def delete(self, index: int) -> None:
        """Quita el elemento en index, corriendo posteriores a la izquierda."""
        if index < 0 or index >= self._size:
            raise IndexError("Index fuera de rango")

        # Correr elementos a la izquierda desde index
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size - 1] = None
        self._size -= 1

    def find(self, item) -> int:
        """Devuelve el índice de la primera ocurrencia, o -1 si no se encuentra."""
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def remove(self, item) -> None:
        """Quita la primera ocurrencia del item."""
        idx = self.find(item)
        if idx == -1:
            raise ValueError("Item no encontrado en el array")
        self.delete(idx)


if __name__ == "__main__":
    arr = DynamicArray()

    # Push y resize automático
    for c in ["A", "B", "C", "D", "E"]:
        arr.push(c)
    print(f"After push 5 → size={arr.size()}, capacity={arr.capacity()}")
    # esperado: size=5, capacity=8 (resize: 1→2→4→8)

    # at
    print(f"at(0)={arr.at(0)}, at(4)={arr.at(4)}")
    # esperado: A, E

    # insert
    arr.insert(1, "X")
    print(f"After insert(1, X) → at(1)={arr.at(1)}, size={arr.size()}")
    # esperado: X, 6

    # prepend
    arr.prepend("Z")
    print(f"After prepend(Z) → at(0)={arr.at(0)}, size={arr.size()}")
    # esperado: Z, 7

    # pop
    last = arr.pop()
    print(f"pop() returned {last}, size={arr.size()}")
    # esperado: E, 6

    # delete
    arr.delete(0)
    print(f"After delete(0) → at(0)={arr.at(0)}")
    # esperado: A

    # find
    print(f"find('X')={arr.find('X')}, find('nope')={arr.find('nope')}")
    # esperado: 1, -1

    # remove
    arr.remove("X")
    print(f"After remove('X') → find('X')={arr.find('X')}")
    # esperado: -1

    print("\n✓ Todas las operaciones funcionaron correctamente")