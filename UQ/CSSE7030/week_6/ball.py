import math


# global constants for testing
# note - our 'y' axis is upside down to what we would normally
# expect in calculus - this is because our intention is
# to be able to draw the ball in a graphics window and
# this is consistent with the axes in a graphics window.
TOP = 0.0
LEFT = 0.0
BOTTOM = 2.0
RIGHT = 4.0
TIMESTEP = 0.1


class Ball(object) :
    """A class for simulating the movement of a ball on a billiard table.
    
    Class Invariant:
        0 <= _direction <= 2*pi
        and
        LEFT + radius <= _x <= RIGHT - radius
        and
        TOP + radius <= _y <= BOTTOM - radius
        and
        0 <= _speed
    """
    
    radius = 0.1
    
    def __init__(self, x, y, speed, direction) :
        """Initialise a ball object with position, speed and direction.

        Parameters:
            x (float): x coordinate starting position of Ball.
            y (float): y coordinate starting position of Ball.
            speed (float): Speed at which Ball is moving.
            direction (float): Direction in which Ball is moving.

        Preconditions:
            The supplied values satisfy the class invariant.
        """
        self._x = x
        self._y = y
        self._speed = speed
        self._direction = direction

    def get_centre_x(self) :
        """(float) Return the x coordinate of the Ball's centre."""     
        return self._x

    def get_centre_y(self) :
        """(float) Return the y coordinate of the Ball's centre."""
        return self._y

    def get_speed(self) :
        """(float) Return the speed of the Ball."""
        return self._speed

    def get_dir(self) :
        """(float) Return the direction in which the ball is travelling."""
        return self._direction

    def __repr__(self) :
        """Ball's string representation."""
        return 'Ball({0:.2f}, {1:.2f}, {2:.2f}, {3:.2f})'.format( 
                self._x, self._y, self._speed, self._direction)

    def _reflect_vertically(self) :
        """Change the direction as the ball bounces off a vertical edge."""
        self._direction = math.pi - self._direction
        if self._direction < 0 :
            self._direction += 2 * math.pi

    def _reflect_horizontally(self) :
        """Change the direction as the ball bounces off a horizontal edge."""
        self._direction = 2 * math.pi - self._direction
   

    def step(self) :
        """Advance time by TIMESTEP - moving the ball."""

        self._x += TIMESTEP * self._speed * math.cos(self._direction)
        self._y += TIMESTEP * self._speed * math.sin(self._direction)
        if self._x < LEFT + self.radius :
            self._x = 2 * (LEFT + self.radius) - self._x
            self._reflect_vertically()
        elif self._x > RIGHT - self.radius :
            self._x = 2 * (RIGHT - self.radius) - self._x
            self._reflect_vertically()
        
        if self._y  < TOP + self.radius :
            self._y = 2 * (TOP + self.radius) - self._y
            self._reflect_horizontally()
        elif self._y > BOTTOM - self.radius :
            self._y = 2 * (BOTTOM - self.radius) - self._y
            self._reflect_horizontally()


    def touching(self, other) :
        """(bool) Return True iff this Ball is touching other."""
        return (((self._x - other.get_centre_x()) ** 2
                 + (self._y - other.get_centre_y()) ** 2)
               <= (2 * self.radius) ** 2)
