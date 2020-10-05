from pydantic import BaseModel
from typing import List


class GeomaticsDTO(BaseModel):
    CAD: List[str]
    GIS: List[str]
    other: List[str]
