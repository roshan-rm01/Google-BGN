from typing import List

from fastapi import APIRouter, HTTPException, Response, status, Depends
from odmantic import ObjectId

from database.database_methods import Database
from models.organisation.model import Job, JobResponse, JobDetails
from utilities.validate_session import validate_org_session

job_router = APIRouter()
job_database = Database(Job)


@job_router.get("/all", response_model=List[JobDetails])
async def get_jobs():
    jobs = [job for job in await job_database.find()]
    return jobs


@job_router.post('/create/', response_model=JobResponse, dependencies=[Depends(validate_org_session)])
async def create_job(job_data: Job):
    # There's no way to check if there's an identical job for now.
    await job_database.save(job_data)
    return {
        "action": "Job Created",
        "message": "Job Post created"
    }


@job_router.get('/get/{job_id}/', response_model=JobDetails, dependencies=[Depends(validate_org_session)])
async def get_job(job_id: ObjectId):
    job = await job_database.find_one(Job.id == job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job does not exist"
        )
    return job


@job_router.put('/update/{job_id}/', response_model=JobResponse, dependencies=[Depends(validate_org_session)])
async def update_job(job_id: ObjectId, job_data: Job):
    job = await job_database.find_one(Job.id == job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job don't exist"
        )
    await job_database.save(job_data)
    return {
        "action": "Job Update",
        "message": "Job details have been updated"
    }


@job_router.delete('/delete/{job_id}/', response_model=JobResponse, dependencies=[Depends(validate_org_session)])
async def delete_job(job_id: ObjectId):
    job = await job_database.find_one(Job.id == job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job does not exist!"
        )
    await job_database.delete(job)
    return {
        "action": "Job Delete",
        "message": "Job Post deleted"
    }
