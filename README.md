# Aplicação Interativa com Grafos em Python

Este projeto implementa uma aplicação de terminal baseada em grafos, que permite ao usuário criar um mapa de cidades, conectar essas cidades com distâncias e encontrar caminhos entre elas. Tudo isso por meio de um menu interativo simples.

## Descrição

A estrutura principal do projeto é um **grafo direcionado e ponderado**, onde:

* **Vértices** representam cidades
* **Arestas** representam conexões com distâncias (pesos)

O usuário pode:

* Adicionar cidades
* Criar conexões entre cidades
* Visualizar todas as conexões
* Buscar um caminho entre duas cidades

A busca de caminho é feita utilizando o algoritmo **DFS (Depth-First Search)** de forma recursiva.

## Funcionalidades

* Adicionar cidades (vértices)
* Conectar cidades com distâncias (arestas com peso)
* Visualizar conexões cadastradas
* Encontrar caminho entre duas cidades
* Interface interativa via menu no terminal

## Exemplo de uso

```
--- MENU ---
1. Adicionar cidade
2. Conectar cidades
3. Mostrar conexões
4. Encontrar caminho entre cidades
5. Sair

Escolha uma opção: 1
Digite o nome da cidade: Palmas

Escolha uma opção: 2
Cidade de origem: Palmas
Cidade de destino: Paraiso
Distância entre as cidades: 20

Escolha uma opção: 4
Cidade de origem: Palmas
Cidade de destino: Paraiso
Palmas -> Paraiso
```

## Estrutura do Código

* `Edge`: Representa uma conexão entre duas cidades com peso (distância).
* `Vertex`: Representa uma cidade, com suas conexões.
* `Graph`: Controla a estrutura geral do grafo.
* `menu()`: Interface interativa com o usuário.
