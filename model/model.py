import copy
import random
from math import sqrt
#from geopy.distance import geodesic

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        """self.studenti_diz ={}
        tutti_studenti = Corso_dao.get_tutti_studenti()
        for studente in tutti_studenti:
            self.studenti_diz[studente.matricola]= studente"""
        self._grafo = nx.DiGraph()
        self._nodes = None
        self._edges = None
        pass


    def buildGraph(self):
        self._grafo.clear()
        self._nodes = DAO.getNodes()
        self._grafo.add_nodes_from(self._nodes)
        self._edges = DAO.getEdges()
        for a in self._edges:
            self._grafo.add_edge(a.cromosoma1, a.cromosoma2, weight=float(a.expression_corr))
        pass

    def getNodesandEdges(self):
        return len(self._nodes), len(self._edges)

    def prendiArchiPesati(self):
        archi = DAO.getEdges()
        for a in archi:
            self._grafo.add_edge(a.cromosoma1,a.cromosoma2,weight=a.expression_corr)

    def archiPrePostSoglia(self,x):
        listaMaggiore=[]
        listaMinore=[]
        edges = DAO.getEdges()
        for e in edges:
            if float(e.expression_corr) == int(x):
                pass
            elif float(e.expression_corr) > int(x):
                listaMaggiore.append(e)
            else:
                listaMinore.append(e)
        return len(listaMinore), len(listaMaggiore)
        pass