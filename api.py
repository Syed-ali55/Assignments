#project/api.py
from fastapi import FastAPI
from scripts.core.services.student_services import student_router
app = FastAPI()
app.include_router(student_router)