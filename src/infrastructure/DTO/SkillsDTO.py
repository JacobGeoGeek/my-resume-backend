from pydantic import BaseModel
from typing import List

from .TechnicalDTO import TechnicalDTO


class SkillsDTO(BaseModel):
    languages: List[str]
    technical: TechnicalDTO
