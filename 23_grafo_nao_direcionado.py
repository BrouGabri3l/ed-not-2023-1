from lib.graph import Graph

estradas = Graph()  # Não direcionado, por padrão
print(estradas)

estradas.add_vertex("Franca")
print(estradas)
print(f"GRAU FRANCA (a): {estradas.degree('Franca')}")
estradas.add_edge("Franca", "Batatais", "Rod. Candido Portinari")
print(estradas)
print(f"GRAU FRANCA (b): {estradas.degree('Franca')}")
estradas.add_edge("Franca", "Restinga")
print(estradas)
print(f"GRAU FRANCA (c): {estradas.degree('Franca')}")

#Remoção da aresta Batatais <-> Franca
estradas.remove_edge("Batatais","Franca", "Rod. Candido Portinari")