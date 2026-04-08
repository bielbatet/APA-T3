"""
Tercera tarea de APA: Multiplicación de vectores y ortogonalidad

Nombre y apellidos: Biel Batet Tudela

Tests unitarios
===============

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4, 10, 18])
>>> 2 * v1
Vector([2, 4, 6])
>>> v1 @ v2
32

>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
>>> v1 // v2 + v1 % v2
Vector([2.0, 1.0, 2.0])
"""

import doctest


class Vector:
    """
    Classe que representa un vector numèric.
    Permet operacions bàsiques entre vectors i amb escalars.
    """

    def __init__(self, elements):
        """
        Inicialitza el vector a partir d'una col·lecció d'elements.

        Args:
            elements: iterable amb les components del vector.
        """
        self.valors = list(elements)

    def __repr__(self):
        """
        Retorna la representació oficial del vector.

        Returns:
            str
        """
        return f"Vector({self.valors})"

    def __eq__(self, altre):
        """
        Compara dos vectors.

        Returns:
            bool
        """
        return isinstance(altre, Vector) and self.valors == altre.valors

    def __len__(self):
        """
        Retorna el nombre de components del vector.
        """
        return len(self.valors)

    def __add__(self, altre):
        """
        Suma dos vectors component a component.
        """
        return Vector([x + y for x, y in zip(self.valors, altre.valors)])

    def __sub__(self, altre):
        """
        Resta dos vectors component a component.
        """
        return Vector([x - y for x, y in zip(self.valors, altre.valors)])

    def __mul__(self, altre):
        """
        Multiplica el vector per un escalar o aplica
        el producte de Hadamard entre dos vectors.
        """
        if isinstance(altre, (int, float)):
            return Vector([x * altre for x in self.valors])

        if isinstance(altre, Vector):
            return Vector([x * y for x, y in zip(self.valors, altre.valors)])

        raise TypeError("Operació no suportada")

    def __rmul__(self, altre):
        """
        Permet la multiplicació escalar per l'esquerra.
        """
        return self.__mul__(altre)

    def __matmul__(self, altre):
        """
        Calcula el producte escalar entre dos vectors.
        """
        return sum(x * y for x, y in zip(self.valors, altre.valors))

    def __floordiv__(self, altre):
        """
        Calcula la component paral·lela d'un vector respecte a un altre.
        """
        coeficient = (self @ altre) / (altre @ altre)
        return coeficient * altre

    def __mod__(self, altre):
        """
        Calcula la component perpendicular d'un vector respecte a un altre.
        """
        component_paralela = self // altre
        return self - component_paralela


if __name__ == "__main__":
    doctest.testmod(verbose=True)