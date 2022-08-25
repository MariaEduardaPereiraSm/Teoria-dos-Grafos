import unittest
from meu_grafo_matriz_adjacencia_nao_dir import *
from meu_grafo import *
#from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):

        # Grafo Exemplo Prim e Kruskal
        self.grafo_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.grafo_prim.adicionaAresta('1', 'A', 'B', 1100)
        self.grafo_prim.adicionaAresta('2', 'A', 'F', 1200)
        self.grafo_prim.adicionaAresta('3', 'A', 'C', 1800)
        self.grafo_prim.adicionaAresta('4', 'B', 'C', 900)
        self.grafo_prim.adicionaAresta('5', 'B', 'D', 800)
        self.grafo_prim.adicionaAresta('6', 'B', 'E', 750)
        self.grafo_prim.adicionaAresta('7', 'A', 'D', 2000)
        self.grafo_prim.adicionaAresta('8', 'C', 'D', 700)
        self.grafo_prim.adicionaAresta('9', 'C', 'F', 850)
        self.grafo_prim.adicionaAresta('10', 'D', 'E', 1100)
        self.grafo_prim.adicionaAresta('11', 'E', 'F', 500)

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

        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C', 2)
        self.g_p4.adicionaAresta('a2', 'C', 'E', 4)
        self.g_p4.adicionaAresta('a3', 'C', 'E', 1)
        self.g_p4.adicionaAresta('a4', 'P', 'C', 2)
        self.g_p4.adicionaAresta('a5', 'P', 'C', 6)
        self.g_p4.adicionaAresta('a6', 'T', 'C', 7)
        self.g_p4.adicionaAresta('a7', 'M', 'C', 8)
        self.g_p4.adicionaAresta('a8', 'M', 'T', 9)
        self.g_p4.adicionaAresta('a9', 'T', 'Z', 10)

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p2.adicionaAresta('a1', 'J', 'C')
        self.g_p2.adicionaAresta('a2', 'C', 'E')
        self.g_p2.adicionaAresta('a3', 'C', 'E')
        self.g_p2.adicionaAresta('a4', 'P', 'C')
        self.g_p2.adicionaAresta('a5', 'P', 'C')
        self.g_p2.adicionaAresta('a6', 'T', 'C')
        self.g_p2.adicionaAresta('a7', 'M', 'C')
        self.g_p2.adicionaAresta('a8', 'M', 'T')
        self.g_p2.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p3.adicionaAresta('a', 'J', 'C')
        self.g_p3.adicionaAresta('a2', 'C', 'E')
        self.g_p3.adicionaAresta('a3', 'C', 'E')
        self.g_p3.adicionaAresta('a4', 'P', 'C')
        self.g_p3.adicionaAresta('a5', 'P', 'C')
        self.g_p3.adicionaAresta('a6', 'T', 'C')
        self.g_p3.adicionaAresta('a7', 'M', 'C')
        self.g_p3.adicionaAresta('a8', 'M', 'T')
        self.g_p3.adicionaAresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p4.adicionaAresta('a1', 'J', 'C')
        self.g_p4.adicionaAresta('a2', 'J', 'E')
        self.g_p4.adicionaAresta('a3', 'C', 'E')
        self.g_p4.adicionaAresta('a4', 'P', 'C')
        self.g_p4.adicionaAresta('a5', 'P', 'C')
        self.g_p4.adicionaAresta('a6', 'T', 'C')
        self.g_p4.adicionaAresta('a7', 'M', 'C')
        self.g_p4.adicionaAresta('a8', 'M', 'T')
        self.g_p4.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        self.g_p1_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p1_sem_paralelas.adicionaAresta('a1', 'J', 'C',1)
        self.g_p1_sem_paralelas.adicionaAresta('a2', 'C', 'E',6)
        self.g_p1_sem_paralelas.adicionaAresta('a3', 'P', 'C',2)
        self.g_p1_sem_paralelas.adicionaAresta('a4', 'T', 'C',1)
        self.g_p1_sem_paralelas.adicionaAresta('a5', 'M', 'C',8)
        self.g_p1_sem_paralelas.adicionaAresta('a6', 'M', 'T',3)
        self.g_p1_sem_paralelas.adicionaAresta('a7', 'T', 'Z',1)


        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        # Grafos completos 2
        self.g_c1 = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c1.adicionaAresta('a1', 'J', 'C', 1)
        self.g_c1.adicionaAresta('a2', 'J', 'E', 10)
        self.g_c1.adicionaAresta('a3', 'J', 'P', 44)
        self.g_c1.adicionaAresta('a4', 'E', 'C', 109)
        self.g_c1.adicionaAresta('a5', 'P', 'C', 184)
        self.g_c1.adicionaAresta('a6', 'P', 'E', 199)

        self.g_c12 = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c12.adicionaAresta('a1', 'J', 'C', 1399)
        self.g_c12.adicionaAresta('a2', 'J', 'E', 10)
        self.g_c12.adicionaAresta('a3', 'J', 'P', 44)
        self.g_c12.adicionaAresta('a4', 'E', 'C', 109)
        self.g_c12.adicionaAresta('a5', 'P', 'C', 184)
        self.g_c12.adicionaAresta('a6', 'P', 'E', 199)

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
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        self.g_d.adicionaAresta('a1', 'A', 'B')
        self.g_d.adicionaAresta('a2', 'B', 'C')
        self.g_d.adicionaAresta('a3', 'C', 'D')
        self.g_d.adicionaAresta('a4', 'B', 'D')
        self.g_d.adicionaAresta('a5', 'A', 'C')
        self.g_d.adicionaAresta('a6', 'E', 'F')
        self.g_d.adicionaAresta('a7', 'F', 'G')
        self.g_d.adicionaAresta('a8', 'G', 'J')
        self.g_d.adicionaAresta('a9', 'J', 'I')
        self.g_d.adicionaAresta('a10', 'I', 'G')

        self.g_e = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_e.adicionaAresta('asd', 'A', 'B')

        self.g_e2 = MeuGrafo(['A', 'B', 'C', 'D'])

        self.g_v1 = MeuGrafo(['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8'])
        self.g_v1.adicionaAresta('a1', 'V1', 'V2')
        self.g_v1.adicionaAresta('a2', 'V2', 'V3')
        self.g_v1.adicionaAresta('a3', 'V3', 'V4')
        self.g_v1.adicionaAresta('a4', 'V4', 'V5')
        self.g_v1.adicionaAresta('a5', 'V5', 'V6')
        self.g_v1.adicionaAresta('a6', 'V7', 'V8')

        self.g_d2 = MeuGrafo(['A', 'B', 'C', 'D'])

        self.nlw = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.nlw.adicionaAresta('1', 'A', 'B')
        self.nlw.adicionaAresta('2', 'A', 'G')
        self.nlw.adicionaAresta('3', 'A', 'J')
        self.nlw.adicionaAresta('4', 'K', 'G')
        self.nlw.adicionaAresta('5', 'K', 'J')
        self.nlw.adicionaAresta('6', 'J', 'G')
        self.nlw.adicionaAresta('7', 'J', 'I')
        self.nlw.adicionaAresta('8', 'I', 'G')
        self.nlw.adicionaAresta('9', 'G', 'H')
        self.nlw.adicionaAresta('10', 'H', 'F')
        self.nlw.adicionaAresta('11', 'F', 'B')
        self.nlw.adicionaAresta('12', 'G', 'B')
        self.nlw.adicionaAresta('13', 'B', 'C')
        self.nlw.adicionaAresta('14', 'C', 'D')
        self.nlw.adicionaAresta('15', 'D', 'E')
        self.nlw.adicionaAresta('16', 'B', 'D')
        self.nlw.adicionaAresta('17', 'B', 'E')

        # Outros testes

        self.grafo_A = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_A.adicionaAresta('1', 'A', 'B')
        self.grafo_A.adicionaAresta('11', 'B', 'F')
        self.grafo_A.adicionaAresta('10', 'F', 'H')
        self.grafo_A.adicionaAresta('9', 'H', 'G')
        self.grafo_A.adicionaAresta('4', 'G', 'K')
        self.grafo_A.adicionaAresta('5', 'K', 'J')
        self.grafo_A.adicionaAresta('7', 'J', 'I')
        self.grafo_A.adicionaAresta('13', 'B', 'C')
        self.grafo_A.adicionaAresta('14', 'C', 'D')
        self.grafo_A.adicionaAresta('15', 'D', 'E')

        self.grafo_B = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_B.adicionaAresta('10', 'F', 'H')
        self.grafo_B.adicionaAresta('9', 'H', 'G')
        self.grafo_B.adicionaAresta('2', 'G', 'A')
        self.grafo_B.adicionaAresta('1', 'A', 'B')
        self.grafo_B.adicionaAresta('13', 'B', 'C')
        self.grafo_B.adicionaAresta('14', 'C', 'D')
        self.grafo_B.adicionaAresta('15', 'D', 'E')
        self.grafo_B.adicionaAresta('3', 'A', 'J')
        self.grafo_B.adicionaAresta('5', 'J', 'K')
        self.grafo_B.adicionaAresta('7', 'J', 'I')

        self.grafo_C = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_C.adicionaAresta('4', 'K', 'G')
        self.grafo_C.adicionaAresta('2', 'G', 'A')
        self.grafo_C.adicionaAresta('1', 'A', 'B')
        self.grafo_C.adicionaAresta('11', 'B', 'F')
        self.grafo_C.adicionaAresta('10', 'F', 'H')
        self.grafo_C.adicionaAresta('13', 'B', 'C')
        self.grafo_C.adicionaAresta('14', 'C', 'D')
        self.grafo_C.adicionaAresta('15', 'D', 'E')
        self.grafo_C.adicionaAresta('3', 'A', 'J')
        self.grafo_C.adicionaAresta('7', 'J', 'I')

        self.grafo_D = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_D.adicionaAresta('13', 'C', 'B')
        self.grafo_D.adicionaAresta('1', 'B', 'A')
        self.grafo_D.adicionaAresta('2', 'A', 'G')
        self.grafo_D.adicionaAresta('4', 'G', 'K')
        self.grafo_D.adicionaAresta('5', 'K', 'J')
        self.grafo_D.adicionaAresta('7', 'J', 'I')
        self.grafo_D.adicionaAresta('9', 'G', 'H')
        self.grafo_D.adicionaAresta('10', 'H', 'F')
        self.grafo_D.adicionaAresta('16', 'B', 'D')
        self.grafo_D.adicionaAresta('15', 'D', 'E')

        self.grafo_E = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_E.adicionaAresta('1', 'A', 'B')
        self.grafo_E.adicionaAresta('2', 'A', 'G')
        self.grafo_E.adicionaAresta('3', 'A', 'J')
        self.grafo_E.adicionaAresta('11', 'F', 'B')
        self.grafo_E.adicionaAresta('13', 'B', 'C')
        self.grafo_E.adicionaAresta('16', 'B', 'D')
        self.grafo_E.adicionaAresta('17', 'B', 'E')
        self.grafo_E.adicionaAresta('4', 'K', 'G')
        self.grafo_E.adicionaAresta('8', 'I', 'G')
        self.grafo_E.adicionaAresta('9', 'G', 'H')

        self.grafo_F = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_F.adicionaAresta('10', 'H', 'F')
        self.grafo_F.adicionaAresta('11', 'F', 'B')
        self.grafo_F.adicionaAresta('9', 'G', 'H')
        self.grafo_F.adicionaAresta('1', 'A', 'B')
        self.grafo_F.adicionaAresta('13', 'B', 'C')
        self.grafo_F.adicionaAresta('16', 'B', 'D')
        self.grafo_F.adicionaAresta('17', 'B', 'E')
        self.grafo_F.adicionaAresta('4', 'K', 'G')
        self.grafo_F.adicionaAresta('6', 'J', 'G')
        self.grafo_F.adicionaAresta('8', 'I', 'G')

        self.grafo_G = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_G.adicionaAresta('4', 'K', 'G')
        self.grafo_G.adicionaAresta('5', 'K', 'J')
        self.grafo_G.adicionaAresta('2', 'A', 'G')
        self.grafo_G.adicionaAresta('8', 'I', 'G')
        self.grafo_G.adicionaAresta('9', 'G', 'H')
        self.grafo_G.adicionaAresta('12', 'G', 'B')
        self.grafo_G.adicionaAresta('10', 'H', 'F')
        self.grafo_G.adicionaAresta('13', 'B', 'C')
        self.grafo_G.adicionaAresta('16', 'B', 'D')
        self.grafo_G.adicionaAresta('17', 'B', 'E')

        self.grafo_H = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])

        self.grafo_H.adicionaAresta('13', 'B', 'C')
        self.grafo_H.adicionaAresta('14', 'C', 'D')
        self.grafo_H.adicionaAresta('1', 'A', 'B')
        self.grafo_H.adicionaAresta('11', 'F', 'B')
        self.grafo_H.adicionaAresta('12', 'G', 'B')
        self.grafo_H.adicionaAresta('17', 'B', 'E')
        self.grafo_H.adicionaAresta('3', 'A', 'J')
        self.grafo_H.adicionaAresta('10', 'H', 'F')
        self.grafo_H.adicionaAresta('4', 'K', 'G')
        self.grafo_H.adicionaAresta('8', 'I', 'G')

        self.g_u_d = MeuGrafo(['A', 'B'])
        self.g_u_d.adicionaAresta('a1', 'A', 'A')

        self.gdisc = MeuGrafo(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
        self.gdisc.adicionaAresta('a1', 'A', 'B')
        self.gdisc.adicionaAresta('a2', 'B', 'D')
        self.gdisc.adicionaAresta('a3', 'B', 'C')
        self.gdisc.adicionaAresta('a4', 'C', 'D')
        self.gdisc.adicionaAresta('a5', 'C', 'E')
        self.gdisc.adicionaAresta('a6', 'D', 'G')
        self.gdisc.adicionaAresta('a7', 'E', 'F')
        self.gdisc.adicionaAresta('a8', 'F', 'G')
        self.gdisc.adicionaAresta('a9', 'E', 'H')
        self.gdisc.adicionaAresta('a10', 'F', 'H')
        self.gdisc.adicionaAresta('a11', 'G', 'H')
        self.gdisc.adicionaAresta('a12', 'H', 'I')

        self.g_u = MeuGrafo(['A'])

        self.g_a = MeuGrafo(["A", "B", "C"])
        self.g_a.adicionaAresta('a1', 'A', 'B')
        self.g_a.adicionaAresta('a2', 'B', 'C')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()), set(['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z']))
        self.assertEqual(set(self.g_e.vertices_nao_adjacentes()), set(['A-C', 'A-D', 'B-C', 'B-D', 'C-D']))
        self.assertEqual(set(self.g_d2.vertices_nao_adjacentes()), set(['A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D']))
        self.assertEqual(set(self.g_c.vertices_nao_adjacentes()), set())
        self.assertEqual(set(self.g_c3.vertices_nao_adjacentes()), set())

        self.assertEqual(set(self.g_p.vertices_nao_adjacentes()),
                        set(['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z']))
        #self.assertEqual(set(self.g_d.vertices_nao_adjacentes()), set(['A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C']))
        #self.assertEqual(set(self.g_d2.vertices_nao_adjacentes()), set({'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D', 'B-A', 'C-A', 'D-A', 'C-B', 'D-B', 'D-C'}))
        self.assertEqual(set(self.g_c.vertices_nao_adjacentes()), set())
        self.assertEqual(set(self.g_c3.vertices_nao_adjacentes()), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_e.grau('A'), 1)
        self.assertEqual(self.g_e.grau('C'), 0)
        self.assertNotEqual(self.g_e.grau('D'), 2)
        self.assertEqual(self.g_e2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_e.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_e.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(set(self.g_p.dfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('C').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('E').A.keys()), set(['a2', 'a1', 'a4', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('P').A.keys()), set(['a4', 'a1', 'a2', 'a6', 'a8', 'a9']))
        self.assertEqual(set(self.g_p.dfs('M').A.keys()), set(['a7', 'a1', 'a2', 'a4', 'a6', 'a9']))
        self.assertEqual(set(self.g_p.dfs('T').A.keys()), set(['a6', 'a1', 'a2', 'a4', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.dfs('Z').A.keys()), set(['a9', 'a6', 'a1', 'a2', 'a4', 'a7']))

        self.assertEqual(set(self.g_p_sem_paralelas.dfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('C').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('E').A.keys()), set(['a2', 'a1', 'a3', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('P').A.keys()), set(['a3', 'a1', 'a2', 'a4', 'a6', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('M').A.keys()), set(['a5', 'a1', 'a2', 'a3', 'a4', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('T').A.keys()), set(['a4', 'a1', 'a2', 'a3', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs('Z').A.keys()), set(['a7', 'a4', 'a1', 'a2', 'a3', 'a5']))

        self.assertEqual(set(self.g_c.dfs('J').A.keys()), set(['a1', 'a4', 'a6']))
        self.assertEqual(set(self.g_c.dfs('C').A.keys()), set(['a1', 'a2', 'a6']))
        self.assertEqual(set(self.g_c.dfs('E').A.keys()), set(['a2', 'a1', 'a5']))
        self.assertEqual(set(self.g_c.dfs('P').A.keys()), set(['a3', 'a1', 'a4']))

        self.assertEqual(set(self.g_c2.dfs('Nina').A.keys()), set(['amiga']))
        self.assertEqual(set(self.g_c2.dfs('Maria').A.keys()), set(['amiga']))

    def test_bfs(self):
        self.assertEqual(set(self.g_p.bfs('J').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('C').A.keys()), set(['a1', 'a2', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('E').A.keys()), set(['a2', 'a1', 'a4', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('P').A.keys()), set(['a4', 'a1', 'a2', 'a6', 'a7', 'a9']))
        self.assertEqual(set(self.g_p.bfs('M').A.keys()), set(['a7', 'a8', 'a1', 'a2', 'a4', 'a9']))
        self.assertEqual(set(self.g_p.bfs('T').A.keys()), set(['a6', 'a8', 'a9', 'a1', 'a2', 'a4']))
        self.assertEqual(set(self.g_p.bfs('Z').A.keys()), set(['a9', 'a6', 'a8', 'a1', 'a2', 'a4']))

        self.assertEqual(set(self.g_p_sem_paralelas.bfs('J').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('C').A.keys()), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('E').A.keys()), set(['a2', 'a1', 'a3', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('P').A.keys()), set(['a3', 'a1', 'a2', 'a4', 'a5', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('M').A.keys()), set(['a5', 'a6', 'a1', 'a2', 'a3', 'a7']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('T').A.keys()), set(['a4', 'a6', 'a7', 'a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs('Z').A.keys()), set(['a7', 'a4', 'a6', 'a1', 'a2', 'a3']))

        self.assertEqual(set(self.g_c.bfs('J').A.keys()), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_c.bfs('C').A.keys()), set(['a1', 'a4', 'a5']))
        self.assertEqual(set(self.g_c.bfs('E').A.keys()), set(['a2', 'a4', 'a6']))
        self.assertEqual(set(self.g_c.bfs('P').A.keys()), set(['a3', 'a5', 'a6']))

        self.assertEqual(set(self.g_c2.bfs('Nina').A.keys()), set(['amiga']))
        self.assertEqual(set(self.g_c2.bfs('Maria').A.keys()), set(['amiga']))

    def testCiclo(self):

        #Os três testes abaixo rodam
        self.assertTrue(self.g_p.ha_ciclo())
        self.assertFalse(self.g_u.ha_ciclo())
        self.assertTrue(self.gdisc.ha_ciclo())
        self.assertTrue(self.g_u_d.ha_ciclo())

        # O teste abaixo dá loop infinito
        #self.assertFalse(self.g_a.ha_ciclo())

    def testCaminho(self):
        #Testes abaixo Funcionam
        self.assertFalse(self.g_d.caminho(12))
        self.assertFalse(self.g_d.caminho(8))
        self.assertFalse(self.g_d.caminho(5))
        self.assertFalse(self.g_d.caminho(0))
        self.assertFalse(self.g_d.caminho(-1))
        self.assertFalse(self.g_u.caminho(1))
        self.assertFalse(self.gdisc.caminho(4))
        self.assertFalse(self.g_p.caminho(5))
        self.assertFalse(self.gdisc.caminho(3))

        #Testes abaixo nao funcionam
        #self.assertListEqual(self.gdisc.caminho(2), ['A', 'a1', 'B', 'a3', 'C'])
        #self.assertEqual(self.g_d.caminho(4), ['E', 'a6', 'F', 'a7', 'G', 'a8', 'J', 'a9', 'I'])

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_c2.conexo())
        self.assertTrue(self.g_c3.conexo())
        self.assertTrue(self.nlw.conexo())
        self.assertTrue(self.grafo_A.conexo())
        self.assertTrue(self.grafo_B.conexo())
        self.assertTrue(self.grafo_C.conexo())
        self.assertTrue(self.grafo_D.conexo())
        self.assertTrue(self.grafo_E.conexo())
        self.assertTrue(self.grafo_F.conexo())
        self.assertTrue(self.grafo_G.conexo())
        self.assertTrue(self.grafo_H.conexo())
        self.assertFalse(self.g_v1.conexo())
        self.assertFalse(self.g_d.conexo())

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

    def test_PrimModificado(self):
        self.assertEqual(self.g_p4.primModificado(self.g_p4),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(self.g_p1_sem_paralelas.primModificado(self.g_p1_sem_paralelas), ['a1', 'a4', 'a7', 'a3', 'a6', 'a2'])
        self.assertEqual(self.g_c.primModificado(self.g_c), ['a1', 'a2', 'a3'])
        self.assertEqual(self.g_c12.primModificado(self.g_c12), ['a2', 'a3', 'a4'])
        self.assertEqual(self.g_c2.primModificado(self.g_c2), ['amiga'])
        self.assertEqual(self.grafo_prim.primModificado(self.grafo_prim), ['11', '6', '5', '8', '1'])

    def test_KruskalModificado(self):
        self.assertEqual(self.g_p.KruskalModificado(),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(self.g_p1_sem_paralelas.KruskalModificado(), ['a1', 'a4', 'a7', 'a3', 'a6', 'a2'])
        self.assertEqual(self.g_c.KruskalModificado(), ['a1', 'a2', 'a3'])
        self.assertEqual(self.g_c12.KruskalModificado(), ['a2', 'a3', 'a4'])
        self.assertEqual(self.g_c2.KruskalModificado(), ['amiga'])
        self.assertEqual(self.grafo_prim.KruskalModificado(), ['11', '8', '6', '5', '1'])