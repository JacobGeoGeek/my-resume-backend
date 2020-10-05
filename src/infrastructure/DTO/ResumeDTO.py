from typing import List
from pydantic import BaseModel

from .GeneralInformationDTO import GeneralInformationDTO
from .EducationDTO import EducationDTO
from .SkillsDTO import SkillsDTO
from .WorkingExperienceDTO import WorkingExperienceDTO
from .EventDTO import EventDTO


class ResumeDTO(BaseModel):
    generalInformation: GeneralInformationDTO
    education: List[EducationDTO]
    skills: SkillsDTO
    workingExperiences: List[WorkingExperienceDTO]
    events: List[EventDTO]
    aboutMe: List[str]
