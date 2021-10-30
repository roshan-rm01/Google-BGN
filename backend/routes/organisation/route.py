from fastapi import APIRouter, Response, Depends, HTTPException, status, body
from models.organisation.model import Job
from database.database_methods import Database

job_router = APIRouter()
job_database = Database(Job)

@job_router.post('/job/create/', response_model=Job)
async def create_job(job_data: Job):
    # if job exists
    
    job_exists = await job_database.find_one(Job._id == job_data._id)
    if job_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Job post exists"
        )
    await job_database.save(job_data)
    return {
        "action": "Job Create",
        "message": "Job Post created"
    }

@job_router.get('/job/get/{job_id}/', response_model=Job)
async def get_job(job_id: int):
    get_job = await job_database.find_one(Job._id == job_id)
    if not get_job:
        raise HTTPException(
            status_code=404,
            detail="Job don't exist"
        )
    return get_job

@job_router.put('/job/update/{job_id}/', response_model=Job)
async def update_job(job_id: int, job_data: Job):
    get_job = await job_database.find_one(Job._id == job_id)
    if not get_job:
        raise HTTPException(
            status_code=404,
            detail="Job don't exist"
        )
    await job_database.save(job_data)
    return {
        "action": "Job Update",
        "message": "Job Post updated"
    }

@job_router.delete('job/delete/{job_id}/', response_model=Job):
async def delete_job(job_id: int):
    get_job = await job_database.find_one(Job._id == job_id)
    if not get_job:
        raise HTTPException(
            status_code=404,
            detail="Job don't exist"
        )
    await job_database.delete(get_job)
    return {
        "action": "Job Delete",
        "message": "Job Post deleted"
    }



