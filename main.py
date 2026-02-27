"""
Multi-Agent Research Team - FastAPI Server
Web UI for running the research crew and viewing results.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

from crew import ResearchCrew

app = FastAPI(title="Multi-Agent Research Team", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/research")
async def research(request: Request):
    try:
        body = await request.json()
        topic = body.get("topic", "").strip()
        platforms = body.get("platforms", "linkedin,twitter,newsletter").strip()
        if not topic:
            return JSONResponse({"error": "Topic is required"}, status_code=400)
        crew = ResearchCrew()
        result = crew.run(topic=topic, platforms=platforms)
        return JSONResponse(result)
    except Exception as e:
        return JSONResponse({"error": f"Research failed: {str(e)}"}, status_code=500)


@app.get("/api/health")
async def health():
    return {
        "status": "healthy",
        "anthropic_key_set": bool(os.getenv("ANTHROPIC_API_KEY")),
        "serper_key_set": bool(os.getenv("SERPER_API_KEY")),
        "framework": "CrewAI",
        "agents": 4,
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
