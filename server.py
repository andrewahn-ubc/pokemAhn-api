from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import torch
import uvicorn

app = FastAPI(title = "NPC Dialogue API for pokemAhn")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pipeline("text-generation", "HuggingFaceTB/SmolLM2-360M-Instruct", temperature=0.7)


class PromptRequest(BaseModel):
    prompt: str

@app.post("/")
async def generate_text(request: PromptRequest):
    prompt = request.prompt
    result = model(
        prompt,
        max_new_tokens=20,    # limit response length
        do_sample=True,       # enable stochastic sampling
        top_p=0.9,            # nucleus sampling
        temperature=0.5       # add creativity
    )[0]["generated_text"]
    return {"response": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
