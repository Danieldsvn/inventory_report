from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            json_data = file.read()
            data = json.loads(json_data)
        return data
