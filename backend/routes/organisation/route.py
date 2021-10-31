from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Query
from odmantic import ObjectId
from pydantic import EmailStr

from database.database_methods import Database
from models.organisation.model import Job, JobResponse, JobDetails, JobFilters, Organisation
from utilities.validate_session import validate_org_session

job_router = APIRouter()
job_database = Database(Job)
org_database = Database(Organisation)


@job_router.post("/", response_model=List[JobDetails])
async def get_jobs(filters: JobFilters):
    filters: dict = filters.dict()
    # Implement feature that allows user find job matching just one of their skillset.
    jobs = []
    if all(val is None for val in filters.values()):
        jobs = [job for job in await job_database.find()]
        return jobs
    if filters:
        if filters["company"]:
            filtered_job = await job_database.find(Job.company.name == filters["company"])
            for job in filtered_job:
                jobs.append(job)
        if filters["skillset"]:
            filtered_job = await job_database.find(Job.skillset == filters["skillset"])
            for job in filtered_job:
                jobs.append(job)
        if filters["role"]:
            filtered_job = await job_database.find(Job.role == filters["role"])
            for job in filtered_job:
                jobs.append(job)
        if filters["title"]:
            filtered_job = await job_database.find(Job.title == filters["title"])
            for job in filtered_job:
                jobs.append(job)
        if filters["salary"]:
            filtered_job = await job_database.find(Job.salary == filters["salary"])
            for job in filtered_job:
                jobs.append(job)
        if filters["industry"]:
            filtered_job = await job_database.find(Job.industry == filters["industry"])
            for job in filtered_job:
                jobs.append(job)
        if filters["location"]:
            filtered_job = await job_database.find(Job.location == filters["location"])
            for job in filtered_job:
                jobs.append(job)

    return jobs


@job_router.post('/create/', response_model=JobResponse, dependencies=[Depends(validate_org_session)])
async def create_job(job_data: Job, session: EmailStr = Depends(validate_org_session)):
    # There's no way to check if there's an identical job for now.

    org_name: Organisation = await org_database.find_one(Organisation.email == session)

    job_data.company.name = org_name.companyName
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
