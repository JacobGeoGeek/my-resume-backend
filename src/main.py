import uvicorn
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


@app.get("/{language}")
def getResume(language: Languages = Query(Languages, title="language", description="Select the language for the Resume")):
    return serviceApplication.getResume(language)
