import math


class Point(object) :
    """A 2D point ADT using polar coordinates."""
    
    def __init__(self, x, y) :
        """Construct a point object from (x, y) coordinates.
        
        Parameters:
            x (float): x coordinate in a 2D cartesian grid.
            y (float): y coordinate in a 2D cartesian grid.
        """
        self._r = math.sqrt(x**2 + y**2)
        self._theta = math.atan2(y, x)

    def x(self) :
        """(float) Return the x coordinate of the point."""
        return self._r * math.cos(self._theta)

    def y(self) :
        """(float) Return the y coordinate of the point."""
        return self._r * math.sin(self._theta)

    def move(self, dx, dy) :
        """Move the point by (dx, dy).

        Parameters:
            dx (float): Amount to move in the x direction.
            dy (float): Amount to move in the y direction.
        """
        x = self.x() + dx
        y = self.y() + dy
        self._r = math.sqrt(x**2 + y**2)
        self._theta = math.atan2(y, x)

    def __str__(self) :
        """The 'informal' string representation of the point."""
        return '({0}, {1})'.format(self.x(), self.y())

    def __repr__(self) :
        """The 'official' string representation of the point."""
        return 'Point({0}, {1})'.format(self.x(), self.y())

    def __add__(self, other) :
        """Return a new Point after adding this point to 'other'.

        Perform vector addition of the points considered as vectors.
        point1 + point2 -> Point

        Parameters:
            other (Point): Other point to be added to this point.

        Return:
            Point: New point object at position of 'self' + 'other'.
        """
        x = self.x() + other.x()
        y = self.y() + other.y()
        return Point(math.sqrt(x**2 + y**2), math.atan2(y, x))

    def __eq__(self, other) :
        """Return True iff 'self' and 'other' have the same x and y coords.

        point1 == point2 -> bool
        
        Parameters:
            other (Point): Other point to be compared to this point.

        Return:
            bool: True if 'self' and 'other' have the same x and y coords.
                  False otherwise.
        """
        return self._r == other.r() and self._theta == other.theta()

    def r(self) :
        """(float) Return the distance of the point from the centre of the
        coordinate system (0, 0).
        """
        return self._r

    def theta(self) :
        """(float) Return the angle, in radians, from the x-axis of the point."""
        return self._theta
