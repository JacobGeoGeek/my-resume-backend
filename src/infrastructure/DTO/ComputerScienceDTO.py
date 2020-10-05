from pydantic import BaseModel
from typing import List


class ComputerScienceDTO(BaseModel):
    programmingLanguages: List[str]
    frameworks: List[str]
    tools: List[str]
