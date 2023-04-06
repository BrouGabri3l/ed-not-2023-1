
class Stack: 

    """Método construtor"""
    def __init__(self):
        #Cria uma lista privada e vazia para armazenar
        #os dados da pilha
        self.__data = []
    """
        Método para inserção
        Em pilhas, tem nome padronizado: push
    """
    def push(self,val):
        self.__data.append(val)
    """
        Método que verifica se a pilha está ou não vazia
    """
    def is_empty(self):
        return len(self.__data) == 0
    """
        Método para remoção
        Em pilhas, tem nome padronizado pop
    """
    def pop(self):
        if self.is_empty():
            raise Exception("Erro: impossível remover de uma pilha vazia")
        #
        return self.__data.pop()
    """
        Método que permite consultar o valor que está no topo da pilha,
        sem removê-lo
        Em pilhas, tem nome padronizado peek
        ("Peek" signfica "dar uma espiadinha" em ingles )
    """
    def peek(self):
        if self.is_empty():
            raise Exception("Erro: impossível consultar uma lista vazia")
        return self.__data[-1] #
    def __str__(self):
        return str(self.__data)