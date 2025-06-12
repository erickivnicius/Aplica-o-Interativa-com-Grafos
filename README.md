Aplicação Interativa com Grafos

Este projeto é uma aplicação em Python que simula um grafo direcionado e ponderado com um menu interativo. Através do terminal, você pode adicionar cidades, conectar rotas entre elas com pesos (distâncias), visualizar as conexões e buscar caminhos entre duas cidades.

Funcionalidades:

- Adicionar cidades (vértices do grafo)

- Conectar cidades com distâncias (arestas com peso)

- Exibir todas as conexões cadastradas

- Buscar um caminho entre duas cidades (busca em profundidade)

- Interface de menu simples e interativa no terminal


Estrutura usada:

O código é baseado na estrutura de grafo orientado, usando três classes principais:

- Vertex: representa uma cidade

- Edge: representa uma conexão com peso

- Graph: gerencia todos os vértices e conexões

A busca de caminho usa um algoritmo DFS (Depth-First Search) recursivo.
