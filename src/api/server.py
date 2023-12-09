from fastapi import FastAPI

from src.model.baseline import run_baseline
from src.schemas.request_data import RequestData

app = FastAPI()


@app.get("/")
def read_root():
    """Stub function to make sure server runs.
    """
    return {"Project": "UniGoTo"}


@app.post("/model/baseline")
def post_model_baseline(req: RequestData):
    """Return a list of recommendations based on user's interests.

    Args:
        data (BaselineStudentData): The data to be processed.
        res_length (int): How many entries to produce.

    Returns:
        List: The results of the baseline model.
    """
    return run_baseline(req.data, req.res_length)
