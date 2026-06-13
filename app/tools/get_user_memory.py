def get_user_memory(user_id: str, memory):
    history = memory.get_history(user_id)
    if history:
        return f"Previous context: {history[-1]}"
    return ""
