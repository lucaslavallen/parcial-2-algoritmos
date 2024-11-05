class Queue: #cola
    def __init__(self) -> None:
        self.__elements= []
    
    def arrive(self, element):
        """Agrega elementos"""
        self.__elements.append(element)

    def attention(self):
        """Devuelve y saca el primer elemento"""
        if len(self.__elements)>0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        """Muestra el tamaño"""
        return len(self.__elements)
    
    def on_front(self):
        """Muestra el elemento en frente"""
        if len(self.__elements)>0:
            return self.__elements[0]
        else:
            return None
        
    def move_to_end(self):
        """Saca el elemento del frente y lo manda al final"""
        element= self.attention()
        if element is not None:
            self.arrive(element)