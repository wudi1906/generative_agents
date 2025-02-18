"""
Author: Joon Sung Park (joonspk@stanford.edu)

File: gpt_structure.py
Description: Wrapper functions for calling local Deepseek model.
"""
import json
import time
from ..llm_adapters.deepseek_adapter import DeepseekAdapter

# 初始化 Deepseek 适配器
llm = DeepseekAdapter()

def generate_response(prompt, temperature=0.7):
    """
    Given a prompt, generate a response using the local Deepseek model.
    """
    try:
        messages = [{"role": "user", "content": prompt}]
        response = llm.chat_completion(messages)
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Deepseek ERROR"

def create_chat_completion(messages, temperature=0.7):
    """
    Given a list of messages, generate a chat completion using the local Deepseek model.
    """
    try:
        response = llm.chat_completion(messages)
        return {
            "choices": [{
                "message": {
                    "content": response
                }
            }]
        }
    except Exception as e:
        print(f"Error in chat completion: {e}")
        return {
            "choices": [{
                "message": {
                    "content": "Deepseek ERROR"
                }
            }]
        }

def get_chat_completion(messages):
    """
    Wrapper function for create_chat_completion that returns just the content.
    """
    try:
        response = create_chat_completion(messages)
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error getting chat completion: {e}")
        return "Deepseek ERROR"

def run_gpt_prompt(prompt, temp_sleep=True):
    """
    Legacy wrapper function for compatibility.
    """
    if temp_sleep:
        time.sleep(0.1)  # 减少延迟，因为是本地模型
    return generate_response(prompt)

def run_gpt_prompt_with_retry(prompt, temp_sleep=True, max_retries=3):
    """
    Retry wrapper for run_gpt_prompt.
    """
    for attempt in range(max_retries):
        try:
            return run_gpt_prompt(prompt, temp_sleep)
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"Final retry failed: {e}")
                return "Deepseek ERROR"
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(1)  # 短暂延迟后重试