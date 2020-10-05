from typing import Set
from ..repository.ResumeRepository import InterfaceResumeRepository
from .setting.setting import Settings
from pymongo import MongoClient
from .DTO.ResumeDTO import ResumeDTO


class ResumeDataBase(InterfaceResumeRepository):

    def __init__(self) -> None:
        self.mongoClient = self._setUpMongoConnection()

    def getResume(self, language: str):
        result = self.mongoClient.MyResume.resume.find_one({}, {language: 1})
        return ResumeDTO(**result.get(language))

    def _setUpMongoConnection(self) -> MongoClient:
        return MongoClient(Settings().getDatabaseURL())
