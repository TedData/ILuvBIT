MAX_CHANNEL = 100


class TV(object) :
    """Representation of a simple television."""

    def __init__(self) :
        self._channel = 1
        self._power = False

    def turn_on(self) :
        """Turns the TV on."""
        self._power = True

    def turn_off(self) :
        """Turns the TV off."""
        self._power = False

    def channel_up(self) :
        """Changes the channel up by 1.
           If the channel goes above 100 then loops back to 1.
        """
        if self._power :
            self._channel += 1
            if self._channel > MAX_CHANNEL :
                self._channel = 1

    def channel_down(self) :
        """Changes the channel down by 1.
           If the channel goes below 1 then loops back to 100.
        """
        if self._power :            
            self._channel -= 1
            if self._channel < 1 :
                self._channel = MAX_CHANNEL

    def __str__(self) :
        if self._power :
            return "I'm a TV on channel {0}".format(self._channel)
        else :
            return "I'm a TV that is turned off"
