from abc import ABC, abstractmethod

class BaseService(ABC):
    """
    Clase base abstracta para servicios.
    """
    @abstractmethod
    def get_by_id(self, entity_id):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, entity_id, data):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass


class CharacterService(BaseService):
    """
    Clase para manejar la lógica relacionada con 'character'.
    """
    def __init__(self, db_session):
        self.db_session = db_session

    def get_by_id(self, character_id):
        # Implementar lógica para obtener un personaje por su ID
        pass

    def create(self, character_data):
        # Implementar lógica para crear un nuevo personaje
        pass

    def update(self, character_id, character_data):
        # Implementar lógica para actualizar un personaje existente
        pass

    def delete(self, character_id):
        # Implementar lógica para eliminar un personaje
        pass

    @classmethod
    def service_info(cls):
        return "CharacterService: Maneja operaciones relacionadas con personajes."


class AzureCognitiveService:
    """
    Clase para manejar la interacción con el servicio cognitivo de Azure.
    """
    def __init__(self, azure_credentials):
        self.azure_credentials = azure_credentials

    def analyze_text(self, text):
        # Implementar lógica para analizar texto usando el servicio cognitivo
        pass

    def detect_language(self, text):
        # Implementar lógica para detectar el idioma de un texto
        pass

    def extract_key_phrases(self, text):
        # Implementar lógica para extraer frases clave de un texto
        pass

    @classmethod
    def service_info(cls):
        return "AzureCognitiveService: Maneja operaciones relacionadas con el servicio cognitivo de Azure."
