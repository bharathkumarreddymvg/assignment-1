import uuid
from app.agents.agent import run_agent
from app.memory.store import MemoryStore

async def handle_chat(user_id: str, message: str):
    memory = MemoryStore()
    response, tools, eval_block = await run_agent(user_id, message, memory)
    return {
        "response": response,
        "eval": eval_block,
        "tools_called": tools,
        "session_id": str(uuid.uuid4())
    }
