from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from src.model.baseline import run_baseline
from src.schemas.request_data import RequestData

app = FastAPI()
client_path = os.path.join(os.path.dirname(__file__), '..', 'client')

# Mount the static files route
app.mount("/static", StaticFiles(directory=client_path), name="static")

@app.get("/")
def read_root():
    """Serve the client app from root"""
    return FileResponse(os.path.join(client_path, 'index.html'))


@app.post("/api/model/baseline")
def post_model_baseline(req: RequestData):
    """Return a list of recommendations based on user's interests.

    Args:
        data (BaselineStudentData): The data to be processed.
        res_length (int): How many entries to produce.

    Returns:
        List: The results of the baseline model.
    """
    baseline_results = run_baseline(req.data, req.res_length)
    
    mapped_results = []
    
    for el in baseline_results:
        transformed_el = {
            'similar_interests': el[0] if len(el) > 0 else None,
            'match_percentage': el[1] if len(el) > 1 else None,
            'university': el[2] if len(el) > 2 else None
        }
        mapped_results.append(transformed_el)
    
    return mapped_results

