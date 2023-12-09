from pydantic import BaseModel


class BaselineStudentData(BaseModel):
    """
    Information about student suitable for baseline model.

    Attributes:
        interests (str): User's interests.
    """
    interests: str
