import random

from abc import ABCMeta, abstractmethod
from gameutils import print_bold, weighted_random_selection
from gameuniterror import GameUnitError

class AbstractGameUnit(metaclass=ABCMeta):
    """Abstract class to represent a game character (or a 'unit')"""
    def __init__(self, name=''):
        self.max_hp = 0
        self.health_meter = 0
        self.name = name
        self.enemy = None
        self.unit_type = None

    @abstractmethod
    def info(self):
        """Print information about this game unit.

        Abstract method. See subclasses for implementation.
        """
        pass

    def attack(self, enemy):
        """The main logic to 'attack' the enemy unit

        Determines injured unit and the amount of injury

        .. todo:: Check if enemy exists!
        """
        injured_unit = weighted_random_selection(self, enemy)
        injury = random.randint(10, 15)
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0)
        print("ATTACK! ", end='')
        self.show_health(end='  ')
        enemy.show_health(end='  ')

    def heal(self, heal_by=2, full_healing=True):
        """Heal the unit replenishing its hit points"""
        if self.health_meter == self.max_hp:
            return
        if full_healing:
            self.health_meter = self.max_hp
        else:
            self.health_meter += heal_by
        # ------------------------------------------------------------------
        # raise a custom exception. Refer to chapter on exception handling
        # ------------------------------------------------------------------
        if self.health_meter > self.max_hp:
            raise GameUnitError("health_meter > max_hp!", 101)

        print_bold("You are HEALED!", end=' ')
        self.show_health(bold=True)

    def reset_health_meter(self):
        """Reset the `health_meter` (assign default hit points)"""
        self.health_meter = self.max_hp

    def show_health(self, bold=False, end='\n'):
        """Print info on the current health reading of this game unit"""
        # TODO: what if there is no enemy?
        msg = "Health: %s: %d" % (self.name, self.health_meter)

        if bold:
            print_bold(msg, end=end)
        else:
            print(msg, end=end)
