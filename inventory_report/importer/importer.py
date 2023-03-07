from abc import ABC, abstractmethod


class Importer(ABC):
    @classmethod
    @abstractmethod
    def import_data(cls):
        raise NotImplementedError
