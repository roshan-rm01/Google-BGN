from fastapi import FastAPI
from backend.models.organisation.model import Job
from backend.database.database_methods import Database

app = FastAPI()

@app.post('/job/create/', response_model=Job)
async def create_job(job: Job):
    return job

@app.get('/job/get/{job_id}/', response_model=Job)
async def get_job(job_id: int):
    return int

@app.put('/job/update/{job_id}/', response_model=Job)
async def update_job(job: Job):
    return job

@app.delete('job/delete/{job_id}/'):
    return {'model': 'deleted'}