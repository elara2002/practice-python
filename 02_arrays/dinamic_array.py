class DynamicArray:
    def __init__(self) -> None:
        self._capacity = 1
        self._size = 0
        self._data = [None] * self._capacity

    def size(self) -> int:
        # cuántos elementos hay
        return self._size

    def capacity(self) -> int:
        # cuánto espacio reservado hay
        return self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def at(self, index: int) -> object:
        if index < 0 or index >= self._size:
            raise IndexError("Index fuera de rango")
        return self._data[index]

    def _resize(self, new_capacity: int) -> None:
        new_data = [None] * new_capacity
        i = 0
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity


    def push(self, item: object) -> None:
        # 1. Verifico que esta lleno, si esta lleno llamo a _resize
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # 2. Meto el item en el cajón disponible
        self._data[self._size] = item

        # 3. Aumento el size en 1
        self._size += 1
       

    def insert(self, index: int, item: object) -> None:
        #Valido el index
        if 0 <= index <= self._size:
            # 1. Valido si esta lleno el array
            if self._size == self._capacity:
                self._resize(2 * self._capacity)
            # 2. Correr los elementos a la derecha
            for i in range(self._size, index, -1):
                self._data[i] = self._data[i - 1]
            self._data[index] = item #reemplazo el dato
            # 3. Aumentar el size
            self._size +=1
        else:
            raise IndexError("Index fuera de rango")
        
    
    def prepend(self, item: object) -> None:
        # insertar al inicio (pista: reusa insert)
        self.insert(0,item)

    def pop(self) -> object:
        # quitar y devolver el último
        if self.is_empty(): # validar que no este vacio el arreglo
            raise IndexError("Index fuera de rango, pop en arreglo vacio")
        last_obj = self._data[self._size - 1] # Guardar la ultima posición
        self._data[self._size - 1] = None # limpiar la posición, buena practica
        self._size -= 1  #decremento del size del arreglo

        return last_obj


    def delete(self, index: int) -> None:
        # borrar en index, recorriendo los demás a la izquierda
        #Valido el index
        if not (0 <= index < self._size):
            raise IndexError("Index fuera de rango, no es posible eliminarlo")
        # Correr elementos de izquierda a derecha
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]

        self._data[self._size - 1] = None

        self._size -=1

    def find(self, item: object) -> int:
        # devolver el índice de la primera ocurrencia, o -1 si no está
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1
      
    def remove(self, item: object) -> None:
        # borrar la primera ocurrencia del valor
        idx = self.find(item)
        if idx != -1:
            self.delete(idx)
            return 
        raise ValueError("El item no se encontro,")

if __name__ == "__main__":
    print("=" * 50)
    print("Test DynamicArray")
    print("=" * 50)

    arr = DynamicArray()
    print(f"\nInicial: size={arr.size()}, capacity={arr.capacity()}, vacío={arr.is_empty()}")

    # --- push y crecimiento (resize automático) ---
    print("\n--- push y resize ---")
    arr.push("A")
    print(f"push A → size={arr.size()}, capacity={arr.capacity()}")
    arr.push("B")
    print(f"push B → size={arr.size()}, capacity={arr.capacity()}  (esperado: capacity=2)")
    arr.push("C")
    print(f"push C → size={arr.size()}, capacity={arr.capacity()}  (esperado: capacity=4, hubo resize)")
    arr.push("D")
    print(f"push D → size={arr.size()}, capacity={arr.capacity()}")

    # --- at ---
    print("\n--- at ---")
    for i in range(arr.size()):
        print(f"  arr.at({i}) = {arr.at(i)}")

    # --- insert ---
    print("\n--- insert(1, 'X') ---")
    arr.insert(1, "X")
    print("  Esperado: A, X, B, C, D")
    print("  Actual:   ", end="")
    for i in range(arr.size()):
        print(arr.at(i), end=", ")
    print(f"\n  size={arr.size()}, capacity={arr.capacity()}")

    # --- prepend ---
    print("\n--- prepend('Z') ---")
    arr.prepend("Z")
    print(f"  Primer elemento: {arr.at(0)}  (esperado: Z)")

    # --- pop ---
    print("\n--- pop() ---")
    ultimo = arr.pop()
    print(f"  Devolvió: {ultimo}  (esperado: D)")
    print(f"  size={arr.size()}")

    # --- delete ---
    print("\n--- delete(0) ---")
    arr.delete(0)
    print(f"  Primer elemento: {arr.at(0)}  (esperado: A)")

    # --- find ---
    print("\n--- find ---")
    print(f"  find('X') = {arr.find('X')}  (esperado: 1)")
    print(f"  find('inexistente') = {arr.find('inexistente')}  (esperado: -1)")

    # --- remove ---
    print("\n--- remove('X') ---")
    arr.remove("X")
    print(f"  find('X') después = {arr.find('X')}  (esperado: -1)")

    # --- Errores esperados ---
    print("\n--- Errores esperados ---")
    try:
        arr.at(99)
    except IndexError as e:
        print(f"  IndexError capturado: {e}  ✓")

    try:
        arr.remove("no existe")
    except ValueError as e:
        print(f"  ValueError capturado: {e}  ✓")

    print("\nSi cada 'actual' coincidió con su 'esperado', todo funciona.")