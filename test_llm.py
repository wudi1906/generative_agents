from reverie.backend.utils.gpt_interface import gpt_completion, gpt_chat_completion

def test_basic_completion():
    prompt = "你好，请简单介绍一下你自己。"
    response = gpt_completion(prompt)
    print("Basic Completion Test:")
    print("Prompt:", prompt)
    print("Response:", response)
    print("\n" + "="*50 + "\n")

def test_chat_completion():
    messages = [
        {"role": "system", "content": "你是一个助手。"},
        {"role": "user", "content": "今天天气怎么样？"}
    ]
    response = gpt_chat_completion(messages)
    print("Chat Completion Test:")
    print("Messages:", messages)
    print("Response:", response)

if __name__ == "__main__":
    print("开始测试 LLM 接口...\n")
    test_basic_completion()
    test_chat_completion()
