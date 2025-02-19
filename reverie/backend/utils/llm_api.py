import requests
import json
from .api_keys import API_CONFIG

OLLAMA_API_URL = API_CONFIG["llm_endpoint"]

def call_llm(prompt, model=API_CONFIG["default_model"]):
    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        
        # 打印原始响应以便调试
        print("Debug - Raw response:", response.text)
        
        response_json = response.json()
        
        # Ollama 的响应格式可能与 OpenAI 不同，需要适当处理
        if "response" in response_json:
            return response_json["response"]
        elif "choices" in response_json:
            return response_json["choices"][0]["text"]
        else:
            print(f"Unexpected response format: {response_json}")
            return str(response_json)
            
    except Exception as e:
        print(f"Error calling Ollama API: {str(e)}")
        print(f"Full error details: {e.__class__.__name__}")
        return None
