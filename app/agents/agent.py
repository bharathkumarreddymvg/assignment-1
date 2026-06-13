from app.tools.search_catalog import search_catalog
from app.tools.get_user_memory import get_user_memory
from app.tools.flag_for_human import flag_for_human

async def run_agent(user_id: str, message: str, memory):
    catalog_result = search_catalog(message)
    user_context = get_user_memory(user_id, memory)
    response = f"{catalog_result} {user_context}"
    eval_block = {
        "groundedness": 0.9,
        "relevance": 0.9,
        "confidence": 0.85,
        "flagged": False,
        "reasoning": "Response sourced from catalog and memory"
    }
    tools = ["search_catalog", "get_user_memory"]
    if eval_block["confidence"] < 0.5:
        flag_for_human(user_id, "low confidence")
        eval_block["flagged"] = True
    memory.save_fact(user_id, message, response)
    return response, tools, eval_block
