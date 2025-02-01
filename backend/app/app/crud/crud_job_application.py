from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.job_application import Job_Application
from app.schemas.job_application import Job_ApplicationCreate, Job_ApplicationUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDJob_Application(CRUDBase[Job_Application, Job_ApplicationCreate, Job_ApplicationUpdate]):

    model = Job_Application

    def __init__(self):
        super().__init__(Job_Application)


job_application = CRUDJob_Application()
