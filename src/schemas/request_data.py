from pydantic import BaseModel
from .baseline_student_data import BaselineStudentData


class RequestData(BaseModel):
    """
    Generic request data.

    Attributes:
        data (BaselineStudentData): Student data.
        res_length (int): Length of the response.
    """
    data: BaselineStudentData
    res_length: int
