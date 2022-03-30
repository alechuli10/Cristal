from Pared import Pared
from Cristal import Cristal

class ParedCortina (Pared):
    def __init__ (self,orientacion,superficie):
        Pared.__init__(self,orientacion)
        self.cristal= Cristal(superficie)
    def superficie_acristalada (self):
        return self.cristal.superficie