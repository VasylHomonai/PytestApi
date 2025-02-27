import json
import os

class Endpoint:
    response = None
    response_json = None
    base_url = "https://api.restful-api.dev/objects"

    def get_full_url(self, endpoint=""):
        return f"{self.base_url}/{endpoint}" if endpoint else self.base_url

    def check_response_is_200(self):
        assert self.response.status_code == 200

    @staticmethod
    def load_json(file_path):
        """Читає JSON-файл і повертає його вміст у вигляді Python-словаря."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не знайдено")
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)