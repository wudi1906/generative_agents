# 由于使用本地 Ollama API，不再需要 OpenAI API key
# 保留此文件以维持项目结构，但移除不必要的配置

# 如果将来需要其他 API 密钥，可以在这里添加
API_CONFIG = {
    "use_local_llm": True,
    "llm_endpoint": "http://192.168.50.137:11434",
    "default_model": "deepseek-r1:14b"
}
