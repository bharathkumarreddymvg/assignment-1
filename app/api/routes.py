from fastapi import APIRouter
from app.services.chat_service import handle_chat
from app.services.eval_service import health_check, get_catalog, get_history, wipe_memory

router = APIRouter()

@router.post("/chat/{user_id}")
async def chat(user_id: str, message: dict):
    return await handle_chat(user_id, message["message"])

@router.get("/chat/{user_id}/history")
async def history(user_id: str):
    return await get_history(user_id)

@router.delete("/chat/{user_id}/memory")
async def delete_memory(user_id: str):
    return await wipe_memory(user_id)

@router.get("/catalog")
async def catalog():
    return await get_catalog()

@router.get("/health")
async def health():
    return await health_check()
