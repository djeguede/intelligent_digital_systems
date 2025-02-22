from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.certificate import Certificate
from app.schemas.certificate import CertificateCreate, CertificateUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDCertificate(CRUDBase[Certificate, CertificateCreate, CertificateUpdate]):

    model = Certificate

    def __init__(self):
        super().__init__(Certificate)


certificate = CRUDCertificate()
