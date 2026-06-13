from app.memory.store import MemoryStore
import json

async def health_check():
    return {"status": "ok"}

async def get_catalog():
    with open("catalog.json") as f:
        return json.load(f)

async def get_history(user_id: str):
    memory = MemoryStore()
    return memory.get_history(user_id)

async def wipe_memory(user_id: str):
    memory = MemoryStore()
    memory.wipe(user_id)
    return {"status": "wiped"}
