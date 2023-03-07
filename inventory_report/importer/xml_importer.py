from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")
        xml_data = ET.parse(path)
        root = xml_data.getroot()
        data_list = []
        for children in root:
            dict = {}
            for index in range(len(children)):
                dict[children[index].tag] = children[index].text
            data_list.append(dict)
        return data_list
