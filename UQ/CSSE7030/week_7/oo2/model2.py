import random

SQ_CLOSE = 1600
STEP_DELTA = 10


def close_to(p1, p2):
    """
    Returns True iff p1 is close to p2, where p1 & p2 are both (x, y) pairs.

    close_to((int, int), (int, int)) -> bool
    """
    x1, y1 = p1
    x2, y2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 < SQ_CLOSE


def get_delta(x1, x2):
    """
    Returns the step size (delta) to move if x1 and x2 are far away enough,
    else 0 if they are too close.

    get_delta(int, int) -> int
    """
    if x1 > x2 + STEP_DELTA:
        return STEP_DELTA
    elif x1 < x2 - STEP_DELTA:
        return -STEP_DELTA
    else:
        return 0


class GameObject(object):
    """
    A basic object for the game.
    """

    def __init__(self, x, y, name):
        """
        Constructor

        GameObject.__init__(GameObject, int, int, str)
        """

        self._x = x
        self._y = y
        self._name = name

    def get_position(self):
        """
        Returns the (x, y) position pair of the game object.

        GameObject.get_position(GameObject) -> (int, int)
        """

        return (self._x, self._y)

    def get_name(self):
        """
        Returns the name of the game object.

        GameObject.get_name(GameObject) -> str
        """

        return self._name


class Character(GameObject):
    """
    A character in the game.
    """

    def __init__(self, x, y, name):
        """
        Constructor

        Character.__init__(Character, int, int, str)
        """

        super().__init__(x, y, name)
        self._health = 100
        self._armour = 100

    def move(self, deltax, deltay):
        """
        Moves the character by given change in x & y.        

        Character.move(Character, int, int) -> None
        """

        self._x += deltax
        self._y += deltay

    def get_health(self):
        """
        Returns the character's health.

        Character.get_health(Character) -> int
        """

        return self._health

    def get_armour(self):
        """
        Returns the character's armour.

        Character.get_armour(Character) -> int
        """

        return self._armour

    def update_health(self, delta):
        """
        Changes the character's health by delta, but cannot go below zero.
        (Positive delta results in an increase).

        Character.update_health(Character, int) -> int
        """

        self._health += delta
        if self._health < 0:
            self._health = 0

    def update_armour(self, delta):
        """
        Changes the character's armour by delta, but cannot go below zero.
        (Positive delta results in an increase).

        Character.update_armour(Character, int) -> int
        """
        self._armour += delta
        if self._armour < 0:
            self._armour = 0


class Player(Character):
    """
    A player in the game.
    """

    def __init__(self, x, y, name):
        """
        Constructor

        Player.__init__(Player, int, int, str)
        """

        super().__init__(x, y, name)
        self._inventory = []
        self._holding = None

    def get_inventory(self):
        """
        Returns the inventory items the player has.

        Player.get_inventory(Player) -> [Item]
        """

        return self._inventory

    def take(self, item):
        """
        Adds an item to the player's inventory.

        Player.take(Player, Item) -> None
        """

        self._inventory.append(item)

    def drop(self, index):
        """
        Removes the item at given index from the player's inventory.
        Does nothing if index is out of valid range.

        Player.drop(Player, int) -> None
        """

        if 0 <= index <= len(self.get_inventory()) - 1:
            item = self._inventory.pop(index)
            if item == self._holding:
                self._holding = None
            item.set_taken(False)
            item.set_position(self._x, self._y)

    def hold(self, index):
        """
        Makes the player hold the item at given index from their inventory.
        Does nothing if index is out of valid range.

        Player.hold(Player, int) -> None
        """

        if 0 <= index <= len(self.get_inventory()) - 1:
            item = self._inventory[index]
            if item in self._inventory:
                self._holding = item

    def get_holding(self):
        """
        Returns the item that the player is currently holding, else None.

        Player.get_holding(Player) -> Item
        """

        return self._holding

    def use(self):
        """
        Uses the item that the player is currently holding.
        Does nothing if the player is not holding anything.

        Player.use(Player) -> None
        """

        if self._holding is not None:
            self._holding.use(self)


class Monster(Player):
    """
    A monster in the game that stays stationary.
    """

    def __init__(self, x, y, name, model):
        """
        Constructs a monster, with reference to the game world (Model).

        Monster.__init__(Monster, int, int, str, Model)
        """

        super().__init__(x, y, name)
        self._model = model

    def attack(self):
        """
        Makes the monster attack the player that is close to itself.

        Monster.attack(Monster) -> None
        """

        if close_to(self.get_position(),
                    self._model.get_player().get_position()):
            self._model.get_player().update_health(-5)
            self._model.get_player().update_armour(-5)

    def step(self):
        """
        Performs the action for the next timestep for the monster:

            Attacks.

        Monster.step(Monster) -> None
        """

        self.attack()


