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



class DeluxeTV(TV) :
    """Representation of a Deluxe TV where the channel can be set
       without using up and down.
    """
    
    def set_channel(self, channel) :
        """Sets the TV channel to the indicated 'channel' if the TV is on.
           If 'channel' is invalid an error message is output.
        """
        if self._power :
            if 1 < channel < MAX_CHANNEL :
                self._channel = channel
            else :
                print("{0} is not a valid channel".format(channel))



class SuperDeluxeTV(DeluxeTV) :
    """Representation of a Super Delux TV where channels can be saved
       to favourites. Channel up and down goes through the favourites.
    """

    def __init__(self) :
        super().__init__()
        self._favourites = []          # All favourite TV channels.

    def store(self) :
        """Stores the current channel as one of the favourites."""
        if self._channel not in self._favourites and self._power :
            self._favourites.append(self._channel)
            self._favourites.sort()

    def remove(self) :
        """Removes the current channel so that it is no longer a favourite."""
        if self._power :
            if self._channel in self._favourites :
                self._favourites.remove(self._channel)
            else :
                print("{0} is not in favourites".format(self._channel))

    def channel_up(self) :
        """Moves to the next higher favourite channel.

           It does not matter if the current channel is a favourite or not.
           Channel will wrap around to 1 if it passes MAX_CHANNEL while
           searching for the next higher favourite channel.
        """
        if self._power :
            if not self._favourites :
                print("No favourites stored")
            else :
                while True :
                    self._channel += 1
                    if self._channel > MAX_CHANNEL :
                        self._channel = 1
                    if self._channel in self._favourites :
                        break

    def channel_down(self) :
        """Moves to the previous (lower) favourite channel.

           It does not matter if the current channel is a favourite or not.
           Channel will wrap around to MAX_CHANNEL if it passes 1 while
           searching for the previous favourite channel.
        """
        if self._power :
            if not self._favourites :
                print("No favourites stored")
            else :
                while True :
                    self._channel -= 1
                    if self._channel < 1 :
                        self._channel = 100
                    if self._channel in self._favourites :
                        break

    def __str__(self) :
        if self._power :
            return "I'm a Super Deluxe TV on channel {0}".format(self._channel)
        else :
            return "I'm a Super Deluxe TV that is turned off"
