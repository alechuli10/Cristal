class Pared:
    def __init__ (self,orientacion):
        self.orientacion= orientacion
        self.ventanas= []
    
    def superficie_acristalada (self):
        superficie= 0
        for ventana in self.ventanas:
            superficie += ventana.cristal.superficie
        return superficie