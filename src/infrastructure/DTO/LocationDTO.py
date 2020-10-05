from pydantic import BaseModel


class LocationDTO(BaseModel):
    building: str
    address: str
    city: str
    province: str
