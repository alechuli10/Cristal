from Cristal import Cristal

class Ventana:
    def __init__ (self, pared, superficie):
        self.cristal= Cristal(superficie)
        pared.ventanas.append(self)