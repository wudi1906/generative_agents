from .llm_api import call_llm

def gpt_completion(prompt, temp=0.7, p=0.9, max_tokens=1500):
    """
    替换原有的 OpenAI GPT 调用
    """
    try:
        response = call_llm(prompt)
        return response
    except Exception as e:
        print(f"Error in GPT completion: {e}")
        return None

def gpt_chat_completion(messages, temp=0.7, p=0.9, max_tokens=1500):
    """
    处理聊天格式的提示
    """
    try:
        # 将消息列表转换为单个提示字符串
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        return call_llm(prompt)
    except Exception as e:
        print(f"Error in chat completion: {e}")
        return None 