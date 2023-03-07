from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if ".csv" in path:
            return Inventory.data_from_csv(path, report_type)
        if ".json" in path:
            return Inventory.data_from_json(path, report_type)
        if ".xml" in path:
            return Inventory.data_from_xml(path, report_type)

    def data_from_csv(path, report_type):
        data = CsvImporter.import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)

    def data_from_json(path, report_type):
        data = JsonImporter.import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)

    def data_from_xml(path, report_type):
        data = XmlImporter.import_data(path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        if report_type == "completo":
            return CompleteReport.generate(data)
