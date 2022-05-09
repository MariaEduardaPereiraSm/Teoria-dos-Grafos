from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        '''Não há uma aresta entre dois vertices'''
        vna = []
        for v in self.N:
            va = []
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == v:
                    va.append(v2)
                elif v2 == v:
                    va.append(v1)
            for k in self.N:
                if k != v and k not in va:
                    a1 = f'{v}-{k}'
                    a2 = f'{k}-{v}'
                    if a1 not in vna and a2 not in vna:
                        vna.append(f'{v}-{k}')

            va = []

        return vna



    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True
        return False



    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        cont = 0
        tem_vertice = False

        for v in self.N:
            if v == V:
                tem_vertice = True
                for a in self.A:
                    v1 = self.A[a].getV1()
                    v2 = self.A[a].getV2()
                    if v1 == v:
                        cont += 1
                    if v2 == v:
                        cont += 1
        if tem_vertice == False and cont == 0:
            raise VerticeInvalidoException("O vértice", V, "não existe no grafo")
        else:
            return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        paralelas = []

        for v in self.N:
            va=[]
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == v:
                    va.append(v2)
                if v2 == v:
                    va.append(v1)
            for vertices in va:
                repeticoes = va.count(vertices)
                if repeticoes >= 2:
                    return True


        return False



    def arestas_sobre_vertice(self, V):

        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        ha_vertice = False
        va = []
        for v in self.N:
            if v == V:
                ha_vertice = True
        for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                if v1 == V or v2 == V:
                    va.append(a)
        if ha_vertice == False:
            raise VerticeInvalidoException("Esse vértice não existe no grafo")
        else:
            return va


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        if self.ha_paralelas():
            return False
        quantidade_vertices = len(self.N)
        for vertice in self.N:
            grau = self.grau(vertice)
            if grau != quantidade_vertices-1:
                return False
        return True

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass