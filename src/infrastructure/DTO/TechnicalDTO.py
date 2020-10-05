from pydantic import BaseModel
from typing import List

from .ComputerScienceDTO import ComputerScienceDTO
from .GeomaticsDTO import GeomaticsDTO


class TechnicalDTO(BaseModel):
    office: List[str]
    geomatics: GeomaticsDTO
    computerScience: ComputerScienceDTO
