from pydantic import BaseModel
from typing import List

from .LocationDTO import LocationDTO


class EventDTO(BaseModel):
    title: str
    location: LocationDTO
    startDate: str
    endDate: str
    description: List[str]
