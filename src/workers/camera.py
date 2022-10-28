from typing import Any
from src.config import Config


class Camera:
    def __init__(self, config: Config) -> None:
        self.config = config()

    def start(self):
        return "Start camera"

    def record(self):
        return "Record"

    def stop_record(self):
        return "Stop record"

    def stop(self):
        return "Stop camera"
