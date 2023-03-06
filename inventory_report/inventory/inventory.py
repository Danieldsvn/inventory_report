from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        data = Inventory.csv_treatment(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)

    def csv_treatment(path):
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
