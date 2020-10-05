from pydantic import BaseModel
from typing import List


class WorkingExperienceDTO(BaseModel):
    title: str
    compagny: str
    city: str
    startMonth: str
    startYear: int
    endMonth: str
    endYear: int
    description: List[str]
    Stacks: List[str]
