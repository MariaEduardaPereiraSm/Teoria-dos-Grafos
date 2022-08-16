import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.g_e.adicionaAresta('1', 'A', 'B')
        self.g_e.adicionaAresta('2', 'A', 'C')
        self.g_e.adicionaAresta('3', 'C', 'A')
        self.g_e.adicionaAresta('4', 'C', 'B')
        self.g_e.adicionaAresta('10', 'C', 'B')
        self.g_e.adicionaAresta('5', 'C', 'D')
        self.g_e.adicionaAresta('6', 'D', 'D')
        self.g_e.adicionaAresta('7', 'D', 'B')
        self.g_e.adicionaAresta('8', 'D', 'E')
        self.g_e.adicionaAresta('9', 'E', 'A')
        self.g_e.adicionaAresta('11', 'E', 'B')

        # Matrizes para teste do algoritmo de Warshall

        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1

        # Dijkstra algorithm

        self.dijkstra = MeuGrafo(
            ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16',
             'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'V29', 'V30', 'V31',
             'V32', 'V33'])

        self.dijkstra.adicionaAresta('a1', 'V1', 'V4')
        self.dijkstra.adicionaAresta('a2', 'V1', 'V3')
        self.dijkstra.adicionaAresta('a3', 'V1', 'V2')
        self.dijkstra.adicionaAresta('a4', 'V2', 'V3')
        self.dijkstra.adicionaAresta('a5', 'V2', 'V5')
        self.dijkstra.adicionaAresta('a6', 'V3', 'V6')
        self.dijkstra.adicionaAresta('a7', 'V4', 'V8')
        self.dijkstra.adicionaAresta('a8', 'V4', 'V12')
        self.dijkstra.adicionaAresta('a9', 'V5', 'V6')
        self.dijkstra.adicionaAresta('a10', 'V5', 'V9')
        self.dijkstra.adicionaAresta('a11', 'V6', 'V7')
        self.dijkstra.adicionaAresta('a12', 'V6', 'V10')
        self.dijkstra.adicionaAresta('a13', 'V6', 'V11')
        self.dijkstra.adicionaAresta('a14', 'V7', 'V4')
        self.dijkstra.adicionaAresta('a15', 'V7', 'V11')
        self.dijkstra.adicionaAresta('a16', 'V8', 'V7')
        self.dijkstra.adicionaAresta('a17', 'V9', 'V13')
        self.dijkstra.adicionaAresta('a18', 'V10', 'V14')
        self.dijkstra.adicionaAresta('a19', 'V11', 'V12')
        self.dijkstra.adicionaAresta('a20', 'V11', 'V15')
        self.dijkstra.adicionaAresta('a21', 'V12', 'V16')
        self.dijkstra.adicionaAresta('a22', 'V13', 'V17')
        self.dijkstra.adicionaAresta('a23', 'V14', 'V18')
        self.dijkstra.adicionaAresta('a24', 'V15', 'V17')
        self.dijkstra.adicionaAresta('a25', 'V15', 'V18')
        self.dijkstra.adicionaAresta('a26', 'V15', 'V19')
        self.dijkstra.adicionaAresta('a27', 'V16', 'V18')
        self.dijkstra.adicionaAresta('a28', 'V16', 'V20')
        self.dijkstra.adicionaAresta('a29', 'V18', 'V19')
        self.dijkstra.adicionaAresta('a30', 'V18', 'V21')
        self.dijkstra.adicionaAresta('a31', 'V19', 'V20')
        self.dijkstra.adicionaAresta('a32', 'V19', 'V23')
        self.dijkstra.adicionaAresta('a33', 'V20', 'V24')
        self.dijkstra.adicionaAresta('a34', 'V21', 'V25')
        self.dijkstra.adicionaAresta('a35', 'V21', 'V26')
        self.dijkstra.adicionaAresta('a36', 'V22', 'V18')
        self.dijkstra.adicionaAresta('a37', 'V23', 'V22')
        self.dijkstra.adicionaAresta('a38', 'V23', 'V27')
        self.dijkstra.adicionaAresta('a39', 'V23', 'V28')
        self.dijkstra.adicionaAresta('a40', 'V24', 'V28')
        self.dijkstra.adicionaAresta('a41', 'V24', 'V29')
        self.dijkstra.adicionaAresta('a42', 'V26', 'V22')
        self.dijkstra.adicionaAresta('a43', 'V26', 'V31')
        self.dijkstra.adicionaAresta('a44', 'V29', 'V32')
        self.dijkstra.adicionaAresta('a45', 'V31', 'V30')
        self.dijkstra.adicionaAresta('a46', 'V31', 'V33')
        self.dijkstra.adicionaAresta('a47', 'V32', 'V31')
        self.dijkstra.adicionaAresta('a48', 'V17', 'V18')
        self.dijkstra.adicionaAresta('a49', 'V33', 'V30')

        self.dijkstra_algorithm = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13'])
        self.dijkstra_algorithm.adicionaAresta('a1', 'V1', 'V4')
        self.dijkstra_algorithm.adicionaAresta('a2', 'V2', 'V5')
        self.dijkstra_algorithm.adicionaAresta('a3', 'V1', 'V3')
        self.dijkstra_algorithm.adicionaAresta('a4', 'V1', 'V2')
        self.dijkstra_algorithm.adicionaAresta('a5', 'V3', 'V6')
        self.dijkstra_algorithm.adicionaAresta('a6', 'V4', 'V12')
        self.dijkstra_algorithm.adicionaAresta('a7', 'V5', 'V9')
        self.dijkstra_algorithm.adicionaAresta('a8', 'V4', 'V8')
        self.dijkstra_algorithm.adicionaAresta('a9', 'V2', 'V3')
        self.dijkstra_algorithm.adicionaAresta('a10', 'V5', 'V6')
        self.dijkstra_algorithm.adicionaAresta('a11', 'V6', 'V10')
        self.dijkstra_algorithm.adicionaAresta('a12', 'V6', 'V11')
        self.dijkstra_algorithm.adicionaAresta('a13', 'V6', 'V7')

    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g.N)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    '''def test_warshall(self):
        self.assertEqual(self.g_p.warshall(), self.g_p_m)
        self.assertEqual(self.g_e.warshall(), self.g_e_m)'''

    def test_drone(self):
        self.assertEqual(self.dijkstra.drone('V2', 'V26'),['V2', 'V5', 'V9', 'V13', 'V17', 'V18', 'V21', 'V26'])
        self.assertEqual(self.dijkstra.drone('V7', 'V30'),['V7', 'V11', 'V15', 'V18', 'V21', 'V26', 'V31', 'V30'])
        self.assertEqual(self.dijkstra.drone('V20', 'V33'),['V20', 'V24', 'V29', 'V32', 'V31', 'V33'])
        self.assertFalse(self.dijkstra_algorithm.drone('V3', 'V12'), )
        self.assertEqual(self.dijkstra_algorithm.drone('V1', 'V10'), ['V1', 'V3', 'V6', 'V10'])
        self.assertEqual(self.dijkstra_algorithm.drone('V1', 'V9'), ['V1', 'V2', 'V5', 'V9'])
        self.assertEqual(self.dijkstra.drone('V3', 'V10'), ['V3', 'V6', 'V10'])
        self.assertEqual(self.dijkstra.drone('V1', 'V33'),['V1', 'V4', 'V12', 'V16', 'V18', 'V21', 'V26', 'V31', 'V33'])

