from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
from copy import deepcopy
from math import inf

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vAdjacentes(self, v):
        adjacentes = []

        for i in range(len(self.M)):
            for k in range(len(self.M)):
                if (len(self.M[i][k]) > 0):
                    if (self.N[i] == v):
                        adjacentes.append(self.N[k])
        return adjacentes

    def drone(self, origem, destino):

        '''
        Provê uma lista aplicando o algotimo de dijkstra modificado.
        O objetivo é levar um drone de um ponto de um mapa até outro ponto do mesmo mapa,
        encontrando o menor caminho que o drone deve fazer para chegar ao seu destino.
        :param V: o vertice origem, vertice destino, carga inicial, carga máxima,
        lista de vertices com pontos de carga.
        :return: lista com o menor caminho do grafo
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        grafo = self.N
        pi = {}
        beta = {}
        verticesNaoVisitados = []

        if (origem not in grafo or destino not in grafo):
            raise VerticeInvalidoException("O vértice não existe no grafo")

        # Adicionando os valores iniciais
        for v in grafo:
            beta[v] = inf
            verticesNaoVisitados.append(v)
        beta[origem] = 0


        verticesNaoVisitados.remove(origem)
        w = origem
        aux = 0
        a = []

        while w != destino:
            a = self.vAdjacentes(w)
            for r in a:
                if (r in verticesNaoVisitados):
                    if (beta[r] >= (beta[w] + 1)):
                        beta[r] = (beta[w] + 1)
                        pi[r] = w

            menorDosBetas = inf

            for i in verticesNaoVisitados:
                if (beta[i] < menorDosBetas):
                    menorDosBetas = beta[i]
                    betaMenor = i

            if (menorDosBetas == inf):
                return False

            aux = betaMenor
            verticesNaoVisitados.remove(aux)
            w = aux

        menorCaminhoDrone = []

        menorCaminhoDrone.append(destino)

        while destino != origem:
            menorCaminhoDrone.append(pi[destino])
            destino = pi[destino]

        menorCaminhoDrone.reverse()
        return menorCaminhoDrone