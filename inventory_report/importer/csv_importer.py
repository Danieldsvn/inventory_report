from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")
        return CsvImporter.data_treatment(path)

    @classmethod
    def data_treatment(cls, path):
        with open(path, encoding="utf8") as file:
            data = csv.reader(file, delimiter=",", quotechar='"')
            data_list = list(data)
            keys = data_list[0]
            companies_data_list = []
            for company_data in range(1, len(data_list)):
                companies_data_list.append(data_list[company_data])
            result = []
            for i in range(len(companies_data_list)):
                dictionary = {}
                for j in range(len(keys)):
                    dictionary[keys[j]] = companies_data_list[i][j]
                    if j == len(keys) - 1:
                        result.append(dictionary)

        return result
