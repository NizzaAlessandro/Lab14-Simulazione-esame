import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGraph()
        listaArchi = list(self._model._grafo.edges(data=True))
        listaArchi.sort(key=lambda x : x[2]["weight"])
        nodi, archi = self._model.getNodesandEdges()
        self._view.txtResult.controls.append(ft.Text(f"Nodi = {nodi}-- Archi = {archi}"))
        """for a in listaArchi:
            self._view.txtResult.controls.append(ft.Text(a))"""
        self._view.txtResult.controls.append(ft.Text(f"Valore minimo {listaArchi[0][2]["weight"]}"))
        self._view.txtResult.controls.append(ft.Text(f"Valore massimo {listaArchi[-1][2]["weight"]}"))
        self._view.update_page()

        pass

    def handle_countedges(self, e):
        self._model.buildGraph()
        pre, post = self._model.archiPrePostSoglia(self._view.txt_name.value)
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia= {post}-"
                                                       f"- Numero archi con peso minore della soglia = {pre}"))
        self._view.update_page()
        pass

    def handle_search(self, e):
        pass