from math import sqrt
from exceptions import *

class Weapon:
    def __init__(self,ammunitions,range) -> None:
        self.ammunations = ammunitions
        self.range = range
    def fire_at(self,x,y,z):
        if self.ammunations == 0:
            raise NoAmmunitionError
        self.ammunations -= 1
        if sqrt(x**2 + y**2) > self.range:
            raise OutOfRangeError
        

class Lancemissileantisurface(Weapon):
    def __init__(self) -> None:
        super().__init__(40, 30)
    def fire_at(self,x, y, z):
        super().fire_at(x,y,z)
        if z != 0:
            raise OutOfRangeError

class Lancemissileantiair(Weapon):
    def __init__(self) -> None:
        super().__init__(50, 40)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z <= 0:
            raise OutOfRangeError

class Lancetorpilles(Weapon):
    def __init__(self) -> None:
        super().__init__(15, 20)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z > 0:
            raise OutOfRangeError


if __name__ == "__main__":
    Lance_missile_anti_surface = Lancemissileantisurface()
    Lance_missile_anti_air = Lancemissileantiair()
    Lance_torpilles = Lancetorpilles()
    Lancemissileantiair.fire_at(0,0,0)
    assert Lancemissileantisurface.ammunations == 39
    try:
        Lancemissileantisurface.fire_at(0,0,1)
    except:
        assert Lancemissileantisurface.ammunations == 38
    Lancemissileantisurface.fire_at(0,0,1)
    assert Lancemissileantisurface.ammunations == 49
    try:
        Lancemissileantisurface.fire_at(0,0,0)
    except:
        assert Lancemissileantisurface.ammunations == 48
    Lancemissileantisurface.fire_at(0,0,0)
    assert Lancetorpilles.ammunations == 14
    Lancetorpilles.fire_at(0,0,-1)
    assert Lancetorpilles.ammunations == 13
    try:
        Lancetorpilles.fire_at(0,0,1)
    except:
        assert Lancetorpilles.ammunations == 12
