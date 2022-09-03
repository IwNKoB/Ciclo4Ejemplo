from abc import ABCMeta

class AbstractModel(metaclass=ABCMeta):
    #Constructor
    def __init__(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)
    #Destructor
    #def __del__(self):
     #   print ("Soy el destructor de la clase")