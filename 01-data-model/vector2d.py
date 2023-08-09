import math

class Vector:
    """
    Represents a 2D vector.

    Attributes:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Initializes a Vector instance.

        Args:
            x (float, optional): The x-coordinate of the vector. Defaults to 0.
            y (float, optional): The y-coordinate of the vector. Defaults to 0.
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        Returns a string representation of the vector.

        Returns:
            str: The string representation of the vector.
        """
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self) -> float:
        """
        Computes the magnitude (absolute value) of the vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        """
        Checks if the vector is nonzero.

        Returns:
            bool: True if the vector is nonzero, False otherwise.
        """
        return bool(abs(self))

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Adds two vectors element-wise.

        Args:
            other (Vector): The vector to be added.

        Returns:
            Vector: The resulting vector.
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> 'Vector':
        """
        Multiplies the vector by a scalar.

        Args:
            scalar (float): The scalar multiplier.

        Returns:
            Vector: The scaled vector.
        """
        return Vector(self.x * scalar, self.y * scalar)