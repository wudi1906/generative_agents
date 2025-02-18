"""
Adapter for local Deepseek model using Ollama
"""
import subprocess
import json

class DeepseekAdapter:
    def __init__(self, model_name="deepseek-r1:14b"):
        self.model = model_name

    def chat_completion(self, messages):
        """
        Generate chat completion using local Deepseek model via Ollama.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
        Returns:
            str: Generated response
        """
        # 将消息列表转换为单个提示
        prompt = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
        # 添加转义处理
        prompt = prompt.replace('"', '\\"')  # 转义双引号
        
        try:
            # 使用 ollama 命令行工具
            cmd = f'ollama run {self.model} "{prompt}"'
            print(f"Executing command: {cmd}")  # 添加日志
            
            result = subprocess.run(
                cmd, 
                shell=True, 
                capture_output=True, 
                text=True
            )
            
            if result.returncode != 0:
                print(f"Error from Ollama: {result.stderr}")
                return "Deepseek ERROR"
                
            print(f"Raw response: {result.stdout}")  # 添加日志
            response = result.stdout.strip()
            
            # 如果响应是 JSON 格式，尝试解析它
            try:
                if response.startswith("{") and response.endswith("}"):
                    return json.loads(response)
                return response
            except json.JSONDecodeError:
                return response
                
        except Exception as e:
            print(f"Error calling Deepseek via Ollama: {e}")
            return "Deepseek ERROR"

    def generate_response(self, prompt):
        """
        Simple wrapper for single prompt generation
        """
        messages = [{"role": "user", "content": prompt}]
        return self.chat_completion(messages)