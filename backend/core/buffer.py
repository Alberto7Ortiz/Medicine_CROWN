from collections import deque


class Buffer:
    """
    Buffer circular de tamaño fijo.

    Cuando alcanza el límite,
    elimina automáticamente el dato más antiguo.
    """

    def __init__(self, max_size):
        if max_size <= 0:
            raise ValueError("El tamaño del buffer debe ser mayor que cero")

        self.max_size = max_size
        self._buffer = deque(maxlen=max_size)


    # ==================================
    # INSERTAR DATO
    # ==================================

    def push(self, item):
        """
        Agrega un elemento al buffer.
        Si está lleno, elimina el más antiguo.
        """

        self._buffer.append(item)


    # ==================================
    # OBTENER ULTIMO DATO
    # ==================================

    def get_last(self):
        """
        Retorna el último elemento almacenado.
        """

        if self.is_empty():
            return None

        return self._buffer[-1]


    # ==================================
    # OBTENER TODO EL BUFFER
    # ==================================

    def get_all(self):
        """
        Retorna todos los elementos almacenados.
        """

        return list(self._buffer)


    # ==================================
    # LIMPIAR BUFFER
    # ==================================

    def clear(self):
        """
        Elimina todos los elementos.
        """

        self._buffer.clear()


    # ==================================
    # INFORMACION
    # ==================================

    def size(self):
        """
        Cantidad actual de elementos.
        """

        return len(self._buffer)


    def is_empty(self):
        """
        Verifica si está vacío.
        """

        return len(self._buffer) == 0


    def is_full(self):
        """
        Verifica si llegó al límite.
        """

        return len(self._buffer) == self.max_size