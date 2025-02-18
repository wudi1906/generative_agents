"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: gpt_structure.py
Description: Wrapper functions for calling local Deepseek model.
"""
import json
import time 

from utils import *
from persona.prompt_template.llm_adapters.deepseek_adapter import DeepseekAdapter

def ChatGPT_request(prompt): 
    """
    Given a prompt and returns the response from local Deepseek model.
    ARGS:
        prompt: a str prompt
    RETURNS: 
        a str of Deepseek's response. 
    """
    try: 
        llm = DeepseekAdapter()
        # 对于这个特定用例，我们不需要系统提示，直接使用用户提示
        messages = [
            {"role": "user", "content": prompt}
        ]
        result = llm.chat_completion(messages)
        return result
    
    except Exception as e: 
        print(f"Deepseek ERROR: {e}")
        return "Deepseek ERROR"

prompt = """
---
Character 1: Maria Lopez is working on her physics degree and streaming games on Twitch to make some extra money. She visits Hobbs Cafe for studying and eating just about everyday.
Character 2: Klaus Mueller is writing a research paper on the effects of gentrification in low-income communities.

Past Context: 
138 minutes ago, Maria Lopez and Klaus Mueller were already conversing about conversing about Maria's research paper mentioned by Klaus This context takes place after that conversation.

Current Context: Maria Lopez was attending her Physics class (preparing for the next lecture) when Maria Lopez saw Klaus Mueller in the middle of working on his research paper at the library (writing the introduction).
Maria Lopez is thinking of initating a conversation with Klaus Mueller.
Current Location: library in Oak Hill College

(This is what is in Maria Lopez's head: Maria Lopez should remember to follow up with Klaus Mueller about his thoughts on her research paper. Beyond this, Maria Lopez doesn't necessarily know anything more about Klaus Mueller) 

(This is what is in Klaus Mueller's head: Klaus Mueller should remember to ask Maria Lopez about her research paper, as she found it interesting that he mentioned it. Beyond this, Klaus Mueller doesn't necessarily know anything more about Maria Lopez) 

Here is their conversation. 

Maria Lopez: "