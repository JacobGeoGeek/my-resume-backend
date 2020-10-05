from pydantic import BaseModel


class GeneralInformationDTO(BaseModel):
    firstName: str
    lastName: str
    address: str
    city: str
    province: str
    postalCode: str
    mobilePhone: str
    homePhone: str
    email: str
    githubURL: str