class TrackingMonster(Monster):
    """
    A monster in the game that tracks the player directly.
    """

    def step(self):
        """
        Performs the action for the next timestep for the monster.

            Attacks, and moves toward the player.

        TrackingMonster.attack(TrackingMonster) -> None
        """

        self.attack()
        px, py = self._model.get_player().get_position()
        x, y = self.get_position()
        self.move(get_delta(px, x), get_delta(py, y))


class RandomTrackingMonster(Monster):
    """
    A monster in the game that tracks the player somewhat randomly.
    """

    def step(self):
        """
        Performs the action for the next timestep for the random monster.

            Attacks, and moves toward the player with a somewhat random offset.

        TrackingMonster.attack(TrackingMonster) -> None
        """

        self.attack()
        px, py = self._model.get_player().get_position()
        x, y = self.get_position()
        dx = get_delta(px, x) // 4
        dy = get_delta(py, y) // 4
        dx = random.normalvariate(dx, 4)
        dy = random.normalvariate(dy, 4)
        self.move(dx, dy)


class Item(GameObject):
    """
    An item in the game.
    """

    def __init__(self, x, y, name):
        """
        Constructor

        Item.__init__(Item)
        """

        super().__init__(x, y, name)
        self._taken = False


    def set_position(self, x, y):
        """
        Sets the xy-position of the item.

        Item.set_position(Item, int, int) -> None
        """

        self._x = x
        self._y = y


    def is_taken(self):
        """
        Returns True iff the item has been taken.

        Item.is_taken(Item) -> bool
        """

        return self._taken


    def set_taken(self, taken=True):
        """
        Sets whether the item has been taken. Defaults to True.

        Item.set_taken(Item, taken=bool)
        """

        self._taken = taken


    def use(self):
        """
        Uses the item.
        Abstract method that must be implemented by child classes.

        Item.use(Item) -> None
        """

        raise NotImplemented("Item.use must be implemented by the child class.")


    def __str__(self):
        """
        Returns the string representation of this item.

        Item.__str__(Item) -> str
        """

        return self._name


class Potion(Item):
    """
    An item in the game that heals the character once.
    """

    def __init__(self, x, y, name, health):
        """
        Constructor

        Potion.__init__(Potion, int, int, str, int)
        """

        super().__init__(x, y, name)
        self._health = health

    def use(self, char):
        """
        If not already used, heals the character.

        Potion.use(Potion, Character) -> None
        """

        char.update_health(self._health)
        self._health = 0


class Weapon(Item):
    """
    An offensive weapon in the game that can inflict damage.
    """

    def __init__(self, x, y, name, health_damage, armour_damage, model):
        """
        Constructs a weapon with knowledge of the game world (Model)

        Weapon.__init__(Weapon, int, int, str, int, int, Model)
        """

        super().__init__(x, y, name)
        self._health_damage = health_damage
        self._armour_damage = armour_damage
        self._model = model


    def use(self, char1):
        """
        Uses the weapon to attack the first nearby character.

        Weapon.use(Weapon, Character) -> None
        """

        if self == char1.get_holding():
            for char2 in self._model.get_monsters():
                if close_to(char1.get_position(), char2.get_position()):
                    char2.update_health(-self._health_damage)
                    char2.update_armour(-self._armour_damage)
                    return


class Model(object):
    """
    A model of the game world.
    """

    def __init__(self):
        """
        Constructor

        Model.__init__()
        """

        self._player = Player(50, 50, "player")
        self._monsters = [Monster(600, 50, "balloon", self),
                         TrackingMonster(50, 400, "purple", self),
                         RandomTrackingMonster(200, 300, "triangle", self)]
        self._items = [Weapon(400, 50, "sword", 10, 10, self),
                      Potion(50, 400, "potion", 40),
                      Weapon(600, 400, "dagger", 2, 2, self)]


    def get_player(self):
        """
        Returns the player.

        Model.get_player(Model) -> Player
        """

        return self._player

    def get_items(self):
        """

        Returns the items that exist in the game.        

        Model.get_items(Model) -> [Items]
        """

        return self._items

    def get_monsters(self):
        """
        Returns the monsters that exist in the game.

        Model.get_monsters(Model) -> [Monster]
        """

        self._monsters = [m for m in self._monsters if m.get_health() > 0]
        return self._monsters

    def player_take_item(self):
        """
        Makes the player take the item that they are close to, else nothing.

        Model.player_take_item(Model) -> None
        """

        cx, cy = self._player.get_position()
        for item in self._items:
            if not item.is_taken() and close_to(self._player.get_position(),
                                                item.get_position()):
                item.set_taken()
                self._player.take(item)
                return

