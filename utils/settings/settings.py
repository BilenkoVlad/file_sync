from typing import Dict

settings = None


def get_settings():
    global settings
    if not settings:
        settings = Settings()

    return settings


class Settings:
    _settings: dict = {}

    def __init__(self):
        self.source_file = self._settings.get("source_file")
        self.replica_file = self._settings.get("replica_file")
        self.seconds_period = self._settings.get("seconds_period")

    @classmethod
    def update_settings(cls, update_settings: Dict[str, str]) -> None:
        cls._settings.update(update_settings)
