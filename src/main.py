from fastapi import FastAPI, Query

from .ressources.languageDTO import Languages
from .infrastructure.database import ResumeDataBase
from .repository import ResumeRepository
from .application.ServiceApplicationResume import ServiceApplicationResume

resumeDataBase: ResumeDataBase = ResumeDataBase()
resumeRepository: ResumeRepository = resumeDataBase
serviceApplication: ServiceApplicationResume = ServiceApplicationResume(
    resumeRepository)


app = FastAPI()


@app.get("/"):
def welcome():
    return "Welcome to the Resume Api"


@app.get("/{language}", description="Get the resume data based on the language.")
def getResume(language: Languages = Query(Languages)):
    return serviceApplication.getResume(language)
