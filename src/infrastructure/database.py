from typing import Set
from ..repository.ResumeRepository import InterfaceResumeRepository
from .setting.setting import Settings
from pymongo import MongoClient
from .DTO.ResumeDTO import ResumeDTO

setting: Settings = Settings()


class ResumeDataBase(InterfaceResumeRepository):

    def __init__(self) -> None:
        self.mongoClient = self._setUpMongoConnection()

    def getResume(self, language: str):
        result = self.mongoClient.MyResume.resume.find_one(
            {}, {language: True, '_id': False})
        return result[language]

    def _setUpMongoConnection(self) -> MongoClient:
        return MongoClient(setting.getDatabaseURL())
