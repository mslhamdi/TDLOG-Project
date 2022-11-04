from tp1 import *


class Vessel:
    def __init__(self,coordinates,max_hits,weapon):
        self.coord=coordinates
        self.max_hits=max_hits
        self.weapon=weapon

    def go_to(self,x,y,z):
        if self.max_hits==0:
            print('DestroyedError')
        else:
            print("I go to (",x,",",y,",",z,")")
            self.coord=(x,y,z)
    
    def get_coordinates(self):
        print(self.coord)

    def fire_at(self,x,y,z):
        if self.max_hits==0:
            print('DestroyedError')
        else:
            return self.weapon.fire_at(x,y,z)

class Cruiser(Vessel):
    def __init__(self,coordinates,weapon,max_hits=6):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z>0:
            print("I can't go higher")
        elif z<0:
            print("I can't go lower")
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)

class Submarine(Vessel):
    def __init__(self,coordinates,weapon,max_hits=2):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=0 or z!=1:
            print("I can't go there")
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)
        

class Fregate(Vessel):
    def __init__(self,coordinates,weapon,max_hits=5):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=0:
            print("I can't go there")
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)


class Destroyer(Vessel):
    def __init__(self,coordinates,weapon,max_hits=4):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=0:
            print("I can't go there")
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)


class Aircraft(Vessel):
    def __init__(self,coordinates,weapon,max_hits=1):
        super().__init__(coordinates,max_hits,weapon)

    def go_to(self,x,y,z):
        if z!=1:
            print("I can't go there")
        else:
            super().go_to(x,y,z)

    def get_coordinates(self):
        super().get_coordinates()

    def fire_at(self,x,y,z):
        super().fire_at(x,y,z)
    
#test
Anti_air=Lance_missiles_antiair()
lance_torpilles_1=Lance_torpilles()
lance_missiles_anti_surface_1=Lance_missiles_antisurface()
lance_torpilles_2=Lance_torpilles()
lance_missiles_anti_surface_2=Lance_missiles_antisurface()

Cruiser=Cruiser((1,1,0),Anti_air,6)
Submarine=Submarine((1,1,-1),lance_torpilles_1,2)
Fregate=Fregate((2,2,0),lance_missiles_anti_surface_1,5)
Destroyer=Destroyer((3,3,0),lance_torpilles_2,4)
Aircraft=Aircraft((1,1,1),lance_missiles_anti_surface_2,1)

Cruiser.go_to(1,2,10)
Cruiser.go_to(1,2,-10)
Cruiser.get_coordinates()
Cruiser.go_to(5,7,0)
Cruiser.get_coordinates()
print(Cruiser.weapon.amo)# affiche le nombre d'amo de l'arme
Cruiser.fire_at(10,10,10)# car c anti_air donc ca marche normal car z>0
Cruiser.fire_at(10,10,-10) #ici ca affiche OutOfRangeError
print(Cruiser.weapon.amo)#le nombre d'amo a diminue de 1 apres OutOfRangeError

#de meme on pourra tester tous les autres vessaux






