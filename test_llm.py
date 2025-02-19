import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from reverie.backend.utils.gpt_interface import gpt_completion, gpt_chat_completion

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test_endpoint():
    return jsonify({"status": "service is running"})

@app.route('/completion', methods=['POST'])
def completion():
    data = request.json
    prompt = data.get('prompt', '')
    response = gpt_completion(prompt)
    return jsonify({
        "prompt": prompt,
        "response": response
    })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    response = gpt_chat_completion(messages)
    return jsonify({
        "messages": messages,
        "response": response
    })

@app.route('/status', methods=['GET'])
def status():
    try:
        # 测试 Ollama 服务是否可用
        response = gpt_completion("test")
        status = "online" if response else "offline"
    except Exception as e:
        status = f"error: {str(e)}"
    
    return jsonify({
        "service": "deepseek-r1:14b",
        "status": status,
        "endpoint": "http://localhost:11434"
    })

if __name__ == "__main__":
    print("启动 LLM 服务...")
    app.run(host='0.0.0.0', port=5001, debug=True)
