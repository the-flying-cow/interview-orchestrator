import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from api.routes import router as api_router


# 1. Initialization
app = FastAPI(title="Interview Orchestrator")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router)


@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse('static/index.html')
    
