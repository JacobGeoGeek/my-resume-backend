from pydantic import BaseModel


class EducationDTO(BaseModel):
    level: str
    schoolName: str
    province: str
    city: str
    degree: str
    startYear: int
    endYear: int
