import math


class Point(object) :
    """A 2D point ADT using cartesian coordinates."""
    
    def __init__(self, x, y) :
        """Construct a point object based on (x, y) coordinates.
        
        Parameters:
            x (float): x coordinate in a 2D cartesian grid.
            y (float): y coordinate in a 2D cartesian grid.
        """
        self._x = x
        self._y = y

    def x(self) :
        """(float) Return the x coordinate of the point."""
        return self._x

    def y(self) :
        """(float) Return the y coordinate of the point."""
        return self._y

    def move(self, dx, dy) :
        """Move the point by (dx, dy).

        Parameters:
            dx (float): Amount to move in the x direction.
            dy (float): Amount to move in the y direction.
        """
        self._x += dx
        self._y += dy


if __name__ == "__main__" :
	"""Example usage of a Point object."""
    p = Point(2, -5)
    print(p.x(), p.y())
    p.move(-3, 9)
    print(p.x(), p.y())
