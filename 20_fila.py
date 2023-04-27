from lib.queue import Queue

fila = Queue()

fila.enqueue("Leotildes")
fila.enqueue("Orozimbo")
fila.enqueue("Valdisney")
fila.enqueue("Adamastor")

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila)

fila.enqueue("Marcinéia")

proximo = fila.peek()
print(f"Próximo a ser atendido: {proximo}")
print(fila)
