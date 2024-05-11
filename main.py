# main.py
from fastapi import FastAPI, Request
import httpx

app = FastAPI()
GROQ_API_URL = 'https://api.groq.com/openai/v1'  # 替换为 Groq API 的实际端点

@app.api_route('/{path:path}', methods=['GET', 'POST', 'PUT', 'DELETE'])
async def proxy(path: str, request: Request):
    method = request.method
    body = await request.body()
    
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method,
            f"{GROQ_API_URL}/{path}",
            headers=request.headers,
            content=body,
        )
        return response.content
