import requests
import json
from .api_keys import API_CONFIG
from .db_manager import DBManager

print("Loading LLM API with config:", API_CONFIG)

def call_llm(prompt, model=None):
    url = API_CONFIG["llm_endpoint"]
    try:
        print(f"Making request to: {url}")
        data = {
            "prompt": prompt,
            "stream": False
        }
        if model:
            data["model"] = model
            
        print(f"Request data: {data}")
        
        response = requests.post(
            url,
            json=data,
            timeout=30
        )
        
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            response_json = response.json()
            if "response" in response_json:
                return response_json["response"]
        
        return None
            
    except Exception as e:
        print(f"Error details: {str(e)}")
        print(f"URL attempted: {url}")
        return None 

# 创建数据库管理器实例
db = DBManager()

# 创建数字人
attributes = {
    "hobbies": ["reading", "painting"],
    "pet_name": "Fluffy",
    "personality": "friendly",
    "occupation": "teacher"
}

human_id = db.create_human(
    name="Isabella Rodriguez",
    age=25,
    gender="female",
    attributes=attributes
)

# 获取数字人信息
human = db.get_human_by_id(human_id)
print(human)

# 更新数字人信息
db.update_human(
    human_id,
    age=26,
    attributes={"hobbies": ["reading", "painting", "cooking"]}
)

# 获取家庭信息
family = db.get_family(human_id)
print(family) 