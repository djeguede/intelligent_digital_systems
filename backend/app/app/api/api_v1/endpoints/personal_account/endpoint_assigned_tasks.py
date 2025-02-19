import requests
from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

@router.get("/assigned_tasks", response_class=HTMLResponse, summary="Назначенные задачи")
async def assigned_task_page(request: Request):
    return TEMPLATES.TemplateResponse("personal_account/assigned_tasks.html", {"request": request})