import flet as ft

from UI.view import View


class Controller:
    def __init__(self, view: View, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._country = None

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self._view.update_page()
        try:
            self._model.creaGrafo(int(self._view._txtAnno.value))
        except ValueError:
            self._view.create_alert("Inserisci un anno compreso tra 1816 e 2016!")
            return
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente", color="green"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumConnesse()} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))
        for country in self._model._listCountries:
            if country in self._model._grafo.nodes:
                self._view._txt_result.controls.append(ft.Text(f"{country.StateNme} -- {country.numVicini} vicini"))
        self._view._btnConnesse.disabled = False
        self._view.update_page()

    def handleRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        countryObj = self._model.getCountryDaCC(self._country)
        if countryObj in self._model._grafo.nodes:
            connComp = self._model.getConnessa(self._view._ddCountries.value)
        else:
            self._view.create_alert("Il grafo non contiene questo stato!")
            return
        if len(connComp) == 1:
            self._view.create_alert("Lo stato non è connesso con nessun altro stato!")
            return
        self._view._txt_result.controls.append(ft.Text(f"Di seguito le componenti connesse a {countryObj.__str__()}"))
        for c in connComp:
            self._view._txt_result.controls.append(ft.Text(f"{c}"))
        self._view.update_page()

    def fillDD(self):
        for country in self._model._listCountries:
            self._view._ddCountries.options.append(ft.dropdown.Option(key=country.CCode, text=country.__str__()))

    def read_country(self, e):
        self._country = e.control.value

