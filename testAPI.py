# Please install OpenAI SDK first: `pip3 install openai python-dotenv`
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # 加载当前目录下 .env 文件


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_BASE_URL")
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你是谁?你能做什么?"},
    ],
    stream=False,
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)