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

    def __str__(self) :
        """The 'informal' string representation of the point."""
        return '({0}, {1})'.format(self._x, self._y)

    def __repr__(self) :
        """The 'official' string representation of the point."""
        return 'Point({0}, {1})'.format(self._x, self._y)
