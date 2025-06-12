class Edge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight


class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacents = []

    def addEdge(self, target, weight):
        self.adjacents.append(Edge(target, weight))


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)
        else:
            print(f"Vértice '{name}' já existe.")

    def addEdge(self, source, target, weight):
        if source not in self.vertices:
            self.addVertex(source)
        if target not in self.vertices:
            self.addVertex(target)
        self.vertices[source].addEdge(target, weight)

    def showConnections(self):
        for name, vertex in self.vertices.items():
            print(f"\n{name} está conectado com:")
            for edge in vertex.adjacents:
                print(f"  -> {edge.target} (peso: {edge.weight})")

    def findPath(self, source, target, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if source in visited:
            return None

        visited.add(source)
        path.append(source)

        if source == target:
            return path.copy()

        for edge in self.vertices[source].adjacents:
            result = self.findPath(edge.target, target, visited, path)
            if result:
                return result

        path.pop()
        return None


def menu():
    graph = Graph()

    while True:
        print("\n--- MENU ---")
        print("1. Adicionar cidade")
        print("2. Conectar cidades")
        print("3. Mostrar conexões")
        print("4. Encontrar caminho entre cidades")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome da cidade: ")
            graph.addVertex(nome)

        elif opcao == '2':
            origem = input("Cidade de origem: ")
            destino = input("Cidade de destino: ")
            peso = int(input("Distância entre as cidades: "))
            graph.addEdge(origem, destino, peso)
            print("Conexão adicionada.")

        elif opcao == '3':
            graph.showConnections()

        elif opcao == '4':
            origem = input("Cidade de origem: ")
            destino = input("Cidade de destino: ")
            if origem in graph.vertices and destino in graph.vertices:
                caminho = graph.findPath(origem, destino)
                if caminho:
                    print(" -> ".join(caminho))
                else:
                    print("Nenhum caminho encontrado.")
            else:
                print("Uma ou ambas as cidades não existem no grafo.")

        elif opcao == '5':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Iniciar aplicação
menu()