import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._idMap = {}
        self._listCountries = DAO.getAllCountries()
        for country in self._listCountries:
            self._idMap[country.CCode] = country
        self._grafo = nx.Graph()

    def creaGrafo(self, anno):
        self.addEdges(anno)

    def addEdges(self, anno):
        self._grafo.clear_edges()
        allEdges, countries = DAO.getAllConnessioni(self._idMap, anno)
        self._grafo.add_nodes_from(countries)
        for e in allEdges:
            self._grafo.add_edge(e.state1, e.state2)

        # aggiungo il numero di vicini
        for c in self._grafo.nodes:
            c.numVicini = len(list(self._grafo.neighbors(c)))

    def getConnessa(self, countryCode):
        country = self._idMap[int(countryCode)]
        if country in self._grafo.nodes:
            connComp = nx.node_connected_component(self._grafo, country)
            return connComp
        else:
            return None

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)

    def checkExistence(self, idCountry):
        return idCountry in self._idMap

    def getNumConnesse(self):
        return nx.number_connected_components(self._grafo)

    def getCountryDaCC(self, ccCountry):
        return self._idMap[int(ccCountry)]
