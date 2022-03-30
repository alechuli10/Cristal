from Pared import Pared
from Casa import Casa
from ParedCortina import ParedCortina
from Ventana import Ventana

def levantarCasa ():
  pared_norte = Pared("NORTE") 
  pared_oeste = Pared("OESTE") 
  pared_sur = Pared("SUR") 
  pared_este = Pared("ESTE") 
  # Instanciación de las ventanas 
  ventana_norte = Ventana(pared_norte, 0.5) 
  ventana_oeste = Ventana(pared_oeste, 1) 
  ventana_sur = Ventana(pared_sur, 2) 
  ventana_este = Ventana(pared_este, 1) 
  # Instanciación de la casa con las 4 paredes 
  casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
  print(casa.superficie_acristalada())
  casa.paredes[2] = ParedCortina("SUR", 10) 
  print(casa.superficie_acristalada())