
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import deque

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

    def gerarVerticesAdjacencentes(self):
        '''
        Gera dicionário com os vertices adjacentes de cada vértice do grafo
        para otimizar a realização da DFS e da BFS.
        '''
        verticesAdjacentes = {}

        for aresta in self.A:
            arestaAtual = self.A[aresta]
            if arestaAtual.getV1() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV1()] = [(arestaAtual.getV2(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV1()].append((arestaAtual.getV2(), aresta))

            if arestaAtual.getV2() not in verticesAdjacentes:
                verticesAdjacentes[arestaAtual.getV2()] = [(arestaAtual.getV1(), aresta)]
            else:
                verticesAdjacentes[arestaAtual.getV2()].append((arestaAtual.getV1(), aresta))

        return verticesAdjacentes

    def dfs_recursivo(self, V, dfs, verticesVisitados, verticesAdjacentes):
        '''
        Responsável por percorrer o grafo de modo recursivo
        :param V: O vértice atual
        :param dfs: Grafo que será construido pela DFS
        :param verticesVisitados: Conjunto responsável por armazenar os
        vértices já visitados durante a busca
        :param verticesAdjacentes: Lista de Adjacência do grafo
        '''
        verticesVisitados.add(V)

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            '''Percorro todos os vertices adjacentes de V-> pegando seu adjacente e sua aresta'''

            if verticeAdjacente not in verticesVisitados:
                '''se o vértice adjacente de V não foi visitado'''
                dfs.adicionaAresta(rotuloAresta, V, verticeAdjacente)
                self.dfs_recursivo(verticeAdjacente, dfs, verticesVisitados, verticesAdjacentes)

    def dfs(self, V=''):
        '''
        Provê um grafo gerado pela DFS partindo do vértice passado como parâmetro.
        :param V: O vértice de partida
        :return: Um objeto do tipo MeuGrafo com o grafo gerado
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
       
        if not self.existeVertice(V):
            raise VerticeInvalidoException(f'O vértice {V} passado como parâmetro não existe.')

        verticesAdjacentes = self.gerarVerticesAdjacencentes()

        dfs = MeuGrafo(self.N[::])
        verticesVisitados = set()

        if V not in verticesAdjacentes: return dfs

        self.dfs_recursivo(V, dfs, verticesVisitados, verticesAdjacentes)

        return dfs

    def bfs(self, V=''):
        '''
        Provê um novo grafo após realizar o bfs
        :param V: O vértice raíz
        :return: Uma lista com o novo grafo pós bfs
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        bfs = MeuGrafo(self.N[::])

        verticesVisitados = [V]
        fila = [V]

        temVertice = False

        for v in self.N:
            if v == V:
                temVertice = True

        while (len(fila) != 0):
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                verticeAnalisado = fila[0]

                if v1 == verticeAnalisado or v2 == verticeAnalisado:
                    verticeAdjacente = v2 if verticeAnalisado == v1 else v1

                    if verticeAdjacente not in verticesVisitados:
                        fila.append((verticeAdjacente))
                        verticesVisitados.append(verticeAdjacente)
                        bfs.adicionaAresta(a, verticeAnalisado, verticeAdjacente)

            fila.pop(0)

        if (temVertice == False):
            raise VerticeInvalidoException("O vértice", V, "não existe no grafo")
        else:
            return bfs

    def recursivo_ciclo(self, V, dfs, verticesVisitados, verticesAdjacentes):
        '''
        Responsável por percorrer o grafo de modo recursivo
        :param V: O vértice atual
        :param dfs: Grafo que será construido pela DFS
        :param verticesVisitados: Conjunto responsável por armazenar os
        vértices já visitados durante a busca
        :param verticesAdjacentes: Lista de Adjacência do grafo
        '''

        verticesVisitados.add(V)

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            '''Percorro todos os vertices adjacentes de V-> pegando seu adjacente e sua aresta'''
            cont = 0
            if verticeAdjacente not in verticesVisitados:
                '''se o vértice adjacente de V não foi visitado'''
                self.recursivo_ciclo(verticeAdjacente, dfs, verticesVisitados, verticesAdjacentes)

        for (verticeAdjacente, rotuloAresta) in verticesAdjacentes[V]:
            if (verticeAdjacente in verticesVisitados):
                cont += 1
        if (cont >= 2):
            return True

    def ha_ciclo(self):
        if(self.ha_laco()):
            return True
        else:
            for vertice in self.N:
                visitados = set()
                arestas = dict([(nomeAresta, [self.A[nomeAresta], "NADA"])
                                for nomeAresta in self.A.keys()])
                pai = vertice
                # Usando a mesma lógica utilizada no método que gera a arvore dfs
                # percorremos o grafo a partir de todos os vertices possiveis verificando
                # se em algum desses caminhos temos duas ligações validas com a raiz.
                caminho = [pai]
                while(len(visitados) != len(self.N)):
                    visitados.add(pai)
                    arestasFilhas = self.arestas_sobre_vertice(pai)

                    for filha in arestasFilhas:
                        valor1 = arestas[filha][0]
                        valor1 = str(valor1)
                        valor1 = valor1.replace(pai, "").replace("-", "")

                        if(arestas[filha][1] != "RETORNO" and len(valor1)>1):
                            if len(valor1) == 10 :
                                v = valor1[4]
                            else:
                                v = valor1[3]

                            """ arestas[filha][0] = valor1"""
                            destino = arestas
                            destino[filha][0] = v
                            destino = arestas[filha][0].replace(
                                pai, "").replace("-", "")

                            if(arestas[filha][1] == "NADA"):
                                if(not destino in visitados):
                                    arestas[filha][1] = "DIRECIONADO"
                                    caminho.append(filha)
                                    caminho.append(destino)
                                    pai = destino
                                    break
                                else:
                                    return True

                            else:
                                arestas[filha][1] = "RETORNO"

                        elif(all([arestas[arestaFilhaCorr][1] == "RETORNO" for arestaFilhaCorr in arestasFilhas])):
                            pai = arestas[filha][0].replace(
                                pai, "").replace("-", "")
                            # pai = arestas[caminho[caminho.index(
                            #     pai)-1]][0].replace(pai, "").replace("-", "")
                            # pai = arestas[filha][0].replace(
                            #     pai, "").replace("-", "")
                            if(pai == vertice):
                                if(all([filho in visitados for filho in self.vertices_filhos(vertice)])) and len(self.N) > len(visitados):
                                    pai = vertice
                            break
        return False

    def arestas(self, V):
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
            return va
        else:
            return va

    def caminho(self, n):

        if (n <= 0) or (n > len(self.N)) and n + 1 > len(self.N):
            return False
        else:
            for raizC in self.N:
                raiz = raizC
                arestas = dict([(nomeAresta, [self.A[nomeAresta], "NADA"])
                                for nomeAresta in self.A.keys()])
                countTamanho = 0

                res = [raiz]

                while (countTamanho < n):
                    temCaminho = False
                    for arestaC in self.arestas(raiz):
                        valor1 = arestas[arestaC][0]
                        valor1 = str(valor1)

                        if (arestas[arestaC][1] == "NADA" and not valor1 in res):
                            valor1 = valor1.replace(raiz, "").replace("-", "")
                            arestas[arestaC][1] = "VISITADA"
                            res.append(arestaC)
                            countTamanho += 1
                            if len(valor1) == 10 :
                                v = valor1[4]
                            else:
                                v = valor1[3]

                            raiz = arestas
                            raiz[arestaC][0] = v

                            res.append(raiz)
                            temCaminho = True
                            ant = res[res.index(raiz) - 2]
                            break

                    if not temCaminho:
                        if (len(res) == 1):
                            break
                        raiz = res[res.index(raiz) - 2]
                        res = res[:-2]
                        countTamanho -= 1
                if (countTamanho == n):
                    return res


            return False

    def aux_conexo(self, V=''):
        bfs = MeuGrafo([V])

        verticesVisitados = [V]
        fila = [V]
        listaBfs = [V]

        while (len(fila) != 0):
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                verticeAnalisado = fila[0]

                if v1 == verticeAnalisado or v2 == verticeAnalisado:
                    verticeAdjacente = v2 if verticeAnalisado == v1 else v1

                    if verticeAdjacente not in verticesVisitados:
                        bfs.adicionaVertice(verticeAdjacente)
                        fila.append((verticeAdjacente))
                        verticesVisitados.append(verticeAdjacente)
                        bfs.adicionaAresta(a, verticeAnalisado, verticeAdjacente)
                        listaBfs.append(verticeAdjacente)

            fila.pop(0)
        return listaBfs

    def conexo(self):
        '''
        Verifica se o grafo é conexo
        :return: Um valor booleano que indica se o grafo é ou não conexo
        '''
        grafo_bfs = self.aux_conexo(self.N[0])
        tamanhoGrafoBfs = len(grafo_bfs)
        tamanhoGrafoAnalisado = len(self.N)

        if (tamanhoGrafoBfs != tamanhoGrafoAnalisado):
            return False
        else:
            return True

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass

    def verticesAdjacentes(self):
        pass