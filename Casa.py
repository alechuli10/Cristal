class Casa:
    def __init__ (self, paredes):
        self.paredes= paredes
        
    
    def superficie_acristalada (self):
        superficie= 0
        for pared in self.paredes:
            superficie += pared.superficie_acristalada()
        return superficie