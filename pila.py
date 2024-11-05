class Stack: #pila

    def __init__(self) -> None: #constructor
        self.__elements = [] # __ hace que sea privado (no se puede utilizar fuera de la clase)

    def push(self, element): #agrego
        """Agrega elementos"""
        self.__elements.append(element)

    def pop(self): #saco
        """Saca el elemento de arriba"""
        if len(self.__elements) > 0 :
            return self.__elements.pop() #saca el primero (ultimo en lista)
        else:
            return None

    def on_top(self): #muestra el ultimo
        """Muestra el elemento de arriba"""
        if len(self.__elements) > 0:
            return self.__elements[-1] #numeros negativos muestran los ultimos
        else:
            return None

    def size(self):
        """Muestra el tamaño de la pila"""
        return len(self.__elements)