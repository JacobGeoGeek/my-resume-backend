from ..repository.ResumeRepository import InterfaceResumeRepository
from pymongo import MongoClient
from .DTO.ResumeDTO import ResumeDTO
import pprint
client = MongoClient(
    "mongodb+srv://JacobChaar1:HEPU6VW3fSwwvsX@myresume.fjkvu.mongodb.net/MyResume?retryWrites=true&w=majority")


class ResumeDataBase(InterfaceResumeRepository):
    def __init__(self) -> None:
        self._db = client.MyResume

    def getResume(self, language: str):
        result = self._db.resume.find_one({}, {language: 1})
        return ResumeDTO(**result.get(language))
